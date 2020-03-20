#University Class
#Authored By Zachery Fogg

#Imports
import College
#Class Declaration
class University:
    #Constructor
    def __init__(self,uniName,enrollment,location,inStateTution,outStateTution,collegList):
        #Set Default values
        self.defaultTuition=10000
        self.defaultEnrollemnt=10000
        self.defaultUniName="EveRy University"
        self.defaultLocation="Gen Er, IC"
        self.collegeList=[]
        #Unser Input values
        self.setUniName(uniName)
        self.setEnrollment(enrollment)
        self.setLocation(location)
        self.__setTuition(inStateTution,outStateTution)
        self.setCollegeList(collegList)

    #Private method __setTuition to set inState and outState Tuition
    #Will set to default values if not 0<tuition<1000000
    def __setTuition(self,inStateTution, outStateTution):
        if(inStateTution>=0 and inStateTution<1000000):
            self.inStateTution = inStateTution
        else:
            print("Invalid InState Tuition value")
            print("InState Tuition set to: " + str(defaultTuition))
            self.inStateTution = defaultTuition
        if(outStateTution>=0 and outStateTution<1000000):
            self.outStateTution = outStateTution
        else:
            print("Invalid OutState Tuition value")
            print("OutState Tuition set to: " + str(defaultTuition))
            self.outStateTution = defaultTuition
    #Method to print out Univerity
    def printUniversity(self):
        print(self.uniName)
        print("At " + self.location)
        print("Total Enrollment: " + str(self.enrollment))
        print("In State Tuition: " + str(self.inStateTution))
        print("Out of State Tuition: " + str(self.outStateTution))
        self.printCollegeList()
    #Method to print out list of Colleges
    def printCollegeList(self):
        if(len(self.collegeList)==0):
            print("There are no colleges within " + self.uniName)
            return
        print("List of Colleges within " + self.uniName + ":")
        for i in range(len(self.collegeList)):
            print(self.collegeList[i].getCollegeName() + ",", end = " ")
        print("\n")

    #Increase Tuition method(accepts double 1-10)
    #will not change if not 1-10
    def increaseTuition(self,multiplier):
        if(multiplier>=1 and multiplier<=10):
            self.inStateTution*=multiplier
            self.outStateTution*=multiplier
        else:
            print("Invalid tuition multiplier; value must be double between 1 and 10")
            print("The values will not be changed")
    #setColList will set the collegeList to the one inputed
    #it will validate that all of the colleges are different
    #using addCollege method
    def setCollegeList(self,colList):
        self.collegeList=[]
        for i in range(len(colList)):
            self.addCollege(colList[i])
    #setUniName, accepts string 0<length<=50
    def setUniName(self,uniName):
        if(len(uniName)>0 and len(uniName)<=50):
            self.uniName=uniName
        else:
            print("Invalid university name length; cannot be 0 or exceed 50")
            print("University Name set to " + defaultUniName)
            self.uniName=defaultUniName
    #setLocation, accepts string of length 0<length<=50
    def setLocation(self,location):
        if(len(location)>0 and len(location)<=50):
            self.location=location
        else:
            print("Invalid location name length; cannot be 0 or exceed 50")
            print("Location set to " + defaultLocation)
            self.location=defaultLocation
    #setEnrollment will accept values 0<=value<=1000000
    def setEnrollment(self,enrollment):
        if(enrollment>=0 and enrollment<=1000000):
            self.enrollment=enrollment
        else:
            print("Invalid enrollment value; cannot be less than 0 or exceed 1000000")
            print("Enrollment set to: " + str(defaultEnrollemnt))

    #Method to add college to college list, will not let college with duplicate name be added
    def addCollege(self,college):
        if ((self.findCollege(college.getCollegeName()))!=-1):
            print("There is already a College with the name " + college.getCollegeName())
            print("in the University. This college will not be added to the University")
        elif(college.getCollegeEnrollment()>self.enrollment):
            print(college.getCollegeName()) + " has an invalid enrollment value"
            print("College enrollment cannot exceed the enrollment of the University")
            print("that it exists within. This college will not be added to the University")
        else:
            self.collegeList.append(college)

    #Method to search for a college, will return index of college
    #or -1 if college is not found
    def findCollege(self,collegeName):
        if(len(self.collegeList)==0):
            return -1
        for i in range(len(self.collegeList)):
            if (self.collegeList[i].getCollegeName() == collegeName):
                return i
        #print("The College: " + collegeName + " was not found")
        return -1
    #getCollege Method, accepts the name of the college
    def getCollege(self,collegeName):
        index = self.findCollege(collegeName)
        if(index>0 and index<len(self.collegeList)):
            return collegeList[index]
        else:
            print("The college "+ collegeName + "was not found")
            print("The college at index 0 will be returned instead")
            return collegeList[0]
    #Method to delete a college, accepts the name of the college
    def delCollege(self,collegeName):
        index = self.findCollege(collegeName)
        if(not(index == -1)):
            self.collegeList.pop(index)
            print("The College: " + collegeName + ", was deleted")
        else:
            #print error
            print("The College: " + collegeName + ", was not found or deleted")
