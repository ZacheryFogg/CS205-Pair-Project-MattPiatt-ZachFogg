#College Class

#Imports
import Professor.py
#Class Declaration
class College:

    #Constructor will initialize collegeName,enrollment
    def __init__(self,collegeName, collegeEnrollment, majorList,profList):
        #Default Values Initialized
        self.defaultCollegeName = "College of Education"
        self.defaultEnrollemnt = 0
        self.majorList=[]
        self.profList=[]
        #User Input values
        self.setCollegeName(collegeName)
        self.setCollegeEnrollment(collegeEnrollment)
        self.setMajorList(majorList)
        self.setProfList(profList)

    #printCollege method will print the out a representation of the college
    def printCollge(self):
        print(self.collegeName)
        print("Enrollment: " + self.collegeEnrollment)
        self.printMajors()
        self.printProfessors()
    #printMajors will print a list of the majors within the college
    def printMajors(self):
        print("List of Majors that exist within " + self.collegeName)
        print(self.majorList)
    #printProfessors will print a list of the professors within the college
    def printProfessors(self):
        print("List of Professors that exist withing " + self.collegeName)
        print(self.profList)

    #Standard Setters
    #setCollegeEnrollment will validate that value is 0<=enrollment<1000000
    def setCollegeEnrollment(self,collegeEnrollment):
        if(collegeEnrollment>=0 and collegeEnrollment<1000000):
            self.collegeEnrollment = collegeEnrollment
        else:
            print("College enrollment value is invalid. Must be 0<= Enrollment < 1000000")
            print("College enrollment has been set to a defualt value of: " + self.defaultEnrollemnt)
    #setCollegeName will accept a string and validate for 0<length<=50
    def setCollegeName(self,collegeName):
        if(len(collegeName)>0 and len(collegeName)<=50):
            self.collegeName=collegeName
        else:
            print("Invalid college name length given; cannot be 0 or exceed 50")
            print("College name set to default value: " + defaultCollegeName)
            self.collegeName=defaultCollegeName
    #setMajorList erases current list and sets new on using addMajor to validate input
    def setMajorList(self,majorList):
        self.majorList=[]
        for i in range(len(majorList)):
            self.addMajor(majorList[i])
    #addMajor adds major only if not duplicate
    def addMajor(self,strMajor):
        if(self.findMajor(strMajor)==-1):
            self.majorList.append(strMajor)
        else:
            print("The Major " +strMajor + " already exists within " + self.collegeName)
            print("and will therefore not be added to the college")
    #findMajor, return index of major or -1 if DNE
    def findMajor(self,strMajor):
        for i in range(len(self.majorList)):
            if (self.majorList[i] == strMajor):
                return i
            else:
                print(self.collegeName + " does not contain the major: " + strMajor)
                return -1
    #deleteMajor deletes major with given name
    def deleteMajor(self,strMajor):
        index = self.findMajor(strMajor)
        if(!(index == -1)):
            self.majorList.pop(index)
            print("The Major: " + strMajor + " was deleted")
        else:
            print("The Major: " + strMajor + " was not found or deleted")
    #setProfList Initialize will erase current list and set a new one
    #using the addProf method to validate that duplicates are not added
    def setProfList(self,profList):
        self.profList=[]
        for in in range(len(profList)):
            self.addProf(profList[i])
    #addProf wil add the given Professor object if no object already
    #exists with the same name
    def addProf(self,prof):
        if(self.findProf(prof.getName())==-1):
            self.profList.append(prof)
        else:
            print("A professor with the name" +prof.getName() +"already exists")
            print("within" + self.collegeName + "and therefore will not be added")
    #findProf method returns the index of a Professor object with the given name
    #will return -1 if the cannot find a valid object
    def findProf(self,profName):
        for i in range(len(self.profList)):
            if (self.profList[i].getName() == profName):
                return i
            else:
                print("Professor " + profName + " was not found within the college" + self.collegeName)
                return -1
    #getProf method, relies on index returned from findProf
    #returns a Professor object with the given object
    def getProf(self,profName):
        index = self.findProf(profName)
        if(index>=0 and index<len(profList)):
            return profList[index]
        else:
            print("The professor with at index 0 will be returned instead")
            return profList[0]
    #deleteProf will delete the Professor object with given name
    def deleteProf(self,profName):
            index = self.findProf(profName)
            if(!(index == -1)):
                self.profList.pop(index)
                print("The Prof: " + profName + " was deleted")
            else:
                print("The Prof: " + profName + " was not found or deleted")
    #getCollegeEnrollment will return an integer
    def getCollegeEnrollment(self):
        return self.getCollegeEnrollment
    #getCollegeName will return an integer
    def getCollegeName(self):
        return self.collegeName
