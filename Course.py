# Course class

#Author: Matthew Piatt
import Section


class Course:
	courseTitle = None ;
	credits = 0;
	sections = list(());
	#default constructor, sections need to be updated manually. Defaults to empty list
	def __init__(self, title, credits):
		self.courseTitle = title
		self.credits = credits
		self.sections = list(())

	# can change the course title, credits, or sections through public methods

	def setCredits(self, creditValue):
		self.credits = credit_value

	def setCourseTitle(self, newTitle):
		self.courseTitle = newTitle

	def addSection(self, section):
		sections.append(section)
		sections = list(set(section)) # removes potential duplicate sections

	def removeSection(self, section):
		sections.remove(section)

	def displayCourseInfo(self):
		print("\n\nCourse title: " + self.courseTitle +"\n" + "Credits: " + str(self.credits) + "\n"
			"Sections: " + str(self.sections)+"\n\n")

	#def get_credits(self):
	#	print(str(credits))
		pass
	def getCourseTitle(self):
		#print("Course title: " + self.courseTitle)
		return self.courseTitle

	def getSections(self):
		print("Sections: " + str(self.sections))
		return self.sections

#def main():
	#test_course = Course("Random",3)
	#test_course.get_credits()
	#test_course.displayCourseInfo()


#main()
