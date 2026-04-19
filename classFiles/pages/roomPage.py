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
import random

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

        if not hasattr(self.ui, 'admin_panel_created'):
            self.admin_panel = QWidget()
            admin_layout = QHBoxLayout(self.admin_panel)
            admin_layout.setContentsMargins(0, 0, 0, 0)
            
            self.btn_transfer_host = QPushButton("Transfer Host")
            self.btn_kick_member = QPushButton("Kick Member")
            
            self.btn_transfer_host.setStyleSheet("background-color: #f39c12; color: white; font-weight: bold; padding: 8px;")
            self.btn_kick_member.setStyleSheet("background-color: #e74c3c; color: white; font-weight: bold; padding: 8px;")
            
            admin_layout.addWidget(self.btn_transfer_host)
            admin_layout.addWidget(self.btn_kick_member)
            self.ui.listView.parentWidget().layout().addWidget(self.admin_panel)
            
            self.ui.admin_panel_widget = self.admin_panel
            self.ui.btn_transfer = self.btn_transfer_host
            self.ui.btn_kick = self.btn_kick_member
            self.ui.admin_panel_created = True
        
        self.admin_panel = self.ui.admin_panel_widget
        self.btn_transfer_host = self.ui.btn_transfer
        self.btn_kick_member = self.ui.btn_kick

        self.admin_panel.setVisible(False)
        self.btn_transfer_host.setEnabled(False)
        self.btn_kick_member.setEnabled(False)

        if self.ui.listView.selectionModel() is not None:
            try:
                self.ui.listView.selectionModel().selectionChanged.disconnect()
            except Exception:
                pass

        # self.ui.listView.selectionModel().selectionChanged.connect(self.on_member_selected)
        self.btn_transfer_host.clicked.connect(lambda: self.execute_admin_action("transfer_host"))
        self.btn_kick_member.clicked.connect(lambda: self.execute_admin_action("kick_member"))

        self.kick_timer = QTimer(self)
        self.kick_timer.timeout.connect(self.checkIfKicked)
        self.kick_timer.start(3000)

    def leaveRoom(self):
        is_admin = (self.user.name == self.room.getAdmin().getName())
        room_id = self.room.getRoomID()
        base_url = self.room.getServerURL().rstrip('/')

        if is_admin:
            try:
                response = requests.get(f"{base_url}/get_members?roomID={room_id}", timeout=5)
                
                if response.status_code == 200:
                    members = response.json().get("members", [])
                    
                    other_members = [m for m in members if m != self.user.name]
                    
                    if other_members:
                        new_host = random.choice(other_members)
                        print(f"DEBUG: Auto-transferring host to {new_host}")
                        
                        transfer_payload = {
                            "roomID": room_id,
                            "admin": self.user.name,
                            "target": new_host
                        }
                        requests.post(f"{base_url}/transfer_host", json=transfer_payload, timeout=5)
                        
            except Exception as e:
                print(f"Error during auto-host transfer: {e}")

        leave_data = {
            "username": self.user.name,
            "roomID": room_id
        }
        
        try:
            print(f"DEBUG: Leaving room {room_id}")
            response = requests.post(f"{base_url}/leave_room", json=leave_data, timeout=5)
            
            if response.status_code == 200:
                self.room.leaveRoom()
                print("Successfully left the room.")
        except Exception as e:
            print(f"Error leaving server: {e}")

        self.backToHome()
        self.room = None
        
        if hasattr(self, 'kick_timer'):
            self.kick_timer.stop()
            
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
        
        is_admin = self.user.name == self.room.getAdmin().getName()
        self.admin_panel.setVisible(is_admin)

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
                
                self.ui.listView.selectionModel().selectionChanged.connect(self.on_member_selected)
            else:
                print("Failed to fetch members from server")
        except Exception as e:
            print(f"Error updating member list: {e}")

    def on_member_selected(self, selected, deselected):
        indexes = self.ui.listView.selectedIndexes()
        if not indexes:
            self.btn_transfer_host.setEnabled(False)
            self.btn_kick_member.setEnabled(False)
            return

        selected_text = indexes[0].data()
        target_username = selected_text[2:] 

        if target_username == self.user.name:
            self.btn_transfer_host.setEnabled(False)
            self.btn_kick_member.setEnabled(False)
        else:
            self.btn_transfer_host.setEnabled(True)
            self.btn_kick_member.setEnabled(True)

    def execute_admin_action(self, endpoint):
        indexes = self.ui.listView.selectedIndexes()
        if not indexes: return
        
        target_username = indexes[0].data()[2:]
        
        payload = {
            "roomID": self.room.getRoomID(),
            "admin": self.user.name,
            "target": target_username
        }

        self.btn_transfer_host.setEnabled(False)
        self.btn_kick_member.setEnabled(False)
        self.btn_transfer_host.setText("Processing...")

        roomUrl = self.room.getServerURL().rstrip('/')
        url = f"{roomUrl}/{endpoint}"
        self.admin_thread = AdminActionThread(url, payload)
        
        self.admin_thread.action_finished.connect(
            lambda success, msg: self.on_admin_action_finished(success, msg, endpoint, target_username)
        )
        self.admin_thread.start()

    def on_admin_action_finished(self, success, message, endpoint, target_username):
        self.btn_transfer_host.setText("Transfer Host")
        
        if success:
            print(f"Admin action successful: {message}")
            
            if endpoint == "transfer_host":
                self.room.getAdmin().name = target_username
                self.admin_panel.setVisible(False)
                
            self.goToMember()
        else:
            print(f"Admin action failed: {message}")
    
    def backToHome(self):
        if hasattr(self, 'kick_timer'):
            self.kick_timer.stop()
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
            self.btn_transfer_host.clicked.disconnect()
            self.btn_kick_member.clicked.disconnect()
        except Exception:
            pass 

        self.ui.MainPages.setCurrentIndex(2)

    def checkIfKicked(self):
        if self.room is None or self.user is None:
            return
        
        url = f"{self.room.getServerURL().rstrip('/')}/room_info"
        self.kick_thread = RoomSyncThread(url, self.user.name)
        self.kick_thread.kicked_signal.connect(self.handle_kicked)
        self.kick_thread.admin_update_signal.connect(self.handle_admin_update) 
        
        self.kick_thread.start()

    def handle_admin_update(self, current_admin):
        if self.room and self.room.getAdmin().getName() != current_admin:
            print(f"Host transfer detected! New host is: {current_admin}")
            
            self.room.getAdmin().name = current_admin
            is_admin = (self.user.name == current_admin)
            self.admin_panel.setVisible(is_admin)
            
            if self.ui.SubPages.currentIndex() == 3:
                self.goToMember()

    def handle_kicked(self):
        self.kick_timer.stop()
        if hasattr(self, 'chat_timer'):
            self.chat_timer.stop()
            
        try:
            if self.room:
                self.room.leaveRoom() 
        except Exception as e:
            print(f"Error removing room locally: {e}")

        self.backToHome()
        self.room = None
        
        QMessageBox.warning(self.window, "Disconnected", "You have been kicked from the room by the Admin.")
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
            
            response = requests.post(url, json=payload, timeout=15) 
            
            print(f"[Thread] 3. Got response! Status Code: {response.status_code}")
            
            try:
                response_data = response.json()
            except Exception:
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

class AdminActionThread(QThread):
    action_finished = Signal(bool, str)
    def __init__(self, url, payload, parent=None):
        super().__init__(parent)
        self.url = url
        self.payload = payload
        print(url)

    def run(self):
        try:
            res = requests.post(self.url, json=self.payload, timeout=5)
            if res.status_code == 200:
                self.action_finished.emit(True, "Action successful")
            else:
                self.action_finished.emit(False, f"Server Error: {res.text}")
        except Exception as e:
            self.action_finished.emit(False, f"Connection Error: {e}")

class RoomSyncThread(QThread):
    kicked_signal = Signal()
    admin_update_signal = Signal(str)

    def __init__(self, url, username, parent=None):
        super().__init__(parent)
        self.url = url
        self.username = username

    def run(self):
        try:
            res = requests.get(self.url, params={"username": self.username}, timeout=3)
            if res.status_code == 200:
                data = res.json()
                
                if data.get("status") == "access_denied":
                    self.kicked_signal.emit()
                elif "admin_name" in data:
                    self.admin_update_signal.emit(data["admin_name"])
        except Exception as e:
            pass
    