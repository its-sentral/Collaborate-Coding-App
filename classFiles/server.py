import socketio
from fastapi import FastAPI
import uvicorn

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = FastAPI()
sio_app = socketio.ASGIApp(sio, app)

# --- STATE MANAGEMENT ---
# A set to keep track of all connected session IDs (sids).
# If you add usernames later, you can change this to a dictionary: {sid: "username"}
active_users = set()

async def broadcast_user_update():
    """Helper function to broadcast the current user list to the room"""
    await sio.emit('user_update', {
        'count': len(active_users),
        'users': list(active_users) # Sets aren't JSON serializable, so convert to list
    }, room="global_room")


@app.get("/")
def home():
    return "Relay Server Running"

@sio.event
async def connect(sid, environ):
    print(f"User Connected: {sid}")
    await sio.enter_room(sid, "global_room")
    
    # Add the new user to our tracking set and tell everyone
    active_users.add(sid)
    await broadcast_user_update()

@sio.event
async def disconnect(sid):
    print(f"User Disconnected: {sid}")
    
    # Remove the user from our tracking set and tell everyone
    active_users.discard(sid)
    await broadcast_user_update()

@sio.event
async def send_video(sid, data):
    # skip_sid=sid is CRITICAL: Don't send my video back to me
    await sio.emit('receive_video', data, room="global_room", skip_sid=sid)

@sio.event
async def send_audio(sid, data):
    # skip_sid=sid is CRITICAL: Prevents lethal feedback loops
    await sio.emit('receive_audio', data, room="global_room", skip_sid=sid)

if __name__ == "__main__":
    # Use loop='uvloop' for better performance on Linux servers
    uvicorn.run(sio_app, host="0.0.0.0", port=8000)