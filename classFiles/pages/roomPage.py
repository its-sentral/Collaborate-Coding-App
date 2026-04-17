from include.pyside6Import import *
from include.lib import *
from uiFiles.output import Ui_Form
from classFiles.RoomClass import RoomObj, Workshop
from classFiles.UserClass import User, Member, Admin
from ..client import VideoCallApp
from PySide6.QtCore import QStringListModel, QTimer
from .demo import CollabEditor
from dotenv import load_dotenv
import requests, os
from shiboken6 import isValid
from PySide6.QtCore import QObject, Signal

load_dotenv()

motherServer = "https://collaborate-coding-app.onrender.com"


RoomBackGroundColor = "#1E1E2F"
RoomTopBarColor = "#2E2E3E"
RoomSectionBtnAreaColor = "#2E2E3E"
RoomSectionDisplayAreaColor = "#1E1E2F"




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
                background-color: #1e1e2e;
                color: #cdd6f4;
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 14px;
                border: 2px solid #313244;
                border-radius: 8px;
                padding: 4px;
            }
            QPlainTextEdit:focus {
                border: 2px solid #89b4fa; /* Glows blue when typing */
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
            lineColor = QColor("#313244") # VS Code dark gray highlight
            selection.format.setBackground(lineColor)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)
        self.setExtraSelections(extraSelections)

    def lineNumberAreaPaintEvent(self, event: QPaintEvent):
        painter = QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), QColor("#181825"))

        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = round(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + round(self.blockBoundingRect(block).height())

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(blockNumber + 1)
                painter.setPen(QColor("#a6adc8")) # VS Code dim text
                painter.drawText(0, top, self.lineNumberArea.width() - 8, self.fontMetrics().height(),
                                 Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + round(self.blockBoundingRect(block).height())
            blockNumber += 1


        painter.setPen(QColor("#45475a"))
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

class ChatFetchThread(QThread):
    chat_fetched = Signal(list)

    def __init__(self, url, room_id, parent=None):
        super().__init__(parent)
        self.url = url
        self.room_id = room_id

    def run(self):
        try:
            res = requests.get(self.url, params={"roomID": self.room_id}, timeout=5)
            if res.status_code == 200:
                self.chat_fetched.emit(res.json())
        except Exception as e:
            print(f"Background Chat Fetch Error: {e}")

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
        self.workshopCreated = False
        self.open_output_windows = []

        self.ui.MainPages.setCurrentIndex(5)
        self.ui.SubPages.setCurrentIndex(0)
        self.ui.roomName.setText(self.room.getRoomName())
        self.ui.roomCode.setText(self.room.getRoomID() + ":")

        self.ui.roomChatBtn.clicked.connect(self.goToChat)
        self.ui.roomCallBtn.clicked.connect(self.goToCall)
        self.ui.roomWorkshopBtn.clicked.connect(self.goToWorkShop)
        self.ui.roomMemberBtn.clicked.connect(self.goToMember)
        self.ui.roomHomeBtn.clicked.connect(self.backToHome)
        self.ui.roomLeaveBtn.clicked.connect(self.leaveRoom)
        
        self.ui.workshopImportBtn.clicked.connect(self.handleImport)
        self.ui.workshopExportBtn.clicked.connect(self.handleExport)

        self.workshop_tool = Workshop()
        self.ui.chatSendTextConfirmBtn.clicked.connect(self.sendChatMessage)
        self.chat_timer = QTimer()
        self.chat_timer.timeout.connect(self.refreshChat)
        
        self.chat_timer.start(3000)

        self.ui.workshopRunBtn.clicked.connect(self.compile_code)



        # Room Background Color
        self.ui.FrameRoom.setStyleSheet(f"background-color: {RoomBackGroundColor};")
        self.ui.FrameRoomTopBar.setStyleSheet(f"background-color: {RoomTopBarColor};")
        self.ui.FrameRoomSectionBtnArea.setStyleSheet(f"background-color: {RoomSectionBtnAreaColor};")

        self.ui.FrameRoomSectionDisplayArea.setStyleSheet(f"background-color: {RoomSectionDisplayAreaColor};")

        # Section Colors if we wanna do it later



    def leaveRoom(self):
        leave_data = {
                "username": self.user.name,
                "roomID": self.room.getRoomID()
            }
        try:
            print(f"DEBUG: Leaving room {self.room.getRoomID()}")
            url = f"{self.room.server_url}/leave_room"
            response = requests.post(url, json=leave_data)
            if response.status_code == 200:
                self.room.leaveRoom()
                print("Successfully left the room on server.")
            else:
                print(f"Server error during leave: {response.text}")
        except Exception as e:
            print(f"Error leaving server: {e}")

        self.backToHome()
        self.room = None
        self.ui.MainPages.setCurrentIndex(2)

    def handleImport(self):
        if hasattr(self, 'work') and isValid(self.work.editor):
            try:
                self.workshop_tool.importCode(self.window, self.work.editor)
            except RuntimeError:
                    print("C++ object deleted during import.")
        else:
            print("Blocked: Editor no longer exists.")

    def handleExport(self):
        self.workshop_tool.exportCode(self.work.editor)

    def compile_code(self):
        CLIENT_ID = os.getenv("CLIENT_ID")
        CLIENT_SECRET = os.getenv("CLIENT_SECRET")
        
        code = self.work.getText()

        self.ui.workshopRunBtn.setEnabled(False)
        
        if hasattr(self, 'output_console'):
            self.output_console.setPlainText("Compiling code in the cloud... Please wait")

        self.compiler_thread = JDoodleCompilerThread(code, CLIENT_ID, CLIENT_SECRET)
        self.compiler_thread.compilation_finished.connect(self.display_code_output)
        self.compiler_thread.start()
        
    def display_code_output(self, result):
        if hasattr(self, 'output_console'):
            self.output_console.setPlainText(f"=== EXECUTION OUTPUT ===\n\n{result}")
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
            self.chat_timer.stop()
            return
            
        base_url = self.room.getServerURL()
        url = f"{base_url}/get_chat"
        
        # Start the background fetcher
        self.fetch_thread = ChatFetchThread(url, self.room.getRoomID())
        self.fetch_thread.chat_fetched.connect(self.updateChatUI)
        self.fetch_thread.start()

    def updateChatUI(self, messages):
        while self.chatLayout.count():
            item = self.chatLayout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
                
        for msg in messages:
            chat_text = f"<b>{msg['sender']}</b>: {msg['content']} <br><small style='color:gray'>{msg['time']}</small>"
            lbl = QLabel(chat_text)
            lbl.setWordWrap(True)
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

    def goToChat(self):
        self.ui.SubPages.setCurrentIndex(0)

    def goToCall(self):
        if not self.callCreated:
            self.callCreated = not self.callCreated
            self.videoWidget = VideoCallApp(self.user.name)
            self.ui.VLCall.addWidget(self.videoWidget,stretch=1)
        self.ui.SubPages.setCurrentIndex(1)

    def goToWorkShop(self):
        if not self.workshopCreated:
            self.workshopCreated = True
            
            self.work = CollabEditor(self.room.getRoomID())
            self.ui.VLWorkShop.addWidget(self.work, stretch=3) 

            self.output_console = QPlainTextEdit()
            self.output_console.setReadOnly(True)
            self.output_console.setMaximumHeight(150)
            self.output_console.setStyleSheet("""
                QPlainTextEdit {
                    background-color: #11111b; /* Slightly darker than editor */
                    color: #a6adc8;
                    font-family: 'Consolas', 'Monaco', monospace;
                    font-size: 13px;
                    border: 2px solid #313244;
                    border-radius: 8px;
                    padding: 6px;
                }
            """)
            self.output_console.setPlainText("Output console ready...")
            self.ui.VLWorkShop.addWidget(self.output_console, stretch=1)

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
                self.ui.listView.setEditTriggers(QListView.NoEditTriggers)
                self.ui.listView.setStyleSheet("font-size: 21px; font-weight: 600;")
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

        if hasattr(self, 'work') and self.work:
            self.ui.VLWorkShop.removeWidget(self.work)
            self.work.deleteLater()
            self.work = None

        if hasattr(self, 'output_console') and self.output_console:
            self.ui.VLWorkShop.removeWidget(self.output_console)
            self.output_console.deleteLater()
            self.output_console = None
            
        self.workshopCreated = False

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