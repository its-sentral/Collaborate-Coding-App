import sys
import re
from PySide6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QVBoxLayout, QWidget, QLabel
from PySide6.QtNetwork import QAbstractSocket
from PySide6.QtWebSockets import QWebSocket
from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor


class CollabEditor(QWidget):
    def __init__(self,roomid):
        super().__init__()
        self.setWindowTitle("PySide6 Workshop Demo")
        self.resize(800, 600)
       
        self.editor = QPlainTextEdit()
        
        self.editor.setPlaceholderText("Start coding here...")
        self.status_label = QLabel("Status: Disconnected")
        font = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        font.setPointSize(12)
        self.editor.setFont(font)
        self.editor.setReadOnly(True)
        self.status_label.setText("Connecting and fetching code...")
        self.highlighter = PythonHighlighter(self.editor.document())

        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.editor)
        
        self.setLayout(layout)

    
        self.socket = QWebSocket()
        self.socket.connected.connect(self.on_connected)
        self.socket.disconnected.connect(self.on_disconnected)
        self.socket.textMessageReceived.connect(self.on_message_received)
        
        self._is_receiving = False

        self.editor.textChanged.connect(self.send_code_update)
        
        self.server_url = f"wss://worshop-demo-branch.onrender.com/ws/{roomid}" 
        self.socket.open(QUrl(self.server_url))

    def getText(self):
        return self.editor.toPlainText()

    def send_code_update(self):
        if not self._is_receiving:
            code = self.editor.toPlainText()
            if self.socket.state() == QAbstractSocket.ConnectedState:
                self.socket.sendTextMessage(code)

    def on_connected(self):
            # We are connected, but waiting for the server to send the 'initial' code
            self.status_label.setText("Status: Connected - Fetching Code...")
            self.status_label.setStyleSheet("color: #cca700;") # Yellow/Orange

    def on_message_received(self, message):
        self._is_receiving = True
        
        cursor = self.editor.textCursor()
        pos = cursor.position()
        
        self.editor.setPlainText(message)
        
        cursor.setPosition(pos)
        self.editor.setTextCursor(cursor)
        
        # This is the 'Sync' breakthrough:
        if self.editor.isReadOnly() or "Syncing" in self.status_label.text():
            self.editor.setReadOnly(False)
            self.status_label.setText("Status: Online & Synced")
            self.status_label.setStyleSheet("color: #4EC9B0;") # Teal/Green
            
        self._is_receiving = False

    def on_disconnected(self):
        self.editor.setReadOnly(True)
        self.status_label.setText("Status: Disconnected (Server Sleeping?)")
        self.status_label.setStyleSheet("color: #F44336;") # Red
        
class PythonHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.rules = []

        # Define styles
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#569CD6")) # VS Code Blue
        keyword_format.setFontWeight(QFont.Weight.Bold)

        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#CE9178")) # Orange/Peach

        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6A9955")) # Green

        # Simple rules for Python
        keywords = ["def", "class", "if", "else", "import", "from", "return", "for", "while"]
        for word in keywords:
            pattern = rf"\b{word}\b"
            self.rules.append((re.compile(pattern), keyword_format))

        self.rules.append((re.compile(r"#[^\n]*"), comment_format))     # Comments
        self.rules.append((re.compile(r"\"[^\"]*\""), string_format))   # Strings
        self.rules.append((re.compile(r"\'[^\']*\'"), string_format))   # Strings

    def highlightBlock(self, text):
        for pattern, fmt in self.rules:
            for match in pattern.finditer(text):
                self.setFormat(match.start(), match.end() - match.start(), fmt)

                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CollabEditor()
    window.show()
    sys.exit(app.exec())