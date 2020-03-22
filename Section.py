#section class

#Author: Matthew Piatt

class section():
	professor = None # name of professor teaching the course
	section = None # section label, character
	time = None # start time
	duration = None # duration of class
	location = None # location of class
	enrollment = None # student enrollment in this section of class


	#Note: sections are differentiated by their section character.
	def __init__(self,professor,section,time,duration,location,enrollment):
		self.professor = professor
		self.section = section.upper()
		self.time = time
		self.duration = duration
		self.location = location
		self.enrollment = enrollment

	#Overwriting default string method. Will only return the section character.
	def __str__(self):
		return self.section

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
		return self.professor

	def getSection(self):
		return self.section

	def getTime(self):
		return self.time

	def getDuration(self):
		return self.duration

	def getLocation(self):
		return self.location

	def getEnrollment(self):
		return self.enrollment
