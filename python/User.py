import os
import FilterList

#setting up the different variables that make up an user: name, age, filters, aboutMe, extraInformation
name = ""
age = 0
filters = FilterList()
#placeholder variable for the about me section: 
aboutMe = "" 
#placeholder variable for the extra information: 
extraInformation = ""
#placeholder variable to store the list of pictures to be added in the front end

class User():
    def __init__(self, name, age, filters, aboutMe, extraInformation):
        self._name = name
        self._age = age
        self._filters = filters
        self._aboutMe = aboutMe
        self._extraInformation = extraInformation

    def setName(self, name):
        self._name = name
    
    def setAge(self, age):
        self._age = age

    def setAboutMe
