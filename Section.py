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
	def set_professor(self,professor):
		self.professor = professor

	def set_section(self,char):
		self.section = char

	def set_time(self,time):
		self.time = time

	def set_duration(self, duration):
		self.duration = duration

	def set_location(self, location):
		self.location = location

	def set_enrollment(self, enrollment):
		self.enrollment = enrollment


	# Display section information
	def display_section_information(self):
		print("\n\nProfessor: " + str(self.professor) +"\n"
			"Section: " + str(self.section) + "\nTime: " + str(self.time)
			+"\nDuration: " + str(self.duration) +"\nLocation: " + str(self.location)
			+"\nEnrollemnt: " + str(self.enrollment))

	#Getters for all parameters
	def get_professor(self):
		print(self.professor)

	def get_section(self):
		print(str(self.section))

	def get_time(self):
		print(str(self.time))

	def get_duration(self):
		print(self.duration)

	def get_location(self):
		print(self.location)

	def get_enrollment(self):
		print(str(self.enrollment))

def main():
	test_section = section("dis dick","D","8:00","50 min","your moms", 2)
	test_section.display_section_information()
main()

