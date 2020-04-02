#Professor Class
#Authored By Zachery Fogg

#Imports
import Course
#Class Declaration
class Professor:

    #Constructor
    def __init__(self,name,office,tenure,rating,courseList):
        #Default Value
        self.defaultName = "Gener IcnAme"
        self.defaultOffice ="Building 101"
        self.defaultTenure = False
        self.defaultRating = 0.0
        self.courseList=[]
        #User Input values
        self.setName(name)
        self.setOffice(office)
        self.setTenure(tenure)
        self.setRating(rating)
        self.setCourseList(courseList)
    #Method to print Professor Object
    def printProfessor(self):
        print("Name: "+ self.name)
        print("Office: "+ self.office)
        print("Tenure: "+ str(self.tenure))
        print("Rating: "+ str(self.rating))
        self.printCourseList()
    #Method to print Course List
    def printCourseList(self):
        if(len(self.courseList)==0):
            print(self.name + " does not currently teach any courses\n")
            return
        print(self.name + " currently teaches the following courses:")
        for i in range(len(self.courseList)):
            print(self.courseList[i].getCourseTitle() + ",",end=" ")
        print("\n\n")
    #setName accepts string of 0<length
    def setName(self,name):
        if(len(name)>0):
            self.name = name;
        else:
            print("Name length cannot be 0")
            print("Name set to default: " + self.defaultName)
            self.name=self.defaultName
    #setOffice accepts a string of 0<length
    def	setOffice(self,office):
        if(len(office)>0):
            self.office = office;
        else:
            print("Office name length cannot be 0")
            print("Office set to default: " + self.defaultOffice)
            self.office=self.defaultOffice
    #setTenure will accept a boolean value or (0,1)
    def setTenure(self,tenure):
        if(tenure==False or tenure == True):
            self.tenure=tenure
        else:
            print("Invalid tenure input. Input must be boolean, 0, or 1")
            print("Tenure has been set to "+ str(self.defaultTenure))
            self.tenure=self.defaultTenure
    #setRating will accept a double or integer 0-5
    def setRating(self,rating):
        if(rating>=0 and rating<=5):
            self.rating = rating
        else:
            self.rating = self.defaultRating
            print("Rating must be a value of 0-5")
            print("Rating has been set to default value of: " + str(self.defaultRating))
    #setCourseList, sets to new list defined by user, validates using addCourse method
    def setCourseList(self,courseList):
        self.courseList=[]
        for i in range(len(courseList)):
            self.addCourse(courseList[i])
    #addCourse, adds course to list, validates courses of duplicate names are not added
    def addCourse(self,course):
        if(self.findCourse(course.getCourseTitle())==-1):
            self.courseList.append(course)
        else:
            print("Professor "+ self.name +" already teaches a course ")
            print("with the name "+ course.getCourseTitle() + " and therefore ")
            print("it will not be added to the list or courses")
    #findCourse, returns index of course, or -1 if a course by that name DNE
    def findCourse(self,courseName):
        if(len(self.courseList)==0):
            return -1
        for i in range(len(self.courseList)):
            if (self.courseList[i].getCourseTitle() == courseName):
                return i
        #print("The Course: " + courseName + " was not found")
        return -1
    #getCourse returns the course if in list, or the first course in list if not
    #getCourse takes an index as argument
    def getCourse(self,courseName):
        index = self.findCourse(courseName)
        if(index>=0 and index<len(self.courseList)):
            return self.courseList[index]
        else:
            print("The course at index 0 will be returned instead")
            return self.courseList[0]
    #delCourse method, deletes course with given name
    def delCourse(self,courseName):
        index = self.findCourse(courseName)
        if(index != -1):
            self.courseList.pop(index)
            print("The Course: " + courseName + " was deleted")
        else:
            print("The Course: " + courseName + " was not found or deleted")
    #getOffice returns string
    def getOffice(self):
        return self.office
    #getTenure returns bool
    def getTenure(self):
        return self.tenure
    #getProfName returns string
    def getProfName(self):
        return self.name
    #getRating returns double
    def getRating(self):
        return self.rating
    def getCourseList(self):
        return self.courseList
