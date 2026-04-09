import sys
import re
from PySide6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QVBoxLayout, QWidget, QLabel
from PySide6.QtNetwork import QAbstractSocket
from PySide6.QtWebSockets import QWebSocket
from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor
from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QPainter, QColor, QTextFormat, QPaintEvent
from PySide6.QtWidgets import QTextEdit

class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.codeEditor = editor

    def sizeHint(self):
        return QSize(self.codeEditor.lineNumberAreaWidth(), 0)

    def paintEvent(self, event: QPaintEvent):
        self.codeEditor.lineNumberAreaPaintEvent(event)


class CodeEditor(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lineNumberArea = LineNumberArea(self)

        # Connect signals to keep line numbers in sync with text
        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)

        self.updateLineNumberAreaWidth(0)
        self.highlightCurrentLine()

        # Dark theme styling
        self.setStyleSheet("""
            QPlainTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 14px;
                border: 1px solid #333333;
                border-radius: 2px;
            }
        """)

    def lineNumberAreaWidth(self):
        digits = 1
        max_val = max(1, self.blockCount())
        while max_val >= 10:
            max_val /= 10
            digits += 1
        space = 25 + self.fontMetrics().horizontalAdvance('9') * digits
        return space

    def updateLineNumberAreaWidth(self, _):
        # This reserves the blank space on the left side of the editor
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    def updateLineNumberArea(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())
        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))

    def highlightCurrentLine(self):
        extraSelections = []
        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            lineColor = QColor("#2a2d2e") # VS Code dark gray highlight
            selection.format.setBackground(lineColor)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)
        self.setExtraSelections(extraSelections)

    def lineNumberAreaPaintEvent(self, event: QPaintEvent):
        painter = QPainter(self.lineNumberArea)
        
        # Fill the background of the line number area
        painter.fillRect(event.rect(), QColor("#1e1e1e"))

        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = round(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + round(self.blockBoundingRect(block).height())

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(blockNumber + 1)
                painter.setPen(QColor("#858585")) # VS Code dim text for numbers
                painter.drawText(0, top, self.lineNumberArea.width() - 8, self.fontMetrics().height(),
                                 Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + round(self.blockBoundingRect(block).height())
            blockNumber += 1

        # Draw a subtle separator line between numbers and code
        painter.setPen(QColor("#333333"))
        painter.drawLine(event.rect().width() - 1, event.rect().top(), 
                         event.rect().width() - 1, event.rect().bottom())
        painter.end()

class CollabEditor(QWidget):
    def __init__(self,roomID):
        super().__init__()
        self.setWindowTitle("PySide6 Workshop Demo")
        self.resize(800, 600)
       
        self.editor = CodeEditor()
        
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
        
        self.server_url = f"wss://worshop-demo-branch.onrender.com/ws/{roomID}" 
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
    window = CollabEditor(11)
    window.show()
    sys.exit(app.exec())