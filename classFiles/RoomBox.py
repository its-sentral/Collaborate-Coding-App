from include.pyside6Import import *
from classFiles.RoomClass import RoomObj

# -------------------- Room Card --------------------
class RoomBox(QFrame):
    clicked = Signal(object)
    def __init__(self, room: RoomObj): 
        super().__init__() 
        self.room = room 

        self.setObjectName("roomCard")

        layout = QVBoxLayout(self) 
        layout.setContentsMargins(6, 6, 6, 6) 
        layout.setSpacing(4) 
        

        title = QLabel(f"{self.room.getRoomID()} : {self.room.getRoomName()}") 
        title.setStyleSheet( f"background-color:{self.room.getColor()};" "font-weight:bold;" "padding:6px;" ) 
        desc = QLabel(self.room.getDescription()) 
        desc.setWordWrap(True) 

        desc.setStyleSheet( "background-color:#4C4C4C;" "color:white;" "padding:6px;" ) 

        self.setStyleSheet("""
            #roomCard {
                background-color: #2E2E2E;
                border: 2px solid #888;
                border-radius: 12px;
            }
            #roomCard:hover {
                border: 2px solid #FFF;
                background-color: #3A3A3A;
            }
        """)

        layout.addWidget(title, stretch=3) 
        layout.addWidget(desc, stretch=7)

        self.setMinimumSize(220, 140) 
        self.setMaximumSize(440, 280) 
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum) # Handle Hover 
        self.baseGeometry = None 
        self.setMouseTracking(True) 

        
    def mousePressEvent(self, event): 
        self.clicked.emit(self.room.getRoomID())
        super().mousePressEvent(event)