# CS205-Pair-Project-MattPiatt-ZachFogg
Repository for CS 205 Pair Project(Matt Piatt and Zach Fogg) 

This repository's purpose is to model a university.

For our data we decided to model a university, specifically UVM. There will be five entities in our model; A University, Colleges within that university, Professors that teach within those colleges, and Courses that those professors teach, and subsections of those Courses. A rough draft of these various entities is below, some fields may be dropped or added: 

University
	
	Fields:
	colleges : set <College>    (ie. CEMS, CAS …) 
	enrollment : integer 
	universityName: string
	tuition : integer
	location : string
	public : boolean
	
	Methods: 
addCollege, increaseTuition, standard getters and setters for other fields

Colleges

	Fields:
	majors : set<String> 
	collegeName: string
	professors: set<Professor> 
	enrollment : integer    (a subset of university enrollment) 
	
	Methods: 
addProfessors, addMajors, adjustEnrollement, getters, setters 

Professors

	Fields:
 
name : string
coursesTaught : set<Course>
office : string 
tenure : boolean
rating : double     (obtained from rate my professor) 
	
Methods: 
addCourses, standard getters and setters 

Courses 

	Fields: 
	title : string
	creditHours : shortInt 
sections: set<Section> 


Methods: standard getters and setters, addSection, removeSection

Section

	Fields: 
	professor : Professor 
	section: char 
	time : String 
	location : string
enrollment : integer 
