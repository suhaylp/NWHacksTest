import os
import User

userList = []

class UserList()    :
    def __init__(self, userList):
        self._userList = userList
    
    def add(self, user):
        i
        for i in userList:
            if i.getID == user.getID:
                inList = True
        self._userList.append(user)

    def remove(self, user):
        for i in userList:
            if i.getID == user.getID:
                self._userList.remove(i)

        