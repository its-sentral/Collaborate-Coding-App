from include.pyside6Import import *
from classFiles.pages.authenPage import Authen


MODERN_STYLE = """
/* Global Background and Font */
QWidget {
    background-color: #1e1e2e;
    color: #cdd6f4;
    font-family: 'Segoe UI', Arial, sans-serif;
}

/* Headings and Titles */
QLabel {
    color: #cdd6f4;
}

/* Specific styling for your Title Labels (Login, Register, etc.) */
QLabel#label_2, QLabel#label_3, QLabel#label_4, QLabel#label_15, QLabel#roomCode {
    color: #89b4fa;
    font-size: 24px;
    font-weight: bold;
}

/* Input Fields (QTextEdit, QLineEdit) */
QTextEdit, QLineEdit {
    background-color: #313244;
    border: 2px solid #45475a;
    border-radius: 8px;
    padding: 8px;
    color: #cdd6f4;
    font-size: 14px;
}

QTextEdit:focus, QLineEdit:focus {
    border: 2px solid #89b4fa;
    background-color: #1e1e2e;
}

/* Standard Buttons */
QPushButton {
    background-color: #89b4fa;
    color: #11111b;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: bold;
    font-size: 14px;
}

QPushButton:hover {
    background-color: #b4befe;
}

QPushButton:pressed {
    background-color: #74c7ec;
}

/* Secondary Buttons (Cancel, Logout) */
QPushButton#loginRegisterBtn, QPushButton#createRoomCancleBtn, QPushButton#joinRoomCancleBtn, QPushButton#homeLogoutBtn {
    background-color: #45475a;
    color: #cdd6f4;
}

QPushButton#loginRegisterBtn:hover, QPushButton#createRoomCancleBtn:hover, QPushButton#joinRoomCancleBtn:hover, QPushButton#homeLogoutBtn:hover {
    background-color: #585b70;
}

/* Sidebar / Menu Buttons (Room Chat, Call, Workshop, Member) */
QPushButton#roomChatBtn, QPushButton#roomCallBtn, QPushButton#roomWorkshopBtn, QPushButton#roomMemberBtn {
    background-color: transparent;
    color: #a6adc8;
    border: 2px solid transparent;
    text-align: left;
    padding-left: 15px;
}

QPushButton#roomChatBtn:hover, QPushButton#roomCallBtn:hover, QPushButton#roomWorkshopBtn:hover, QPushButton#roomMemberBtn:hover {
    background-color: #313244;
    border-left: 4px solid #89b4fa;
    color: #cdd6f4;
}

/* Scroll Areas and Lists */
QScrollArea, QListView {
    border: none;
    background-color: transparent;
}

QListView::item {
    padding: 10px;
    border-bottom: 1px solid #313244;
}

QListView::item:selected {
    background-color: #313244;
    color: #89b4fa;
    border-radius: 5px;
}

/* Scrollbars */
QScrollBar:vertical {
    border: none;
    background-color: #1e1e2e;
    width: 10px;
    margin: 0px 0px 0px 0px;
}

QScrollBar::handle:vertical {
    background-color: #45475a;
    min-height: 20px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background-color: #585b70;
}
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(MODERN_STYLE)
    window = Authen()
    window.resize(600, 420)
   
    window.show()
    sys.exit(app.exec())