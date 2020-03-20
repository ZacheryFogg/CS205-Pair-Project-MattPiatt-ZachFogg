#section class

#Author: Matthew Piatt

class section():
	professor = None # name of professor teaching the course
	section = None # section label, character
	time = None # start time
	duration = None # duration of class
	location = None # location of class
	enrollment = None # student enrollment in this section of class

	def __init__(self,professor,section,time,duration,location,enrollment):
		self.professor = professor
		self.section = section
		self.time = time
		self.duration = duration
		self.location = location
		self.enrollment = enrollment

	#setters for all variables
	def setProfessor(self,professor):
		self.professor = professor

	def setSection(self,char):
		self.section = char

	def setTime(self,time):
		self.time = time

	def setDuration(self, duration):
		self.duration = duration

	def setLocation(self, location):
		self.location = location

	def setEnrollment(self, enrollment):
		self.enrollment = enrollment


	# Display section information
	def displaySectionInformation(self):
		print("\n\nProfessor: " + str(self.professor) +"\n"
			"Section: " + str(self.section) + "\nTime: " + str(self.time)
			+"\nDuration: " + str(self.duration) +"\nLocation: " + str(self.location)
			+"\nEnrollemnt: " + str(self.enrollment))

	#Getters for all parameters
	def getProfessor(self):
		print(self.professor)
		return self.professor

	def getSection(self):
		print(str(self.section))
		return self.section

	def getTime(self):
		print(str(self.time))
		return self.time

	def getDuration(self):
		print(self.duration)
		return self.duration

	def getLocation(self):
		print(self.location)
		return self.location

	def getEnrollment(self):
		print(str(self.enrollment))
		return self.enrollment

#def main():
#	test_section = section("dis dick","D","8:00","50 min","your moms", 2)
#	test_section.displaySectionInformation()
#main()
