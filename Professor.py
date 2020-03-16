#Professor Class

#Imports
import Course.py
#Class Declaration
class Professor:

    #Constructor
    def __init__(self,name,office,tenure,rating,courseList):
        #Default Value
        self.defaultName = "Generic Name"
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
    #setName accepts string of 0<length<=50
    def setName(self,name):
        if(len(name)>0 and len(name)<=50):
            self.name = name;
        else:
            print("Name length cannot be 0 or exceed 50")
            print("Name set to default: " + self.defaultName)
            self.name=defaultName
    #setOffice accepts a string of 0<length<=50
    def	setOffice(self,office):
        if(len(office)>0 and len(office)<=50):
            self.office = office;
        else:
            print("Office name length cannot be 0 or exceed 50")
            print("Office set to default: " + self.defaultOffice)
            self.office=defaultOffice
    #setTenure will accept a boolean value or (0,1)
    def setTenure(self,tenure):
        if(tenure==0):
            tenure=False
        elif(tenure==1):
            tenure==True
        elif(type(tenure)==bool):
            self.tenure=tenure
        else:
            print("Invalid tenure input. Input must be boolean, 0, or 1")
            print("Tenure has been set to "+ self.defaultTenure)
            self.tenure=tenure
    #setRating will accept a double or integer 0-5
    def setRating(self,rating):
        if(rating>=0 and rating<=5):
            self.rating = rating
        else:
            print("Rating must be a value of 0-5")
            print("Rating has been set to default value of: " + self.defaultRating)
    #setCourseList, sets to new list defined by user, validates using addCourse method
    def setCourseList(self,courseList):
        self.courseList=[]
        for i in range(len(courseList)):
            self.addCourse(courseList[i])
    #addCourse, adds course to list, validates courses of duplicate names are not added
    def addCourse(self,course):
        if(self.findCourse(course.getCourseTitle())==-1)
            courseList.append(course)
        else:
            print("Professor "+ self.name +" already teaches a course ")
            print("with the name "+ course.getCourseTitle() + " and therefore ")
            print("it will not be added to the list or courses")
    #findCourse, returns index of course, or -1 if a course by that name DNE
    def findCourse(self,courseName):
        for i in range(len(self.courseList)):
            if (self.courseList[i].getCourseTitle() == courseName):
                return i
            else:
                print("The Course: " courseName + " was not found")
                return -1
    #getCourse returns the course if in list, or the first course in list if not
    #getCourse takes an index as argument
    def getCourse(self,courseName):
        if(index>=0 and index<len(courseList)):
            return courseList[index]
        else:
            print("The course at index 0 will be returned instead")
            return courseList[0]
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
        return office
    #getTenure returns bool
    def getTenure(self):
        return tenure
    #getProfName returns string
    def getProfName(self):
        return name
    #getRating returns double
    def getRating(self):
        return rating
