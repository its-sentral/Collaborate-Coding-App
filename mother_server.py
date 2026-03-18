from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ZODB, ZODB.FileStorage
import transaction
from BTrees.OOBTree import OOBTree

app = FastAPI()

# 1. Open the local ZODB database file
storage = ZODB.FileStorage.FileStorage('database.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

# 2. Create the "users" dictionary if it doesn't exist yet
if not hasattr(root, 'users'):
    root.users = OOBTree()
    transaction.commit()

# 3. Define what data we expect from the UI
class UserData(BaseModel):
    username: str
    password: str

# --- ENDPOINT 1: REGISTER ---
@app.post("/register")
def register(user: UserData):
    # Check if username is taken
    if user.username in root.users:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Save the new user and password to ZODB
    root.users[user.username] = {"password": user.password}
    transaction.commit() # ALWAYS commit when saving new data!
    
    print(f"Server: Registered new user '{user.username}'")
    return {"status": "success"}

# --- ENDPOINT 2: LOGIN ---
@app.post("/login")
def login(user: UserData):
    # Check if the user exists
    if user.username not in root.users:
        raise HTTPException(status_code=401, detail="User not found")
    
    # Check if the password matches
    if root.users[user.username]["password"] != user.password:
        raise HTTPException(status_code=401, detail="Incorrect password")
    
    print(f"Server: '{user.username}' logged in successfully.")
    return {"status": "success"}