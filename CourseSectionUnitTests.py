#Unit tests for Course and Section classes. 
#Author: Matthew Piatt

import unittest
import Course
import Section

class courseAndSectionTest(unittest.TestCase):


	#Creating section and course objects to be used in testing
	def setUp(self):
		self.course1 = Course.Course("title",3)
		self.section1 = Section.section("Professor", "A","8:30","20 min","Discovery 403", "1")
		self.section2 = Section.section("Professor", "B","4:20","20 min","Discovery 403", "2")



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



if __name__ == '__main__':
	unittest.main()

