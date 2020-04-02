#Simulation
import University
import College
import Professor
import Course
import Section

class Simulation:
  #uni is a University object, cems/cas are College objects, prof is a Professor object
  #cour is a Course object, sec is a Section Object
  def __init__(self):
    #initialize objects
    self.uni = University.University("UVM", 12000, "Burlington, Vermont", 18000, 45000,[])
    self.cems = College.College("CEMS", 2000, [],[])
    self.cas = College.College("CAS", 3000, [],[])
    self.john = Professor.Professor("John Doe", "Votey 401", False, 3.0,[])
    self.jane = Professor.Professor("Jane Doe", "Votey 402", True, 2.5,[])
    self.sam = Professor.Professor("Sam Doe", "Votey 403", True, 5.0,[])
    self.cs127 = Course.Course("CS 127", 3)
    self.cs424 = Course.Course("CS 424", 18)
    self.cs319 = Course.Course("CS 319", 3)

  def run(self):
    #Demonstration of University
    print("University before Alterations:\n")
    self.uni.printUniversity()
    #Add colleges
    self.uni.setCollegeList([self.cas, self.cems])
    #Increase Tuition
    self.uni.increaseTuition(2.0)
    #Change Enrollement
    self.uni.setEnrollment(11500)
    #Delete and then add the same college
    print("Deleting and Adding Colleges from University")
    self.uni.delCollege("CAS")
    self.uni.printCollegeList()
    self.uni.addCollege(self.cas)
    self.uni.printCollegeList()
    #Find a college that doesn't exist
    print("Trying to find a college that doesn't exist")
    index1 = self.uni.findCollege("Grossman")
    if(index1==-1):
        print("Grossman college was not found")
    else:
        print("Grossman college exists at index: " + str(index))
    print("University after Alterations:\n")
    self.uni.printUniversity()

    #Demonstration of College
    print("CEMS before Alterations:\n")
    self.cems.printCollege()
    #Add/Delete Majors
    self.cems.setMajorList(["Computer Science","Mechanical Engineering","Mathematics"])
    self.cems.addMajor("Biomedical Engineering")
    self.cems.delMajor("Mathematics")
    #Add/Delete Professors
    self.cems.setProfList([self.jane, self.john])
    self.cems.addProf(self.sam)
    self.cems.delProf("John Doe")
    #Increase Enrollment
    self.cems.setCollegeEnrollment(3500)
    #Find
    print("Trying to find a major that doesn't exist and a professor that does")
    index2 = self.cems.findProf("Jane Doe")
    if(index2 == -1 ):
        print("Jane Doe is not a professor in CEMS")
    else:
        print("Jane Doe is a professor in CEMS and exists at index " + str(index2))

    index3= self.cems.findMajor("Art Education")
    if(index3 == -1 ):
        print("Art Education is not a major in CEMS")
    else:
        print("Art Education is a major in CEMS and exists at index " + str(index3))
    print("CEMS after Alterations:\n")
    self.cems.printCollege()

    #Demonstration of Professor Class
    print("Professor John Doe Before Alterations:\n")
    self.john.printProfessor()
    #Add and delete courses
    self.john.setCourseList([self.cs127,self.cs319])
    self.john.addCourse(self.cs424)
    self.john.delCourse("CS 127")
    #Update office, tenure, and rating
    self.john.setTenure(1)
    self.john.setRating(4.0)
    self.john.setOffice("Dicovery 501")
    #Try and Find a course
    index4= self.john.findCourse("CS 319")
    if(index4==-1):
        print("John Doe does not teach CS 319")
    else:
        print("John Does does teach CS 319")
    print("Professor John Doe after Alterations:\n")
    self.john.printProfessor()

    #Demonstration of Course and section class
    print("\n\nOriginal course before alterations: \n\n")
    self.cs127.displayCourseInfo()
    #self.cs127.addSection() #Uncomment these to build section manually.
    #self.cs127.addSection()

    self.cs127Section = Section.section("Professor2", "BCD", "time", "duration", "location", -10)
    self.cs127.addSection(self.cs127Section)

    self.cs127.displaySection("A")
    self.cs127.displaySection("B")
    self.cs127.setCourseTitle("cs1127")
    self.cs127.setCredits("4")
    print("\n\nAltered course: \n\n")
    self.cs127.displayCourseInfo()
    self.cs127.displayAllSections()

    self.cs127Section.setDuration("3 hrs")
    print(self.cs127Section.duration)
