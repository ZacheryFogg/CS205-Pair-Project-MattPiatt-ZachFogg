import unittest
import University
import College
import Professor
import Course
import Section

class TestModel(unittest.TestCase):
  def setUp(self):
    # called before every test
    print('setUp()')

    #initialize objects.
    #Sufix Uni indicates a University object
    #Sufix Col indicates a College object
    #Sufix Prof indicates a Professor object
    #Sufix Cour indicates a Course Object


    #Zachs Objects
    self.uvmUni = University.University("UVM", 12000, "Burlington, Vermont", 18000, 45000,[])

    self.cemsCol = College.College("CEMS", 2000, [],[])
    self.casCol = College.College("CAS", 3000, [],[])
    self.grossmanCol = College.College("Grossman School of Buisness", 4000, [],[])
    self.larnerCol = College.College("Larner College of Medicine", 24000, [],[])

    self.johnProf = Professor.Professor("John Doe", "Votey 401", False, 3.0,[])
    self.janeProf = Professor.Professor("Jane Doe", "Votey 402", True, 2.5,[])
    self.samProf = Professor.Professor("Sam Doe", "Votey 403", True, 5.0,[])
    self.taylorProf = Professor.Professor("Taylor Doe", "Votey 404", False, 1.0,[])

    self.cs127Cour = Course.Course("CS 127", 3)
    self.cs424Cour = Course.Course("CS 424", 18)
    self.cs319Cour = Course.Course("CS 319", 3)
    self.cs205Cour = Course.Course("CS 205", 3)

    #Matts Objects
    self.course1 = Course.Course("title",3)
    self.section1 = Section.section("Professor", "Section","time","duration","location", "enrollment")
    self.section2 = Section.section("Professor", "Section","time","duration","location", "enrollment")


  def tearDown(self):
    # called after every test
    print('tearDown()')

  #---------------------Zachs UnitTesting----------------------------------
  #Testing for University Class
  def test_UniversityIncreaseTuition(self):
      #multiplier must be 1<=x<=10
      self.uvmUni.increaseTuition(0.5)
      self.assertEqual(self.uvmUni.getInStateTuition(), 18000)
      self.assertEqual(self.uvmUni.getOutStateTuition(), 45000)
      self.uvmUni.increaseTuition(10.1)
      self.assertEqual(self.uvmUni.getInStateTuition(), 18000)
      self.assertEqual(self.uvmUni.getOutStateTuition(), 45000)
      self.uvmUni.increaseTuition(1)
      self.assertEqual(self.uvmUni.getInStateTuition(), 18000)
      self.assertEqual(self.uvmUni.getOutStateTuition(), 45000)
      self.uvmUni.increaseTuition(2)
      self.assertEqual(self.uvmUni.getInStateTuition(), 36000)
      self.assertEqual(self.uvmUni.getOutStateTuition(), 90000)

  #This test function will test all methods related to the collegeList field
  #ie. addCollege, delCollege, findCollege...ect.
  def test_UniversityCollegeList(self):
      #Test that setCollege list works as intended and does not allow duplicates
      #and does not allow a college with greater enrollment then the university
      self.uvmUni.setCollegeList([self.cemsCol, self.casCol, self.larnerCol,self.cemsCol])
      self.assertEqual([self.cemsCol, self.casCol], self.uvmUni.getCollegeList())
      #addCollege is used in setCollege list, so if above test cases are passed then it works as intended
      #test delCollege
      self.uvmUni.addCollege(self.grossmanCol)
      self.uvmUni.delCollege("CEMS")
      self.assertEqual([self.casCol,self.grossmanCol], self.uvmUni.getCollegeList())
      self.uvmUni.delCollege("DNE")
      self.assertEqual([self.casCol,self.grossmanCol], self.uvmUni.getCollegeList())
      #test findCollege. will return index of college or -1 if not in list
      self.assertEqual(self.uvmUni.findCollege("CAS"), 0)
      self.assertEqual(self.uvmUni.findCollege("CEMS"),-1)
      #test getCollege. If college not in list, will return col at index 0
      self.assertEqual(self.uvmUni.getCollege("CAS"), self.casCol)
      self.assertEqual(self.uvmUni.getCollege("DNE"), self.casCol)

  def test_UniversitySetters(self):
      self.uvmUni.setUniName("")
      self.assertEqual(self.uvmUni.getUniName(), "EveRy University")
      self.uvmUni.setUniName("UVM")

      self.uvmUni.setLocation("")
      self.assertEqual(self.uvmUni.getLocation(), "Gen Er, IC")
      self.uvmUni.setLocation("Burlington, Vermont")

      self.uvmUni.setEnrollment(-1)
      self.assertEqual(self.uvmUni.getUniEnrollment(), 10000)
      self.uvmUni.setEnrollment(1000001)
      self.assertEqual(self.uvmUni.getUniEnrollment(),10000)




   #Testing for College Class
  def test_ColMajorList(self):
       #Test setMajorList. setMajorList uses addMajor method. Should not allow duplicates
       self.cemsCol.setMajorList(["Computer Science", "Mathematics", "Computer Science", "Data Science"])
       self.assertEqual(["Computer Science", "Mathematics", "Data Science"],self.cemsCol.getMajorList())
       #Test the collegeList can be updated
       self.cemsCol.addMajor("Mechanical Engineering")
       self.assertEqual(["Computer Science", "Mathematics", "Data Science","Mechanical Engineering"],self.cemsCol.getMajorList())
       #Test delMajor
       #Delete Major that does exist
       self.cemsCol.delMajor("Mathematics")
       self.assertEqual(["Computer Science","Data Science","Mechanical Engineering"],self.cemsCol.getMajorList())
       #Delete Major that DNE
       self.cemsCol.delMajor("Artistic Expression")
       self.assertEqual(["Computer Science","Data Science","Mechanical Engineering"],self.cemsCol.getMajorList())
       #Test findMajor
       #Find major that does exist
       self.assertEqual(self.cemsCol.findMajor("Data Science"),1)
       #find major that DNE
       self.assertEqual(self.cemsCol.findMajor("Dance Therapy"),-1)
       #majorList does not have a "getMajor" method, as majors are only strings

  def test_CollegeProfList(self):
       #Testing profList
       #Test setProfList. setProfList uses addProf, does not allow duplicates
       self.cemsCol.setProfList([self.johnProf, self.janeProf, self.samProf, self.johnProf])
       self.assertEqual([self.johnProf,self.janeProf, self.samProf], self.cemsCol.getProfList())
       #Test that list can be updated
       self.cemsCol.addProf(self.taylorProf)
       self.assertEqual([self.johnProf,self.janeProf, self.samProf,self.taylorProf], self.cemsCol.getProfList())
       #Test delProf
       #delete prof that does exist
       self.cemsCol.delProf("John Doe")
       self.assertEqual([self.janeProf, self.samProf,self.taylorProf], self.cemsCol.getProfList())
       #delete prof the DNE
       self.cemsCol.delProf("Sarah Solonick")
       self.assertEqual([self.janeProf, self.samProf,self.taylorProf], self.cemsCol.getProfList())
       #Test findProf
       #find prof that does exist
       self.assertEqual(self.cemsCol.findProf("Jane Doe"), 0)
       #find prof that DNE
       self.assertEqual(self.cemsCol.findProf("Joe Dirt"), -1)
       #Test getProf
       #get prof that does exist
       self.assertEqual(self.cemsCol.getProf("Taylor Doe"), self.taylorProf)
       #get prof that does not exist should return prof at index 0
       self.assertEqual(self.cemsCol.getProf("John Doe"), self.janeProf)

  def test_CollegeSetters(self):
       #Test setCollegeEnrollment, does not allow values <0 or   >=1000000
       self.cemsCol.setCollegeEnrollment(-1)
       self.assertEqual(self.cemsCol.getCollegeEnrollment(),0)
       self.cemsCol.setCollegeEnrollment(1000000)
       self.assertEqual(self.cemsCol.getCollegeEnrollment(),0)

       #Test setCollegeName, does not allow empty string
       self.cemsCol.setCollegeName("")
       self.assertEqual(self.cemsCol.getCollegeName(), "College of Education")

    #Testing for Professor Class
  def test_ProfessorCourseList(self):
      #Test setCourseList. setCourseList uses addCourse, does not allow duplicates
      self.johnProf.setCourseList([self.cs127Cour, self.cs319Cour, self.cs127Cour, self.cs424Cour])
      self.assertEqual([self.cs127Cour, self.cs319Cour,self.cs424Cour], self.johnProf.getCourseList())
      #Test that courseList can be modified
      self.johnProf.addCourse(self.cs205Cour)
      self.assertEqual([self.cs127Cour, self.cs319Cour,self.cs424Cour, self.cs205Cour], self.johnProf.getCourseList())
      #Test delCourse
      #delete course that does exist
      self.johnProf.delCourse("CS 127")
      self.assertEqual([self.cs319Cour,self.cs424Cour,self.cs205Cour], self.johnProf.getCourseList())
      #delete course that DNE
      self.johnProf.delCourse("CS 124")
      self.assertEqual([self.cs319Cour,self.cs424Cour,self.cs205Cour], self.johnProf.getCourseList())
      #Test findCourse
      #find course that does exist
      self.assertEqual(self.johnProf.findCourse("CS 424"),1)
      #find course that DNE
      self.assertEqual(self.johnProf.findCourse("CS 127"),-1)
      #Test getCourse
      #getCourse that does exist
      self.assertEqual(self.johnProf.getCourse("CS 319"), self.cs319Cour)
      #getCourse that DNE, should return course at index 0
      self.assertEqual(self.johnProf.getCourse("CS 008"), self.cs319Cour)

  def test_ProfessorSetters(self):
      #Test setName, does not allow empty string
      self.johnProf.setName("")
      self.assertEqual(self.johnProf.getProfName(),"Gener IcnAme")
      self.johnProf.setName("John Doe")
      self.assertEqual(self.johnProf.getProfName(),"John Doe")
      #Test setOffice, does not allow empty string
      self.johnProf.setOffice("")
      self.assertEqual(self.johnProf.getOffice(),"Building 101")
      self.johnProf.setOffice("Votey 301")
      self.assertEqual(self.johnProf.getOffice(),"Votey 301")
      #Test setRating, 0<=x<=5
      self.johnProf.setRating(-1)
      self.assertEqual(self.johnProf.getRating(), 0.0)
      self.johnProf.setRating(5.1)
      self.assertEqual(self.johnProf.getRating(), 0.0)
      self.johnProf.setRating(2.0)
      self.assertEqual(self.johnProf.getRating(), 2.0)
      #Test setTenure
      self.johnProf.setTenure(0)
      self.assertFalse(self.johnProf.getTenure())
      self.johnProf.setTenure(1)
      self.assertTrue(self.johnProf.getTenure())
      self.johnProf.setTenure(True)
      self.assertTrue(self.johnProf.getTenure())
      self.johnProf.setTenure(False)
      self.assertFalse(self.johnProf.getTenure())
      self.johnProf.setTenure("true")
      self.assertFalse(self.johnProf.getTenure())




  def testCourseSetMethods(self):
	  #Should change credit value to 2
      self.course1.setCredits(2)
      self.assertEqual(self.course1.getCredits(),2)

      #Should change title to CS205
      self.course1.setCourseTitle("CS205")
      self.assertEqual(self.course1.getCourseTitle(),"CS205")

  def testSectionSetMethods(self):
      #should set section professor to Jason Hibbeler
      self.section1.setProfessor("Jason Hibbeler")
      self.assertEqual(self.section1.getProfessor(),"Jason Hibbeler")

      #Should set section to B
      self.section1.setSection("B")
      self.assertEqual(self.section1.getSection(),"B")

      #Should set time to "3:30"
      self.section1.setTime("3:30")
      self.assertEqual(self.section1.getTime(), "3:30")

      #Should set duration to 50 min
      self.section1.setDuration("50 min")
      self.assertEqual(self.section1.getDuration(),"50 min")

      #Should set location to "Votey 209"
      self.section1.setLocation("Votey 209")
      self.assertEqual(self.section1.getLocation(), "Votey 209")

      #should set enrollment to 40
      self.section1.setEnrollment(40)
      self.assertEqual(self.section1.getEnrollment(), 40)

  def testAddSectionMethods(self):
      #Add sections, when added length should increase by 1
      self.course1.addSection(self.section1)
      self.assertEqual(len(self.course1.sections), 1)

      self.course1.addSection(self.section2)
      self.assertEqual(len(self.course1.sections), 2)

      #remove sections, when removed length should decrease by 1
      self.course1.removeSection(self.section2)
      self.assertEqual(len(self.course1.sections),1)

      #Check that the correct section was removed (therefore self.section1 should still be the only section)
      self.assertEqual(self.course1.sections[0], self.section1)

















  #---------------------Matts UnitTesting----------------------------------



#-----------------------------------------
if __name__ == "__main__":
  unittest.main()
