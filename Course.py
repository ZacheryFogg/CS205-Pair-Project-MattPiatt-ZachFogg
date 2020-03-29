# Course class

#Author: Matthew Piatt
import Section


class Course:
	courseTitle = None;
	credits = 0;
	sections = list(());
	#default constructor, sections need to be updated manually. Defaults to empty list
	def __init__(self, title, credits):
		self.setCourseTitle(title)
		self.setCredits(credits)
		self.sections = list(())

	# can change the course title, credits, or sections through public methods

	def setCredits(self, creditValue):
		if int(creditValue) < 0 :
			print("Invalid credit value. Value must be a non negative integer \n")
			print("Defaulting to 0 credits\n\n")
			self.credits = 0
		else: #valid credit value
			self.credits = creditValue

	def setCourseTitle(self, newTitle):
		self.courseTitle = newTitle

	def addSection(self, sectionObj=None):

		if (sectionObj is not None): #add section that has been made. 
			if (isinstance(sectionObj, Section.section )): # Make sure the object being passed is of correct type
				self.sections.append(sectionObj)

		else:
			#add section that also needs to be created
			professor = input("\nEnter class professor's name: ")
			section = input("\nEnter section: ")
			time = input("\nEnter class start time: ")
			duration = input("\nEnter class duration: ")
			location = input("\nEnter class location: ")
			enrollment = input ("\nEnter class enrollment: ")

			sectionObj = Section.section(professor, section, time, duration, location, enrollment)
			self.sections.append(sectionObj)



	def removeSection(self, section):
		self.sections.remove(section)

	def displayCourseInfo(self):
		returnString = "\n\nCourse title: " + self.courseTitle +"\n" + "Credits: " + str(self.credits) + "\nSections: "
		for section in self.sections:
			returnString += str(section) + ", "
		returnString = returnString[:-2]
		print(returnString)
	def getCredits(self):
		return self.credits

	def getCourseTitle(self):
		#print("Course title: " + self.courseTitle)
		return self.courseTitle

	def getSections(self):
		#print("Sections: " + str(self.sections))
		return self.sections

	def displaySection(self, sectionChar):
		for section in self.sections:
	
			if (section.section == sectionChar.upper()): # found desired section
				section.displaySectionInformation()
				return 
			
		print("\n\nsection not found, make sure to specify unique section character\n\n")

	def displayAllSections(self):
		for section in self.sections:
			section.displaySectionInformation()



# def main():
# 	course1 = Course("default",3)
# 	print(course1.getCredits())

# main()
