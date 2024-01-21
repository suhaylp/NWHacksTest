import os

class Filter():
    filterName = ""
    def __init__ (self, filterName):
        self._filterName = filterName
    
    def getName(self):
        return self._filterName

class AcademicFilter(Filter):
    courseNumber = ""
    def __init__ (self, filterName, courseNumber):
        super().__init__(filterName)
        self._courseNumber = courseNumber
    
    def getCourseNumber(self):
        return self._courseNumber
    
class PersonalFilter(Filter):
    def __init__(self, filterName):
        super().__init__(filterName)