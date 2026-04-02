from include.pyside6Import import *
from classFiles.pages.authenPage import Authen


MODERN_STYLE = """

"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(MODERN_STYLE)
    window = Authen()
    window.resize(600, 420)
   
    window.show()
    sys.exit(app.exec())