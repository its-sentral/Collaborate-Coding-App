from include.pyside6Import import *
from include.lib import *
from uiFiles.output import Ui_Form
from classFiles.pages.homePage import Home
from classFiles.RoomClass import RoomObj
from classFiles.UserClass import Admin, User, Member


# -------------------- Authentication Window --------------------
class Authen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.user = None
        self.home = None


        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        self.ui = Ui_Form()
        self.ui.setupUi(central_widget)


        self.ui.MainPages.setCurrentIndex(0)
        self.ui.loginConfirmBtn.clicked.connect(self.loginConfirm)
        self.ui.loginRegisterBtn.clicked.connect(self.returnToRegister)


        self.ui.registerConfirmBtn.clicked.connect(self.createNewUser)
        self.ui.registerLoginBtn.clicked.connect(self.returnToLogin)

       



        adm = Admin("gmail1", "name1", 0, 0)
        data = [
            RoomObj("Physics Lab", "A101", "Experiments and equipment", "#AA4444", adm),
            RoomObj("Computer Room", "B202", "Coding and projects", "#4488AA", adm),
            RoomObj("Art Studio", "C303", "Creative workspace", "#44AA88", adm),
            RoomObj("Math Room", "D404", "Problem solving zone", "#AA8844", adm),
            RoomObj("Chemistry Lab", "E505", "Chemical experiments", "#8844AA", adm),
            RoomObj("Biology Lab", "F606", "Microscopes and specimens", "#44AA44", adm),
            RoomObj("Library", "G707", "Books and study area", "#AAAA44", adm),
            RoomObj("Music Room", "H808", "Instruments and practice", "#44AAAA", adm),
        ]
        self.user = User("123@g.com", "Mrs.Tester 101", 1, 50, data)

        
    def loginConfirm(self):
        self.ui.MainPages.setCurrentIndex(2)
        self.home = Home(self.user, self.ui, self)

    def returnToRegister(self):
        self.ui.MainPages.setCurrentIndex(1)

    def createNewUser(self):
        self.ui.MainPages.setCurrentIndex(2)
        self.home = Home(self.user, self.ui, self)

    def returnToLogin(self):
        self.ui.MainPages.setCurrentIndex(0)
    
    # -------------------- Responsive Resize --------------------
    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.home:
            self.home.rebuildGrid()