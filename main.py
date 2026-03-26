import sys
from PySide6.QtWidgets import QApplication, QWidget
import requests
from uiFiles.output import Ui_Form
from classFiles.SystemClass import LoginSystem, RegisterSystem
from uiFiles.output import Ui_Form as Ui_Home


class ColabCodingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.currentUser = None 
        self.ui.MainPages.setCurrentIndex(0)


        self.baseUrl = "https://collaborate-coding-app.onrender.com"
        self.loginSys = LoginSystem(self.baseUrl)
        self.regSys = RegisterSystem(self.baseUrl)

        self.ui.loginRegisterBtn.clicked.connect(self.changeToRegister)
        self.ui.registerLoginBtn.clicked.connect(self.changeToLogin)
        
        self.ui.homeCreateRoomBtn.clicked.connect(self.changeToHome)
        self.ui.createRoomCancleBtn.clicked.connect(self.changeToCreateRoom)

        self.ui.homeAddRoomBtn.clicked.connect(self.changeToAddRoom)
        self.ui.loginConfirmBtn.clicked.connect(self.login)
        self.ui.registerConfirmBtn.clicked.connect(self.register)
        

        self.ui.createRoomConfirmBtn.clicked.connect(self.createRoom)

    def changeToRegister(self):
        self.ui.MainPages.setCurrentIndex(1)
    def changeToAddRoom(self):
        self.ui.MainPages.setCurrentIndex(5)
    def changeToLogin(self):
        self.ui.MainPages.setCurrentIndex(0)
    def changeToHome(self):
        self.ui.MainPages.setCurrentIndex(3)
    def changeToCreateRoom(self):
        self.ui.MainPages.setCurrentIndex(2)


    def register(self):
        username = self.ui.registerUsername.toPlainText().strip()
        passwrod = self.ui.registerPassword.toPlainText().strip()
        confirmPassword = self.ui.registerConfirmPassword.toPlainText().strip()

        success, message = self.regSys.addUser(username, passwrod, confirmPassword)
        if success:
            print("Registration Successful!")
            self.ui.MainPages.setCurrentIndex(0)
        else:
            print(f"Registration Failed: {message}")

    
    def login(self):
        username = self.ui.loginUsername.toPlainText().strip()
        password = self.ui.loginPassword.toPlainText().strip()

        success, data = self.loginSys.check(username, password)

        if success:
            self.currentUser = username
            self.homeScreen = HomeWidget(self.currentUser, parent=self.ui.MainPages)
            if self.ui.MainPages.widget(2):
                oldWidget = self.ui.MainPages.widget(2)
                self.ui.MainPages.removeWidget(oldWidget)
                
            self.ui.MainPages.insertWidget(2, self.homeScreen)
        
            self.ui.MainPages.setCurrentIndex(2)
        else:
            print(f"Login failed: {data}")

    def createRoom(self):
        pass



class HomeWidget(QWidget):
    def __init__(self, username, parent=None):
        super().__init__(parent)
        self.ui = Ui_Home()
        self.ui.setupUi(self)
        
        self.ui.userName.setText(username)
        self.ui.logoutBtn.clicked.connect(self.logout)

    def logout(self):
        # We'll handle this in the main app
        self.parent().setCurrentIndex(0)
        

if __name__ == "__main__":
   
    app = QApplication(sys.argv)    
    window = ColabCodingApp()
    window.show()
    sys.exit(app.exec())