from include.classImport import *
from include.lib import *

from persistent import Persistent
class Room(object):
    def __init__(self, Rname, RID : str, admin: 'Admin', mem=[]):
        self.WorkSys = Workshop()
        self.ChatSys = Chat()
        self.roomName = Rname
        self.roomID = RID
        self.member = mem 
        self.admin = admin

    def removeMember(self,name:str):
        for i in self.member:
            if i.getName() == name:
                i.leaveRoom(self.roomID)
                break

    def removeMember(self,id:int):
        for i in self.member:
            if i.getName() == id:
                i.leaveRoom(self.roomID)
                break

    def textSent(self,text,sender):
        self.ChatSys.addConversation(text,sender)

class Call(object):
    def __init__(self):
        self.startTime = datetime.now()
        self.endTime = None

    def endCall(self):
        self.endTime = datetime.now()

    def getStartTime(self):
        return self.startTime
    
    def getEndTime(self):
        return self.endTime
    
class Workshop(object):
    def __init__(self):
        pass

    def importCode(self,file):
        pass

    def exportCode(self):
        pass

class Conversation(object):
    def __init__(self,content,sender):
        self.content = content
        self.sender = sender
        self.time = datetime.now()

    def getDetail(self):
        return (self.time,self.sender,self.content)

class Chat(object):
    def __init__(self):
        self.history = []

    def addConversation(self,content,sender):
        Convo = Conversation(content,sender)
        self.history.append(Convo)

    def getChatHistory(self):
        return self.history