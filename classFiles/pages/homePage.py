from include.pyside6Import import *
from include.lib import *
from uiFiles.output import Ui_Form
from classFiles.RoomBox import RoomBox
from classFiles.pages.roomPage import RoomPage,RoomObj
import requests
import random
from classFiles.UserClass import Admin

motherServer = "https://collaborate-coding-app.onrender.com"
roomServerOne = "https://serveroneroom.onrender.com"

UI_COLORS = [
    "#3498db", # Blue
    "#e74c3c", # Red
    "#2ecc71", # Green
    "#f1c40f", # Yellow
    "#9b59b6", # Purple
    "#1abc9c", # Teal
    "#e67e22", # Orange
    "#34495e"  # Dark Blue/Gray
]
# -------------------- Main Window --------------------
class Home(QObject):
    def __init__(self, user, ui :Ui_Form, parentWindow):
        super().__init__()

        self.ui = ui
        self.window = parentWindow
        self.currentRoom = None
        self.servers = [
           "https://serveroneroom.onrender.com",
           "https://servertworoom.onrender.com"

        ]
        self.creation_count = 0
        
        self.user = user
        self.server_url = ""

        self.filtered_rooms = []


        # Connect search bar to trigger search on every text change
        self.ui.homeSearchBar.textChanged.connect(self.performSearch)

        # Use the grid created by Designer
        self.grid = QGridLayout()
        self.grid.setSpacing(20)
        self.ui.scrollAreaWidget.setLayout(self.grid)

        self.colAmount = None


    def updatedHome(self):
        self.ui.homeUserName.setText(str(self.user.getName()))
                # home
        self.ui.homeLogoutBtn.clicked.connect(self.gotoLogout)
        self.ui.homeAddRoomBtn.clicked.connect(self.goToAddRoom)
        self.ui.homeCreateRoomBtn.clicked.connect(self.goToCreateRoom)

        # join room
        self.ui.joinRoomConfirm.clicked.connect(self.addNewRoom)
        self.ui.joinRoomCancleBtn.clicked.connect(self.backToHome)

        # create room
        self.ui.createRoomConfirmBtn.clicked.connect(self.createNewRoom)
        self.ui.createRoomCancleBtn.clicked.connect(self.backToHome)
        # info_res = requests.get(f"{roomServerOne}/room_info", params={"username": self.user.getName()})
        # if info_res.status_code == 200:
        #     data = info_res.json()
        #     new_room = RoomObj(
        #         Rname=data["name"],
        #         RID=data["roomID"],
        #         desc=data["description"],
        #         color=data["color"],
        #         admin=Admin(name="Admin", gmail="ea", id="12", pno="9"),
        #         mem=[] 
        #     )
        #     self.user.rooms.append(new_room)
        #     self.performSearch() 
        #     self.backToHome()

        self.performSearch()
    def backToHome(self):
        self.ui.MainPages.setCurrentIndex(2)
    def randomColor():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        return(r,g,b)
    def addNewRoom(self):
        roomId = self.ui.joinRoomCode.toPlainText().strip()
        if not roomId:
            print("Please enter a Room ID")
            return
        
        payload = {
            "username": self.user.getName(),
            "roomID": roomId
        }
        found_room = False

        try:
            
            for base_url in self.servers:
                print(f"Checking server: {base_url} for Room {roomId}...")
                
                try:
                
                    join_url = f"{base_url}/join_room"
                    response = requests.post(join_url, json=payload, timeout=5)
                    
                    if response.status_code == 200:
                        print(f"Successfully joined room {roomId} on {base_url}!")
                        
                        info_res = requests.get(f"{base_url}/room_info", params={"username": self.user.getName()})
                        
                        if info_res.status_code == 200:
                            data = info_res.json()
                            
                            new_room = RoomObj(
                                Rname=data["name"],
                                RID=data["roomID"],
                                desc=data.get("description", ""),
                                color=data.get("color"),
                                admin=Admin(name=data.get("admin_name", "Admin"), gmail="", id="", pno=""),
                               
                                server_url=base_url 
                            )
                            
                            self.user.rooms.append(new_room)
                            found_room = True
                            break 
                except Exception as e:
                    print(f"Server {base_url} skipped: {e}")
                    continue

            if found_room:
                self.performSearch() 
                self.backToHome()
            else:
                print("Room ID not found on any available server.")
                    
        except Exception as e:
            print(f"Error joining room: {e}")


    def createNewRoom(self):
        roomName = self.ui.createRoomName.toPlainText().strip()
        roomDesc = self.ui.createRoomDescription.toPlainText().strip()

        server_index = self.creation_count % 2
        selected_server_url = self.servers[server_index]
        roomID = str(random.randint(0,100))
        roomColor = random.choice(UI_COLORS)

        if not roomName:
            print("ROOM CAN'T BE EMPTY")
            return
    
        payload = {
            "name": roomName,
            "description": roomDesc,
            "roomID": roomID,
            "color": roomColor,
            #admin data
            "admin_name": str(self.user.getName()),
            "admin_gmail": str(self.user.getGmail()),
            "admin_id": str(self.user.getID()),
            "admin_pno": str(self.user.getPhoneNo())
        }
        try:
           
            response = requests.post(f"{selected_server_url}/claim_server", json=payload, timeout=10)
            
            if response.status_code == 200:
                print(f"Success: Room '{roomName}' is now live on Render!")
                self.creation_count += 1
                local_admin = Admin(
                        gmail=self.user.getGmail(),
                        name=self.user.getName(),
                        id=self.user.getID(),
                        pno=self.user.getPhoneNo()
                    )
                new_local_room = RoomObj(
                    Rname=payload["name"],
                    RID=payload["roomID"],
                    desc=payload["description"],
                    color=payload["color"],
                    admin=local_admin,
                    server_url=selected_server_url
                )

                self.user.rooms.append(new_local_room)
                self.performSearch()
                self.backToHome()
                
            else:
                print(f"Server rejected: {response.text}")
        except Exception as e:
            print(f"Failed to connect to Room Server: {e}")

    
    def gotoLogout(self):

        if hasattr(self, 'chat_timer'):
            self.chat_timer.stop()
        self.ui.homeLogoutBtn.clicked.disconnect()
        self.ui.homeAddRoomBtn.clicked.disconnect()
        self.ui.homeCreateRoomBtn.clicked.disconnect()
        
        self.ui.joinRoomConfirm.clicked.disconnect()
        self.ui.joinRoomCancleBtn.clicked.disconnect()
        self.ui.createRoomConfirmBtn.clicked.disconnect()
        self.ui.createRoomCancleBtn.clicked.disconnect()
    
        self.clearGrid()
        
        self.user = None
        self.filtered_rooms = []
        
        self.ui.MainPages.setCurrentIndex(0)
        
        print("Logout successful: Home state has been reset and signals disconnected.")

    def goToAddRoom(self):
        self.ui.MainPages.setCurrentIndex(4)
    
    def goToCreateRoom(self):
        self.ui.MainPages.setCurrentIndex(3)


    # -------------------- Search --------------------
    def performSearch(self):
        text = self.ui.homeSearchBar.text().lower().strip()

        # Show all if search is empty
        if not text:
            self.filtered_rooms = list(self.user.getRooms())
        else:
            self.filtered_rooms = [
                v for v in self.user.getRooms()
                if text in v.getRoomName().lower()
                or text in v.getDescription().lower()
                or text in str(v.getRoomID()).lower()
            ]

        self.rebuildGrid(ignore=True)

    # -------------------- Grid Helpers --------------------
    def clearGrid(self):
        while self.grid.count():
            item = self.grid.takeAt(0)
            widget = item.widget()
            if widget:
                    widget.setParent(None) 
                    widget.deleteLater()

    def rebuildGrid(self, ignore=False):
       
        someCardWidth = 300
        available_width = self.ui.scrollArea.viewport().width()
        columns = max(2, available_width // someCardWidth)

     
        if self.colAmount is not None and columns == self.colAmount and not ignore:
            return

       
        self.colAmount = columns
        self.clearGrid()

        
        if not self.filtered_rooms:
            print("Grid cleared: No rooms found for this user.")
            return

        row = col = 0
        for room in self.filtered_rooms:
            card = RoomBox(room)
            
            card.clicked.connect(self.handleRoomSelection)
            
            self.grid.addWidget(card, row, col)

            col += 1
            if col >= self.colAmount:
                col = 0
                row += 1
        self.grid.activate()

        self.ui.scrollAreaWidget.adjustSize()
        self.ui.scrollAreaWidget.update()

        self.ui.scrollAreaWidget.show()
        print(f"Successfully drew {len(self.filtered_rooms)} room(s).")

    def handleRoomSelection(self, room_id):
        for room in self.user.getRooms():
            if room.getRoomID() == room_id:
                self.currentRoom = RoomPage(self.user, self.ui, self.window, room)
                break
    
    def syncWithServer(self):
        print(f"Checking all servers for {self.user.getName()}...")
        self.user.rooms = [] # Start fresh
        
    
        server_urls = [
            "https://serveroneroom.onrender.com",
            "https://servertworoom.onrender.com"
        ]

        try:
            for base_url in server_urls:
                url = f"{base_url}/room_info"
                params = {"username": self.user.getName()}
                
                try:
                    response = requests.get(url, params=params, timeout=5)
                    
                    if response.status_code == 200:
                        data = response.json()
                        
                        if data.get("status") == "active":
                            # Determine the Admin
                            if data.get("role") == "admin":
                                admin_obj = Admin(
                                    gmail=self.user.getGmail(),
                                    name=self.user.getName(),
                                    id=self.user.getID(),
                                    pno=self.user.getPhoneNo()
                                )
                            else:
                                admin_obj = Admin(
                                    name=data.get("admin_name", "Unknown Admin"),
                                    gmail="", id="", pno="" 
                                )
                            
                            # Create the Room Object
                            new_room = RoomObj(
                                Rname=data["name"],
                                RID=data["roomID"],
                                desc=data.get("description", ""),
                                color=data.get("color", "#3498db"),
                                admin=admin_obj,
                                server_url=base_url
                            )

                            # CRITICAL: Attach the server URL so the app 
                            # knows which server to use for THIS specific room
                            new_room.server_url = base_url
                            
                            self.user.rooms.append(new_room)
                            print(f"Room '{data['name']}' found and synced from {base_url}!")
                            
                            # If you only allow ONE active room per user across all servers, 
                            # you can 'break' the loop here.
                            # break 

                except Exception as e:
                    print(f"Could not reach server {base_url}: {e}")

            # After checking all servers, refresh the UI
            self.performSearch() 

        except Exception as e:
            print(f"General Sync Error: {e}")