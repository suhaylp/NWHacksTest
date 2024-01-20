import os
import FilterList

#setting up the different variables that make up an user: id, name, age, filters, aboutMe, extraInformation and list of pictures
id = 0
name = ""
age = 0
filters = FilterList()
#placeholder variable for the about me section: 
aboutMe = "" 
#placeholder variable for the extra information: 
extraInformation = ""
#placeholder variable to store the list of pictures to be added in the front end

#the user class with the respective getter and setter methods for most of the variables
class User():
    def __init__(self, id, name, age, filters, aboutMe, extraInformation):
        self._id = id
        self._name = name
        self._age = age
        self._filters = filters
        self._aboutMe = aboutMe
        self._extraInformation = extraInformation

    def setName(self, name):
        self._name = name
    
    def setAge(self, age):
        self._age = age

    def setAboutMe(self, aboutMe):
        self._aboutMe = aboutMe

    def setExtraInformation(self, extraInformation):
        self._extraInformation = extraInformation

    #no setter method for the id because we don't want the id to be modifiable once the user has been created 
    #function to set the list of pictures to be added in the front end

    def getID(self):
        return self._id

    def getName(self):
        return self._name

    def getAge(self):
        return self._age
    
    def getAboutMe(self):
        return self._aboutMe

    def getExtraInformation(self):
        return self._extraInformation

    #function to return the list of pictures to be set up in the front end
