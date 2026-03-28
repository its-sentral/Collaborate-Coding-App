from include.pyside6Import import *
from include.lib import *
from uiFiles.output import Ui_Form
from classFiles.RoomClass import RoomObj
from classFiles.UserClass import User, Member, Admin

class RoomPage(QObject):
    def __init__(self, user, ui :Ui_Form, window: QMainWindow, room: RoomObj):
        super().__init__(window)

        self.user = user
        self.ui = ui
        self.window = window
        self.room = room

        self.ui.MainPages.setCurrentIndex(5)
        self.ui.SubPages.setCurrentIndex(0)
        self.ui.roomName.setText(self.room.getRoomName())
        self.ui.roomCode.setText(self.room.getRoomID())

        self.ui.roomChatBtn.clicked.connect(self.goToChat)
        self.ui.roomCallBtn.clicked.connect(self.goToCall)
        self.ui.roomWorkshopBtn.clicked.connect(self.goToWorkShop)
        self.ui.roomMemberBtn.clicked.connect(self.goToMember)
        self.ui.roomHomeBtn.clicked.connect(self.backToHome)

    def goToChat(self):
        self.ui.SubPages.setCurrentIndex(0)

    def goToCall(self):
        self.ui.SubPages.setCurrentIndex(1)

    def goToWorkShop(self):
        self.ui.SubPages.setCurrentIndex(2)

    def goToMember(self):
        self.ui.SubPages.setCurrentIndex(3)
    
    def backToHome(self):
        self.ui.MainPages.setCurrentIndex(2)