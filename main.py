import sys
from PySide6.QtWidgets import QApplication, QWidget


from output import Ui_Form 

class MyWorkshopApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.MainPages.setCurrentIndex(0)
        
        self.ui.loginRegisterBtn.clicked.connect(self.changeToRegister)
        self.ui.registerLoginBtn.clicked.connect(self.changeToLogin)

    def changeToRegister(self):
        self.ui.MainPages.setCurrentIndex(1)

    def changeToLogin(self):
        self.ui.MainPages.setCurrentIndex(0)

    def login(self):
        username = self.ui.loginUsername.toPlainText().strip()
        passwrod = self.ui.loginPassword.toPlainText().strip()
        

if __name__ == "__main__":
   
    app = QApplication(sys.argv)    

    window = MyWorkshopApp()
    window.show()
    
    
    sys.exit(app.exec())