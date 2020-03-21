import unittest
import Univerity
import College
import Professor
import Course
import Section

class TestModel(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    # called one time, at beginning
    print('setUpClass()')
    #initialize objects.
    #Sufix Uni indicates a University object
    #Sufix Col indicates a College object
    #Sufix Prof indicates a Professor object
    #Sufix Cour indicates a Course Object
    self.uvmUni = University.University("UVM", 12000, "Burlington, Vermont", 18000, 45000,[])

    self.cemsCol = College.College("CEMS", 2000, [],[])
    self.casCol = College.College("CAS", 3000, [],[])
    self.grossmanCol = College.College("Grossman School of Buisness", 2400, [],[])
    self.larnerCol = College.College("Larner College of Medicine", 4000, [],[])

    self.johnProf = Professor.Professor("John Doe", "Votey 401", False, 3.0,[])
    self.janeProf = Professor.Professor("Jane Doe", "Votey 402", True, 2.5,[])
    self.samProf = Professor.Professor("Sam Doe", "Votey 403", True, 5.0,[])
    self.taylorProf = Professor.Professor("Taylor Doe", "Votey 404", False, 1.0,[])

    self.cs127Cour = Course.Course("CS 127", 3)
    self.cs424Cour = Course.Course("CS 424", 18)
    self.cs319Cour = Course.Course("CS 319", 3)

  @classmethod
  def tearDownClass(cls):
    # called one time, at end
    print('tearDownClass()')

  def setUp(self):
    # called before every test
    print('setUp()')

  def tearDown(self):
    # called after every test
    print('tearDown()')

  #---------------------Zachs UnitTesting----------------------------------
  #This test function will test all methods related to the collegeList field
  #ie. addCollege, delCollege, findCollege...ect.
  def test_UniCollegeList(self):

  #---------------------Matts UnitTesting----------------------------------


  
#-----------------------------------------
if __name__ == "__main__":
  unittest.main()
