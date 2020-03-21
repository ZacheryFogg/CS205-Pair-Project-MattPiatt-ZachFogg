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
  def tearDown(self):
    # called after every test
    print('tearDown()')

  #---------------------Zachs UnitTesting----------------------------------
  #Testing for University Class
  def test_UniIncreaseTuition(self):
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
  def test_UniCollegeList(self):
      #Test that setCollege list works as intended and does not allow duplicates
      #and does not allow a college with greater enrollment then the university
      self.uvmUni.setCollegeList([self.cemsCol, self.casCol, self.larnerCol])
      self.assertEqual([self.cemsCol, self.casCol], self.uvmUni.getCollegeList())
      #addCollege is used in setCollege list, so if above test cases are past then it works as intended
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

  def test_UniSetters(self):
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




  #---------------------Matts UnitTesting----------------------------------



#-----------------------------------------
if __name__ == "__main__":
  unittest.main()
