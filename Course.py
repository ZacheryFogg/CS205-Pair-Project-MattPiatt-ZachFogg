# Course class 

#Author: Matthew Piatt


class Course:
	course_title = None ;
	credits = 0;
	sections = list(()); 
	#default constructor, sections need to be updated manually. Defaults to empty list  
	def __init__(self, title, credits):
		self.course_title = title
		self.credits = credits
		self.sections = list(())

	# can change the course title, credits, or sections through public methods

	def set_credits(self, credit_value):
		self.credits = credit_value

	def set_course_title(self, new_title):
		self.course_title = new_title

	def add_section(self, section):
		sections.append(section)
		sections = list(set(section)) # removes potential duplicate sections

	def remove_section(self, section):
		sections.remove(section)

	def display_course_info(self):
		print("\n\nCourse title: " + self.course_title +"\n" + "Credits: " + str(self.credits) + "\n"
			"Sections: " + str(self.sections)+"\n\n")

	#def get_credits(self):
	#	print(str(credits))

	def get_course_title(self):
		print("Course title: " + self.course_title)

	def get_sections(self):
		print("Sections: " + str(self.sections))


def main():
	test_course = Course("Random",3)
	#test_course.get_credits()
	test_course.display_course_info()


main()

