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
		self.setProfessor(professor)
		self.setSection(section.upper())
		self.setTime(time)
		self.setDuration (duration)
		self.setLocation(location)
		self.setEnrollment(enrollment)

	#Overwriting default string method. Will only return the section character.
	def __str__(self):
		return self.section

	#setters for all variables
	def setProfessor(self,professor): #should not contain any numbers
		for char in professor:
			if char.isdigit():
				print("Invalid professor input. Professor names do not contain numbers.\n")
				print("Defaulting to professor for professor")
				self.professor = "professor"
				return
		self.professor = professor

	def setSection(self,char): # if given multiple characters do nothing
		if len(char) > 1: #invlaid input
			print("\nInput must be a single character. Example: B \n" )
			print("Defaulting to A for section\n\n")
			self.section ="A"
		else:
			self.section = char

	def setTime(self,time): # must be a string of form number:number
		inputTuple = time.partition(":") #returns tuple [[number],[:],[number]]

		if inputTuple[0].isdigit() and len(inputTuple[0]) <= 2  and inputTuple[len(inputTuple)-1].isdigit() and len(inputTuple[len(inputTuple)-1]) <= 2:
			self.time = time

		else:
			print ("Input must be a time. Example: 10:30 \n")
			print("Defaulting to 00:00 for time")
			self.time = "00:00"


	def setDuration(self, duration): # must be of form value unit ex: 50 min
		inputString = duration.rstrip() #strip all trailing whitespace
		inputString = duration.lstrip() #strip all leading whitespace

		timeUnits = list(()) # will be ["min", "hrs"]
		timeUnits.append("min")
		timeUnits.append("hrs")

		count = 0 # Increment to determine which unit matches

		inputString = inputString.split() #should split on the space remaining

		if len(inputString) > 2 : # invalid input
			print("Invalid duration input. Input must be of the form value unit example: 50 min \n")
			print("Defaulting to 0 min for duration\n\n")
			self.duration = "0 min"
			return
		else:
			for unit in timeUnits:
				count += 1
				if (unit == inputString[len(inputString) - 1] ) :
					if (count == 1 and int(inputString[0]) <= 300): #class length should be less than 500 minutes
						self.duration = duration
						return
					elif ((count == 2) and (int(inputString[0]) <= 5)):
						self.duration = duration
						return
					else:
						print("Class duration above maximum allowed (5 hours or 300 min is the max)\n")
						print("Defaulting to 0 min for duration\n\n")
						self.duration = "0 min"
						return
				else:
					print("\nUnit of measurement not found, allowed units are: min , hrs \n")
					print("Defaulting to 0 min for duration\n\n")
					self.duration = "0 min"
					return


	def setLocation(self, location): #of form building classroom ex: Waterman 423
		inputString = location.rstrip() #remove trailing whitespace
		inputString = location.lstrip() # remove leading whitespace
		inputString = inputString.split() # should split on remaining whitespace and return a list

		if len(inputString) > 2 : # invalid input
			print("Invalid location input. Input must be of the form building classroom Example: Discovery 403")
			print("Defaulting to Unknown 000 for location")
			self.location = "Unknown 000"

		elif not(inputString[0].isalnum() and inputString[len(inputString) - 1].isdigit()): #if either fails invalid input
			print("Invalid location input. Input must be of the form building classroom Example: Discovery 403\n")
			print("Defaulting to Unknown 000 for location\n\n")
			self.location = "Unknown 000"

		else:
			self.location = location



	def setEnrollment(self, enrollment): # must be nonnegative and non zero
		if int(enrollment) <= 0: #invalid argument, do nothing
			print("Enrollment must be nonzero and not negative\n")
			print("Defaulting to 0 for enrollment\n\n")
			self.enrollment = 0
		else:
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
		print(self.section)
		return self.section

	def getTime(self):
		return self.time

	def getDuration(self):
		return self.duration

	def getLocation(self):
		return self.location

	def getEnrollment(self):
		return self.enrollment
