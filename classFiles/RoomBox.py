from include.pyside6Import import *
from classFiles.RoomClass import RoomObj

# -------------------- Room Card --------------------
class RoomBox(QFrame):
    clicked = Signal(object)
    def __init__(self, room: RoomObj): 
        super().__init__() 
        self.room = room 

        self.setObjectName("roomCard")

        # 1. Set margins and spacing to 0 so inner labels fill the frame perfectly
        layout = QVBoxLayout(self) 
        layout.setContentsMargins(0, 0, 0, 0) 
        layout.setSpacing(0) 

        # 2. Title Label (Header)
        title = QLabel(f"{self.room.getRoomID()} : {self.room.getRoomName()}") 
        # Apply rounded corners ONLY to the top to match the outer frame
        title.setStyleSheet(f"""
            background-color: {self.room.getColor()};
            color: #11111b; /* Dark text for better contrast against bright colors */
            font-size: 15px;
            font-weight: bold;
            padding: 12px 15px;
            border-top-left-radius: 11px;
            border-top-right-radius: 11px;
        """) 
        
        # 3. Description Label (Body)
        desc = QLabel(self.room.getDescription()) 
        desc.setWordWrap(True) 
        desc.setAlignment(Qt.AlignTop | Qt.AlignLeft) # Push text to the top instead of centering
        # Apply rounded corners ONLY to the bottom
        desc.setStyleSheet("""
            background-color: #313244;
            color: #cdd6f4;
            font-size: 13px;
            padding: 15px;
            border-bottom-left-radius: 11px;
            border-bottom-right-radius: 11px;
        """) 

        # 4. Outer Frame Styling
        self.setStyleSheet("""
            #roomCard {
                background-color: transparent;
                border: 1px solid #45475a; /* Thinner, softer border */
                border-radius: 12px;
            }
            #roomCard:hover {
                border: 1px solid #89b4fa; /* Accent color border on hover */
            }
        """)

        # Add widgets. No stretch on title so it hugs the text, stretch=1 on desc so it fills the rest
        layout.addWidget(title) 
        layout.addWidget(desc, stretch=1)

        self.setMinimumSize(220, 160) 
        self.setMaximumSize(440, 280) 
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum) 
        
        # 5. Add a pointer cursor for better UX
        self.setCursor(Qt.PointingHandCursor)
        self.setMouseTracking(True) 

    def mousePressEvent(self, event): 
        self.clicked.emit(self.room.getRoomID())
        super().mousePressEvent(event)