from include.pyside6Import import *
from include.lib import *
from uiFiles.output import Ui_Form
from classFiles.pages.homePage import Home
from classFiles.RoomClass import RoomObj
from classFiles.UserClass import Admin, User, Member
from classFiles.SystemClass import LoginSystem, RegisterSystem

mainBackGroundColor = "#2550B0"
authenAreaColor = "#0B1D42"
goToRegisterOrLoginBtnColor = "#4488AA"
confirmBtnColor = "#44AA88"


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        # Set up the UI from the generated file
        self.ui = Ui_Form()
        self.ui.setupUi(self)


# -------------------- Authentication Window --------------------
class Authen(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        self.ui = Ui_Form()
        self.ui.setupUi(central_widget)
    
        self.user = None
        self.home = Home(None, self.ui, self)


        self.ui.MainPages.setCurrentIndex(0)
        self.ui.loginConfirmBtn.clicked.connect(self.loginConfirm)
        self.ui.loginRegisterBtn.clicked.connect(self.returnToRegister)


        self.ui.registerConfirmBtn.clicked.connect(self.createNewUser)
        self.ui.registerLoginBtn.clicked.connect(self.returnToLogin)

        self.baseUrl = "https://collaborate-coding-app.onrender.com"
        self.loginSys = LoginSystem(self.baseUrl)
        self.regSys = RegisterSystem(self.baseUrl)



        # Setup Login Page
        pixmap = QPixmap("uiFiles\image\AuthenSideImage.jpg")
        pixmap.scaled(4, 3, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.ui.loginImage.setPixmap(pixmap)
        self.ui.loginImage.setScaledContents(False)

        self.ui.FrameLogin.setStyleSheet(f"background-color: {mainBackGroundColor}; border-top-right-radius: 30px; border-bottom-right-radius: 30px;")
        self.ui.FrameLoginImage.setStyleSheet("border-radius: 20px;")


        self.ui.FrameLoginArea.setStyleSheet(f"background-color: {authenAreaColor};")
        self.setTextBox(self.ui.loginUsername)
        self.setTextBox(self.ui.loginPassword)
        self.setStyleSheet(f"background-color: {mainBackGroundColor};")

        self.setButton(self.ui.loginConfirmBtn, confirmBtnColor)
        self.setButton(self.ui.loginRegisterBtn, goToRegisterOrLoginBtnColor)


        # Setup Register Page
        self.ui.registerImage.setPixmap(pixmap)
        self.ui.registerImage.setScaledContents(False)
        self.ui.FrameRegister.setStyleSheet(f"background-color: {mainBackGroundColor}; border-top-right-radius: 30px; border-bottom-right-radius: 30px;")
        self.ui.FrameRegisterImageContainer.setStyleSheet("border-radius: 20px;")
        self.ui.FrameRegisterArea.setStyleSheet(f"background-color: {authenAreaColor};")

        self.setTextBox(self.ui.registerUsername)
        self.setTextBox(self.ui.registerGmail)
        self.setTextBox(self.ui.registerPhoneNumber)
        self.setTextBox(self.ui.registerPassword)
        self.setTextBox(self.ui.registerConfirmPassword)

        self.setButton(self.ui.registerConfirmBtn, confirmBtnColor)
        self.setButton(self.ui.registerLoginBtn, goToRegisterOrLoginBtnColor)






        # adm = Admin("gmail1", "name1", 0, 0)
        # data = [
        #     Room("Physics Lab", "A101", "Experiments and equipment", "#AA4444", adm),
        #     Room("Computer Room", "B202", "Coding and projects", "#4488AA", adm),
        #     Room("Art Studio", "C303", "Creative workspace", "#44AA88", adm),
        #     Room("Math Room", "D404", "Problem solving zone", "#AA8844", adm),
        #     Room("Chemistry Lab", "E505", "Chemical experiments", "#8844AA", adm),
        #     Room("Biology Lab", "F606", "Microscopes and specimens", "#44AA44", adm),
        #     Room("Library", "G707", "Books and study area", "#AAAA44", adm),
        #     Room("Music Room", "H808", "Instruments and practice", "#44AAAA", adm),
        # ]
        # self.user = User("123@g.com", "Mrs.Tester 101", 1, 50, data)

    def setTextBox(self, obj):
        obj.setStyleSheet("border-radius: 10px; background-color: #fff; color: #000; font-size: 18px; font-weight: bold;")
        obj.setCursorWidth(2)
        obj.setContentsMargins(5, 5, 5, 5)


    def setButton(self, obj, color):
        obj.setStyleSheet(f"border-radius: 10px; background-color: {color}; color: #000; font-size: 18px; font-weight: bold;")
        obj.setCursor(Qt.PointingHandCursor)
        obj.setContentsMargins(5, 5, 5, 5)


    def loginConfirm(self):
        username = self.ui.loginUsername.toPlainText().strip()
        password = self.ui.loginPassword.toPlainText().strip()
        if not username or not password:
            print("Login failed: username or password can't be blank")
            return
        
        success, data = self.loginSys.check(username, password)

        if success:
            print(f"FULL SERVER RESPONSE: {data}")
            u_info = data.get('user_data')
            self.user = Member(
                            gmail=u_info['gmail'],
                            name=u_info['name'],
                            id=u_info['id'],
                            pno=u_info['phone'],
                            memOf=u_info['rooms'] 
                        )
            self.home.user = self.user
            self.home.syncWithServer()
            self.home.updatedHome()
            self.ui.MainPages.setCurrentIndex(2)
           
        else:
            print(f"Login failed: {data}")
       

    def returnToRegister(self):
        self.ui.MainPages.setCurrentIndex(1)

    def createNewUser(self):
        username = self.ui.registerUsername.toPlainText().strip()
        password = self.ui.registerPassword.toPlainText().strip()
        gmail = self.ui.registerGmail.toPlainText().strip()
        phone = self.ui.registerPhoneNumber.toPlainText().strip()
        confirmPassword = self.ui.registerConfirmPassword.toPlainText().strip()

        success, message = self.regSys.addUser(username,gmail,phone, password, confirmPassword)
        if success:
            print("Registration Successful!")
            self.ui.MainPages.setCurrentIndex(0)
        else:
            print(f"Registration Failed: {message}")

    def returnToLogin(self):
        self.ui.MainPages.setCurrentIndex(0)
    
    # -------------------- Responsive Resize --------------------
    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.home:
            self.home.rebuildGrid()