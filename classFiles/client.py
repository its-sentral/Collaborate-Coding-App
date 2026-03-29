import sys
import cv2
import base64
import pyaudio
import socketio
import threading
import queue
import numpy as np
from PySide6.QtCore import QTimer, Signal, QObject, Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QSizePolicy
import time

# --- CONFIGURATION ---
SERVER_URL = "https://ccp-servertest.onrender.com" 


# Lowered for better performance over internet
RATE = 16000 
CHUNK = 1024 

class NetworkSignals(QObject):
    update_video = Signal(str)
    update_user_count = Signal(int)
    update_status = Signal(str)

class VideoCallApp(QWidget):
    def __init__(self):
        super().__init__()
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
        layout.addWidget(self.status_label,stretch=1)

        self.currentUser = QLabel()
        self.currentUser.setText("Waiting to join")
        self.currentUser.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.currentUser,stretch=1)

        self.is_muted = False
        self.btn_mute = QPushButton("Mute Microphone")
        self.btn_mute.clicked.connect(self.toggle_mute)
        self.btn_mute.setEnabled(False)
        layout.addWidget(self.btn_mute, stretch=1)
        
        # self.remote_video_label = QLabel("Waiting for video...")
        # self.remote_video_label.setAlignment(Qt.AlignCenter)
        # self.remote_video_label.setStyleSheet("background: black; color: white;")
        # self.remote_video_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # layout.addWidget(self.remote_video_label,stretch=1)
        
        self.btn_connect = QPushButton("Join Room")
        self.btn_connect.clicked.connect(self.start_connection)
        layout.addWidget(self.btn_connect,stretch=1)

        self.btn_leave = QPushButton("Leave Call")
        self.btn_leave.clicked.connect(self.leave_call)
        self.btn_leave.setEnabled(False)
        layout.addWidget(self.btn_leave, stretch=1)

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
        self.signals.update_user_count.connect(self.update_user_label)
        self.signals.update_status.connect(self.update_status_label)

        # --- EVENT HANDLERS ---
        @self.sio.on('connect')
        def on_connect():
            print("✅ CONNECTED")
            # Emit a signal instead of touching the UI directly
            self.signals.update_status.emit("Status: Connected!")
            
            # Now tell the server we are ready to join and be counted!
            self.sio.emit('join_room', "global_room")

        @self.sio.on('user_update')
        def on_user_update(data):
            count = data['count']
            self.currentUser.setText(f"Users in call: {count}")

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

    def toggle_mute(self):
        # Flip the boolean (True becomes False, False becomes True)
        self.is_muted = not self.is_muted 
        
        if self.is_muted:
            self.btn_mute.setText("Unmute Microphone")
            self.btn_mute.setStyleSheet("background-color: #ff4444; color: white; font-weight: bold;")
        else:
            self.btn_mute.setText("Mute Microphone")
            self.btn_mute.setStyleSheet("")

    def start_connection(self):
        if self.is_running: return
        try:
            self.sio.connect(SERVER_URL, wait_timeout=20) 
            self.is_running = True
            
            QTimer.singleShot(100, self.send_video_loop) 
            threading.Thread(target=self.send_audio_loop, daemon=True).start()
            threading.Thread(target=self.audio_playback_worker, daemon=True).start()
            
            # --- UPDATE YOUR BUTTON STATES HERE ---
            self.btn_connect.setEnabled(False)
            self.btn_leave.setEnabled(True)
            self.btn_mute.setEnabled(True) # If you added the mute button!
            
        except Exception as e:
            print(f"❌ Connection Failed: {e}")

    def leave_call(self):
        print("Leaving call...")
        
        self.is_running = False 
        
        if self.sio.connected:
            self.sio.emit('manual_leave')
            time.sleep(0.5) 
            self.sio.disconnect()
            
        self.btn_connect.setEnabled(True)
        self.btn_leave.setEnabled(False)
        
        if hasattr(self, 'btn_mute'):
            self.btn_mute.setEnabled(False)
            self.is_muted = False
            self.btn_mute.setText("Mute Microphone")
            self.btn_mute.setStyleSheet("")
            
        self.signals.update_status.emit("Status: Idle")
        self.signals.update_user_count.emit(0)
        self.currentUser.setText("Waiting to join")
        

    def update_user_label(self, count):
        self.currentUser.setText(f"Participants: {count}")

    def update_status_label(self, status_text):
        self.status_label.setText(status_text)

    def audio_playback_worker(self):
        print("🔊 Playback Worker Active")
        while self.is_running:
            # If the queue gets too big (backlog), skip ahead to reduce delay
            if self.audio_queue.qsize() > 10:
                while self.audio_queue.qsize() > 2:
                    self.audio_queue.get() # Toss old audio to catch up
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
    w = VideoCallApp()
    w.show()
    sys.exit(app.exec())