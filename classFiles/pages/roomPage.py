from include.pyside6Import import *
from include.lib import *
from uiFiles.output import Ui_Form
from classFiles.RoomClass import RoomObj
from classFiles.UserClass import User, Member, Admin
from ..client import VideoCallApp
from PySide6.QtCore import QStringListModel, QTimer
from .demo import CollabEditor
from dotenv import load_dotenv
import requests, os

load_dotenv()

motherServer = "https://collaborate-coding-app.onrender.com"


class CodeEditor(QPlainTextEdit): # Switched to QPlainTextEdit for stability
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lineNumberArea = LineNumberArea(self)

        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)

        self.updateLineNumberAreaWidth(0)
        self.highlightCurrentLine()
        
        # VS Code style
        # Inside CodeEditor.__init__
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
        space = 20 + self.fontMetrics().horizontalAdvance('9') * digits
        return space

    def updateLineNumberAreaWidth(self, _):
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
        # 1. Fill background
        painter.fillRect(event.rect(), QColor("#1e1e1e"))

        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = round(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + round(self.blockBoundingRect(block).height())

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(blockNumber + 1)
                painter.setPen(QColor("#858585")) # VS Code dim text
                painter.drawText(0, top, self.lineNumberArea.width() - 8, self.fontMetrics().height(),
                                 Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + round(self.blockBoundingRect(block).height())
            blockNumber += 1


        painter.setPen(QColor("#333333"))
        painter.drawLine(event.rect().width() - 1, event.rect().top(), 
                         event.rect().width() - 1, event.rect().bottom())
        
        painter.end()

class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.codeEditor = editor

    def sizeHint(self):
        return QSize(self.codeEditor.lineNumberAreaWidth(), 0)

    def paintEvent(self, event):
        self.codeEditor.lineNumberAreaPaintEvent(event)


class RoomPage(QObject):
    def __init__(self, user, ui :Ui_Form, window: QMainWindow, room: RoomObj):
        super().__init__(window)

        self.user = user
        self.ui = ui
        self.window = window
        self.room = room
        print(f"DEBUG: Entering room with URL: {self.room.server_url}")
        
        self.chatContents = QWidget()
        self.chatLayout = QVBoxLayout(self.chatContents)
        self.chatLayout.setAlignment(Qt.AlignTop)
        self.ui.chatHistoryArea.setWidget(self.chatContents)
        self.ui.chatHistoryArea.setWidgetResizable(True)

        self.callCreated = False
        self.open_output_windows = []

        self.ui.MainPages.setCurrentIndex(5)
        self.ui.SubPages.setCurrentIndex(0)
        self.ui.roomName.setText(self.room.getRoomName())
        self.ui.roomCode.setText(self.room.getRoomID())

        self.ui.roomChatBtn.clicked.connect(self.goToChat)
        self.ui.roomCallBtn.clicked.connect(self.goToCall)
        self.ui.roomWorkshopBtn.clicked.connect(self.goToWorkShop)
        self.ui.roomMemberBtn.clicked.connect(self.goToMember)
        self.ui.roomHomeBtn.clicked.connect(self.backToHome)

        self.work = CollabEditor()
        self.ui.VLWorkShop.addWidget(self.work,stretch=1)

        self.ui.chatSendTextConfirmBtn.clicked.connect(self.sendChatMessage)
        self.chat_timer = QTimer()
        self.chat_timer.timeout.connect(self.refreshChat)
        self.chat_timer.start(3000)


        self.ui.workshopRunBtn.clicked.connect(self.compile_code)

    def compile_code(self):
        CLIENT_ID = os.getenv("CLIENT_ID")
        CLIENT_SECRET = os.getenv("CLIENT_SECRET")
        
        code = self.work.getText()

        # Disable the run button so the user doesn't spam it while waiting
        self.ui.workshopRunBtn.setEnabled(False)
        print("Compiling code in the cloud... Please wait.")

        # Create and start the background thread
        self.compiler_thread = JDoodleCompilerThread(code, CLIENT_ID, CLIENT_SECRET)
        self.compiler_thread.compilation_finished.connect(self.display_code_output)
        self.compiler_thread.start()
        
    def display_code_output(self, result):
        print("=== EXECUTION OUTPUT ===")
        print(result)
        
        new_window = OutputWindow(result)
        self.open_output_windows.append(new_window)
        new_window.show()
        self.ui.workshopRunBtn.setEnabled(True)
        
    def sendChatMessage(self):
        text = self.ui.chatSendTextEdit.toPlainText().strip()
        if not text:
                    return
    
        payload = {
                "username": self.user.getName(),
                "text": text,
                "roomID": self.room.getRoomID()
            }
        
        try:
            base_url = self.room.getServerURL()
            url = f"{base_url}/send_chat" 
            res = requests.post(url, json=payload, timeout=5)
            
            if res.status_code == 200:
                self.ui.chatSendTextEdit.clear()
                self.refreshChat()
        except Exception as e:
            print(f"Chat Error: {e}")

    def refreshChat(self):
        try:
            if self.chatLayout is None:
                self.chat_timer.stop()
                return
        except RuntimeError:
            print("UI deleted, stopping chat timer.")
            self.chat_timer.stop()
            return
        try:
            base_url = self.room.getServerURL()
            url = f"{base_url}/get_chat"
            params = {"roomID": self.room.getRoomID()}
            res = requests.get(url, params=params, timeout=5)

            if res.status_code == 200:
                messages = res.json()

               
                while self.chatLayout.count():
                    item = self.chatLayout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
                for msg in messages:
                    
                    chat_text = f"<b>{msg['sender']}</b>: {msg['content']} <br><small style='color:gray'>{msg['time']}</small>"
                    
                    lbl = QLabel(chat_text)
                    lbl.setWordWrap(True) # Wrap long text
                    lbl.setStyleSheet("""
                        background-color: #3e3e3e; 
                        color: white; 
                        padding: 8px; 
                        border-radius: 10px; 
                        margin-bottom: 2px;
                    """)
                    
                    self.chatLayout.addWidget(lbl)

              
                self.ui.chatHistoryArea.verticalScrollBar().setValue(
                    self.ui.chatHistoryArea.verticalScrollBar().maximum()
                )

        except Exception as e:
            print(f"Chat Refresh Error: {e}")

    def goToChat(self):
        self.ui.SubPages.setCurrentIndex(0)

    def goToCall(self):
        if not self.callCreated:
            self.callCreated = not self.callCreated
            self.videoWidget = VideoCallApp()
            self.ui.VLCall.addWidget(self.videoWidget,stretch=1)
        self.ui.SubPages.setCurrentIndex(1)

    def goToWorkShop(self):
        self.ui.SubPages.setCurrentIndex(2)

    def goToMember(self):
        self.ui.SubPages.setCurrentIndex(3)
        self.ui.listView.clearSelection()
        try:
            room_id = self.room.getRoomID()
            base_url = self.room.getServerURL()
            response = requests.get(f"{base_url}/get_members?roomID={room_id}", timeout=5)
            
            if response.status_code == 200:
                member_names = response.json().get("members", [])
                
                
                model = QStringListModel()
                display_list = []
                for name in member_names:
                   
                    prefix = "👑 " if name == self.room.getAdmin().getName() else "👤 "
                    display_list.append(f"{prefix}{name}")
                model.setStringList(display_list)
                self.ui.listView.setModel(model)
            else:
                print("Failed to fetch members from server")
        except Exception as e:
            print(f"Error updating member list: {e}")
    
    def backToHome(self):
        if hasattr(self, 'chat_timer'):
            self.chat_timer.stop()
        self.user = None

        if self.callCreated and hasattr(self, 'videoWidget') and self.videoWidget:
            self.videoWidget.leave_call()
            self.ui.VLCall.removeWidget(self.videoWidget)
            self.videoWidget.deleteLater()
            self.videoWidget = None
            self.callCreated = False

        try:
            self.ui.roomChatBtn.clicked.disconnect()
            self.ui.roomCallBtn.clicked.disconnect()
            self.ui.roomWorkshopBtn.clicked.disconnect()
            self.ui.roomMemberBtn.clicked.disconnect()
            self.ui.roomHomeBtn.clicked.disconnect()
            self.ui.workshopRunBtn.clicked.disconnect()
        except RuntimeError:
            pass # Failsafe in case they are already disconnected

        self.ui.MainPages.setCurrentIndex(2)

class JDoodleCompilerThread(QThread):
    compilation_finished = Signal(str)

    def __init__(self, code_to_compile, client_id, client_secret, parent=None):
        super().__init__(parent)
        self.code_to_compile = code_to_compile
        self.client_id = client_id
        self.client_secret = client_secret

    def run(self):
        print("[Thread] 1. Background thread started!")
        
        if not self.client_id or not self.client_secret:
            self.compilation_finished.emit("Error: CLIENT_ID or CLIENT_SECRET is missing. Check your .env file!")
            return

        url = "https://api.jdoodle.com/v1/execute"
        payload = {
            "clientId": self.client_id,
            "clientSecret": self.client_secret,
            "script": self.code_to_compile,
            "language": "python3",
            "versionIndex": "4"
        }
        
        try:
            print("[Thread] 2. Sending code to JDoodle...")
            
            # ADDED TIMEOUT: If JDoodle doesn't respond in 15 seconds, force an error!
            response = requests.post(url, json=payload, timeout=15) 
            
            print(f"[Thread] 3. Got response! Status Code: {response.status_code}")
            
            try:
                response_data = response.json()
            except Exception:
                # If JDoodle crashes and returns HTML instead of JSON
                self.compilation_finished.emit(f"Server Error. Raw response: {response.text}")
                return

            if response.status_code == 200:
                result = response_data.get("output", "No output returned.")
            else:
                result = f"API Error {response.status_code}: {response_data.get('error', 'Unknown Error')}"
                
        except requests.exceptions.Timeout:
            result = "Error: The request timed out. JDoodle took more than 15 seconds to respond."
            print("[Thread] ERROR: Request timed out!")
        except Exception as e:
            result = f"Failed to connect to JDoodle: {e}"
            print(f"[Thread] ERROR: Exception caught: {e}")
            
        print("[Thread] 4. Emitting result back to main app...")
        self.compilation_finished.emit(result)

class OutputWindow(QWidget):
    def __init__(self, result_text):
        super().__init__()
        self.setWindowTitle("JDoodle Output")
        self.resize(500, 400)
        layout = QVBoxLayout(self)
        self.text_area = QPlainTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setPlainText(result_text)
        self.text_area.setStyleSheet("""
            QPlainTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 14px;
                border: 1px solid #333333;
            }
        """)
        
        layout.addWidget(self.text_area)
