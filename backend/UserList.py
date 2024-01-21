import os
import User

class UserList():
    userList = []
    def __init__(self, userList):
        self._userList = userList
    
    def add(self, user):
        inList = False
        for i in self._userList:
            if i.getID == user.getID:
                inList = True
        if inList == False:
            self._userList.append(user)

    def remove(self, user):
        for i in self._userList:
            if i.getID == user.getID:
                self._userList.remove(i)

    def getUserList(self):
        return self._userList

        