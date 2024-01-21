import os
import Filter

class FilterList():
    filterList = {}

    def __init__ (self):
        self._filterList = {
            "personal": [],
            "academic": []
        }

    def add(self, filter, personal):
        tempList = []
        alreadyInList = False
        if personal == True:
            tempList = self._filterList.get("personal")
            
            for i in tempList:
                if i.getName() == filter.getName():
                    alreadyInList = True

            if alreadyInList == False:
                tempList.append(filter)
                self._filterList.update({"personal": tempList})
        else:
            tempList = self._filterList.get("academic")
            
            for i in tempList:
                if i.getName() == filter.getName() and i.getCourseNumber() == filter.getCourseNumber():
                    alreadyInList = True
            
            if alreadyInList == False:
                tempList.append(filter)
                self._filterList.update({"academic": tempList})
    
    def remove(self, filter, personal):
        tempList = []
        if personal == True:
            tempList = self._filterList.get("personal")

            for i in tempList:
                if i.getName() == filter.getName():
                    tempList.remove(i)
            
            self._filterList.update({"personal": tempList})

        else:
            tempList = self._filterList.get("academic")

            for i in tempList:
                if i.getName() == filter.getName() and i.getCourseNumber() == filter.getCourseNumber():
                    tempList.remove(i)
            
            self._filterList.update({"academic": tempList})




            



