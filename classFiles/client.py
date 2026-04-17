import sys,cv2,base64,pyaudio,socketio,threading,queue,time
import numpy as np
from PySide6.QtCore import QTimer, Signal, QObject, Qt, QSize, QThread
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QListWidget

SERVER_URL = "https://ccp-servertest.onrender.com" 

RATE = 16000 
CHUNK = 1024 

class NetworkSignals(QObject):
    update_video = Signal(str)
    update_user_list = Signal(list)
    update_status = Signal(str)

class ConnectThread(QThread):
    connection_result = Signal(bool, str)
    
    def __init__(self, sio, url, parent=None):
        super().__init__(parent)
        self.sio = sio
        self.url = url
        
    def run(self):
        try:
            self.sio.connect(self.url, wait_timeout=20)
            self.connection_result.emit(True, "Connected")
        except Exception as e:
            self.connection_result.emit(False, str(e))

class VideoCallApp(QWidget):
    def __init__(self,user_name):
        super().__init__()
        self.name = user_name
        self.resize(600, 500)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setMinimumHeight(350)
        self.setMinimumWidth(400)
        self.setMaximumHeight(16777215)
        self.setMaximumWidth(16777215)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.status_label = QLabel("Status: Idle")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label, stretch=1)

        self.user_list_widget = QListWidget()
        self.user_list_widget.addItem("Waiting to join...")
        self.user_list_widget.setStyleSheet("""
            QListWidget {
                background-color: #1e1e1e;
                color: #d4d4d4;
                border: 1px solid #333333;
                border-radius: 4px;
                padding: 5px;
                font-size: 14px;
            }
        """)
        layout.addWidget(self.user_list_widget, stretch=2)

        button_layout = QHBoxLayout() 
        button_layout.addStretch() 
        
        self.btn_toggle_call = QPushButton("Join Room")
        self.btn_toggle_call.setMinimumSize(QSize(80, 60)) 
        self.btn_toggle_call.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.btn_toggle_call.clicked.connect(self.handle_call_toggle)
        button_layout.addWidget(self.btn_toggle_call)

        self.is_muted = False
        self.btn_mute = QPushButton("Mute Mic") 
        self.btn_mute.setMinimumSize(QSize(80, 60))
        self.btn_mute.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.btn_mute.clicked.connect(self.toggle_mute)
        self.btn_mute.setEnabled(False)
        button_layout.addWidget(self.btn_mute)

        button_layout.addStretch()

        layout.addLayout(button_layout) 
        self.setLayout(layout)

        # --- AUDIO BUFFERING SETUP ---
        self.audio_queue = queue.Queue()
        self.buffer_threshold = 5  # "Bucket" size to prevent gaps

        # Network
        self.sio = socketio.Client(
            reconnection_delay=1, 
            reconnection_delay_max=5,
            logger=False, 
            engineio_logger=False
        )
        self.signals = NetworkSignals()
        self.signals.update_video.connect(self.display_remote_frame)
        self.signals.update_user_list.connect(self.update_user_list_ui)
        self.signals.update_status.connect(self.update_status_label)

        # --- EVENT HANDLERS ---
        @self.sio.on('connect')
        def on_connect():
            print("✅ CONNECTED")
            self.signals.update_status.emit("Status: Connected!")
            self.sio.emit('join_room', {'room': 'global_room', 'username': self.name})

        @self.sio.on('user_update')
        def on_user_update(data):
            user_list = data.get('users', [])
            self.signals.update_user_list.emit(user_list)

        @self.sio.on('receive_video')
        def on_video(data):
            self.signals.update_video.emit(data['image'])

        @self.sio.on('receive_audio')
        def on_audio(data):
            try:
                # If the server is relaying bytes, data['audio'] is already decoded
                raw_audio = data['audio']
                self.audio_queue.put(raw_audio)
            except:
                pass

        # Audio Devices
        self.p = pyaudio.PyAudio()
        try:
            self.mic = self.p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)
            self.spk = self.p.open(format=pyaudio.paInt16, channels=1, rate=RATE, output=True, frames_per_buffer=CHUNK)
            print(f"🎤 Audio OK ({RATE}Hz)")
        except Exception as e:
            print(f"❌ Audio Error: {e}")

        self.cap = cv2.VideoCapture(0)
        self.is_running = False

    def handle_call_toggle(self):
        if self.is_running:
            self.leave_call()
        else:
            self.start_connection()

    def toggle_mute(self):
        self.is_muted = not self.is_muted 
        if self.is_muted:
            self.btn_mute.setText("Unmute Microphone")
            self.btn_mute.setStyleSheet("background-color: #ff4444; color: white; font-weight: bold;")
        else:
            self.btn_mute.setText("Mute Microphone")
            self.btn_mute.setStyleSheet("")

    def start_connection(self):
        if self.is_running: return
        
        self.btn_toggle_call.setText("Connecting...")
        self.btn_toggle_call.setEnabled(False)
        
        self.connect_thread = ConnectThread(self.sio, SERVER_URL)
        self.connect_thread.connection_result.connect(self.on_connection_finished)
        self.connect_thread.start()

    def on_connection_finished(self, success, message):
        self.btn_toggle_call.setEnabled(True)
        
        if success:
            self.is_running = True
            QTimer.singleShot(100, self.send_video_loop) 
            threading.Thread(target=self.send_audio_loop, daemon=True).start()
            threading.Thread(target=self.audio_playback_worker, daemon=True).start()
            self.btn_toggle_call.setText("Leave Call")
            self.btn_toggle_call.setStyleSheet("background-color: #ff4444; color: white; font-weight: bold;")
            self.btn_mute.setEnabled(True)
        else:
            print(f"❌ Connection Failed: {message}")
            self.btn_toggle_call.setText("Join Room")

    def leave_call(self):
        print("Leaving call...")
        self.is_running = False 
        
        self.btn_toggle_call.setText("Join Room")
        self.btn_toggle_call.setStyleSheet("")
        
        if hasattr(self, 'btn_mute'):
            self.btn_mute.setEnabled(False)
            self.is_muted = False
            self.btn_mute.setText("Mute Mic")
            self.btn_mute.setStyleSheet("")

        self.signals.update_status.emit("Status: Idle")
        self.signals.update_user_list.emit([])

        if self.sio.connected:
            def background_disconnect(sio_instance):
                try:
                    sio_instance.emit('manual_leave')
                    time.sleep(0.5)
                    sio_instance.disconnect()
                    print("✅ Disconnected in background.")
                except Exception as e:
                    pass

            threading.Thread(target=background_disconnect, args=(self.sio,), daemon=True).start()

    def update_user_list_ui(self, users):
        self.user_list_widget.clear()
        
        if not users:
            self.user_list_widget.addItem("Waiting to join...")
        else:
            for user in users:
                self.user_list_widget.addItem(f"👤 {user}")

    def update_status_label(self, status_text):
        self.status_label.setText(status_text)

    def audio_playback_worker(self):
        print("🔊 Playback Worker Active")
        while self.is_running:
            if self.audio_queue.qsize() > 10:
                while self.audio_queue.qsize() > 2:
                    self.audio_queue.get()
                print("🚀 Delay detected: Skipping to real-time")

            if self.audio_queue.qsize() < self.buffer_threshold:
                time.sleep(0.01) # Breathe
                continue 
            try:
                chunk = self.audio_queue.get_nowait()
                self.spk.write(chunk)
            except:
                time.sleep(0.01)

    def send_video_loop(self):
        pass

    def send_audio_loop(self):
        while self.is_running:
            try:
                data = self.mic.read(CHUNK, exception_on_overflow=False)
                if self.sio.connected and not self.is_muted:
                    self.sio.emit('send_audio', {'room': "global_room", 'audio': data})
            except:
                break

    def display_remote_frame(self, b64_image):
        try:
            data = base64.b64decode(b64_image)
            np_arr = np.frombuffer(data, np.uint8)
            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            if frame is not None:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame.shape
                qimg = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)
                self.remote_video_label.setPixmap(QPixmap.fromImage(qimg).scaled(640, 480, Qt.KeepAspectRatio))
        except:
            pass

    def closeEvent(self, event):
        self.is_running = False
        self.sio.disconnect()
        self.cap.release()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = VideoCallApp('Jeff')
    w.show()
    sys.exit(app.exec())