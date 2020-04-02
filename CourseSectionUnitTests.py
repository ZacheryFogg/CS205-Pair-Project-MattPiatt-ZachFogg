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

	def testInputValidation(self):
		#Invalid input for professor: contains number. Default for professor is professor
		self.section1.setProfessor("professor12")
		self.assertEqual(self.section1.getProfessor(), "professor")

		#Invalid input for section: must be one character. Should default to 'A'
		self.section1.setSection("ABC")
		self.assertEqual(self.section1.getSection(), "A")

		#Invalid input for time: Should default to 00:00
		self.section1.setTime("12:12:12")
		self.assertEqual(self.section1.getTime(), "00:00")

		#Invalid input for duration, wrong unit: should default to 0 min
		self.section1.setDuration(".04 days")
		self.assertEqual(self.section1.getDuration(), "0 min")

		#Invalid input for duration, above maximum value: should default to 0 min
		self.section1.setDuration("10000 min")
		self.assertEqual(self.section1.getDuration(), "0 min")

		#Invalid input for duration, wrong format: should default to 0 min
		self.section1.setDuration("10 hours 20 minutes")
		self.assertEqual(self.section1.getDuration(), "0 min")

		#Invalid input for location, wrong format: should default to "Unknown 000"
		self.section1.setLocation("2275 oak ave")
		self.assertEqual(self.section1.getLocation(), "Unknown 000") 

		#Invalid input for location, wrong format: should default to "Unknown 000"
		self.section1.setLocation("423 Waterman")
		self.assertEqual(self.section1.getLocation(), "Unknown 000")

		#Invalid input enrollment, below zero. Should default to 0
		self.section1.setEnrollment(-12)
		self.assertEqual(self.section1.getEnrollment(), 0)

		#Invalid input for credits, below zero. Should default to 0
		self.course1.setCredits(-3)
		self.assertEqual(self.course1.getCredits(), 0)

		#Invalid input for title, empty string. Should default to "course title"
		self.course1.setCourseTitle(" ")
		self.assertEqual(self.course1.getCourseTitle(), "course title")



if __name__ == '__main__':
	unittest.main()

