from RoomClass import Room
import ZODB

class User(object):
    def __init__(self,gmail,name,id,pno):
        self.gmail = gmail
        self.name = name
        self.id = id
        self.phone = pno

    def createRoom(self):
        pass

    def getGmail(self):
        return self.gmail

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getPhoneNo(self):
        return self.phone

    def joinRoom(self):
        pass

    def login(self):
        pass

    def register(self):
        pass

    def setName(self):
        pass

    def setPhoneNumber(self):
        pass

class Member(User):
    def __init__(self, gmail, name, id, pno, memOf=list([])):
        User.__init__(self,gmail, name, id, pno)
        self.room : list = memOf

    def editCode(self):
        pass

    def exportCode(self):
        pass

    def importCode(self):
        pass

    def joinCall(self):
        pass

    def leaveCall(self):
        pass

    def leaveRoom(self, RID : int):
        self.room.remove(RID)

    def sendText(self):
        pass

    def startCall(self):
        pass

class Admin(Member):
    def __init__(self, gmail, name, id, pno, roomOwn : Room, memOf=[]):
        Member.__init__(self,gmail,name,id,pno,memOf)
        self.roomOwn = roomOwn

    def deleteRoom(self):
        del self.roomOwn