from include.pyside6Import import *
from include.lib import *
from uiFiles.output import Ui_Form
from classFiles.RoomBox import RoomBox
from classFiles.pages.roomPage import RoomPage,RoomObj
import requests
import random
from classFiles.UserClass import Admin

motherServer = "https://your-mother-server.onrender.com"
roomServerOne = "https://serveroneroom.onrender.com"
# -------------------- Main Window --------------------
class Home(QObject):
    def __init__(self, user, ui :Ui_Form, parentWindow):
        super().__init__()

        self.ui = ui
        self.window = parentWindow
        self.currentRoom = None

        
        self.user = user
        
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

        self.performSearch()
    def backToHome(self):
        self.ui.MainPages.setCurrentIndex(2)

    def addNewRoom(self):
        roomId = self.ui.joinRoomCode.toPlainText().strip()
        if not roomId:
            print("Please enter a Room ID")
            return
        
        payload = {
            "username": self.user.getName(),
            "roomID": roomId
        }
        try:
            # 2. Tell the server this user wants to join
            response = requests.post(f"{roomServerOne}/join_room", json=payload, timeout=10)
            
            if response.status_code == 200:
                print(f"Successfully joined room {roomId}!")
                
                # 3. Refresh the local data so the new room appears on the Home grid
                self.syncWithServer() 
                
                # 4. Go back to Home
                self.backToHome()
            else:
                print(f"Failed to join: {response.json().get('detail', 'Unknown error')}")
                
        except Exception as e:
            print(f"Error joining room: {e}")
    
    def createNewRoom(self):
        roomName = self.ui.createRoomName.toPlainText().strip()
        roomDesc = self.ui.createRoomDescription.toPlainText().strip()

        roomID = str(random.randint(0,100))
        roomColor = "#3498db"

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
           
            response = requests.post(f"{roomServerOne}/claim_server", json=payload, timeout=10)
            
            if response.status_code == 200:
                print(f"Success: Room '{roomName}' is now live on Render!")
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
                    admin=local_admin
                )

                self.user.rooms.append(new_local_room)
                self.performSearch()
                self.syncWithServer()
                self.backToHome()
                
            else:
                print(f"Server rejected: {response.text}")
        except Exception as e:
            print(f"Failed to connect to Room Server: {e}")

    
    def gotoLogout(self):
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
        # 1. Calculate columns based on current window width
        someCardWidth = 300
        available_width = self.ui.scrollArea.viewport().width()
        columns = max(2, available_width // someCardWidth)

        # 2. THE FIX: Only 'return' if the window didn't resize AND we aren't forcing a refresh
        if self.colAmount is not None and columns == self.colAmount and not ignore:
            return

        # 3. Update the state and WIPE the old UI
        self.colAmount = columns
        self.clearGrid()

        # 4. If the user has no rooms, stop here (screen is now clean and empty)
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
        
        # This tells the UI to repaint everything in the grid
        self.ui.scrollAreaWidget.update()
        
        # Ensure the widget inside the scroll area is actually visible
        self.ui.scrollAreaWidget.show()
        print(f"Successfully drew {len(self.filtered_rooms)} room(s).")

    def handleRoomSelection(self, room_id):
        for room in self.user.getRooms():
            if room.getRoomID() == room_id:
                self.currentRoom = RoomPage(self.user, self.ui, self.window, room)
                break
    
    def syncWithServer(self):

        print(f"Checking server for {self.user.getName()}...")
        try:

            url = "https://serveroneroom.onrender.com/room_info"
            params = {"username": self.user.getName()}
            
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if data.get("status") == "active":

                    creator_data = self.user
                    if data.get("role") == "admin":
                        creator_data = Admin(
                            gmail=self.user.getGmail(),
                            name=self.user.getName(),
                            id=self.user.getID(),
                            pno=self.user.getPhoneNo()
                        )

                    new_room = RoomObj(
                        Rname=data["name"],
                        RID=data["roomID"],
                        desc=data.get("description", ""),
                        color=data.get("color", "#3498db"),
                        admin=creator_data
                    )

                    # 3. Update the user's local room list
                    self.user.rooms = [new_room]
                    print("Room found and synced!")
                else:
                    # No active room for this user
                    self.user.rooms = []
                    print("No active rooms found on server.")

                # 4. Refresh the UI Grid
                self.performSearch() 

        except Exception as e:
            print(f"Sync Error: {e}")
