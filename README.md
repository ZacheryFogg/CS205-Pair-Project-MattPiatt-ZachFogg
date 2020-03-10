# CS205-Pair-Project-MattPiatt-ZachFogg
Repository for CS 205 Pair Project(Matt Piatt and Zach Fogg)

This repository's purpose is to model a university.

For our data we decided to model a university, specifically UVM. There will be five entities in our model; A University, Colleges within that university, Professors that teach within those colleges, and Courses that those professors teach, and subsections of those Courses. A rough draft of these various entities is below, some fields may be dropped or added:

University

	Fields:

	collegeList        : list<College> 	
	enrollment         : integer
	universityName     : string
	inStateTuition     : integer
	outStateTution     : integer
	location           : string
	defaultTuition     : integer
	defaultEnrollemnt  : integer
	defaultUniName     : string
	defaultLocation    : String



	Methods:    

	Constructor
	(private)setTuition: void
	printUniversity    : void
	increaseTuition    : void
	setCollegeList     : void
	setUniName         : void
	setLocation        : void
	setEnrollment      : void
	addCollege         : void
	findCollege        : integer
	getCollege 				 : College
	delCollege         : void
	printCollegeList   : void

College

	Fields:

	majors             : set<String>
	collegeName        : string
	profList           : list<Professor>
	colEnrollment      : integer
	defaultCollegeName : string
	defaultEnrollemnt  : integer

	Methods:

	Constructor        : void
	printCollege		   : void
	printMajors 			 : void
	printProfessors    : void
	setCollegeEnrollment: void
	setCollegeName     : void
	setMajorList  		 : void
	addMajor           : void
	findMajor          : integer
	deleteMajor        : void
	setProfList        : void
	addProf            : void
	findProf           : integer
	getProf 					 : Professor
	deleteProf         : void
	getCollegeEnrollment: integer
	getCollegeName     : string

Professors

	Fields:

	name               : string
	courseList         : list<Course>
	office             : string
	tenure             : boolean
	rating             : double
	defaultName 		   : string
	defaultOffice 		 : string
	defaultTenure 		 : boolean
	defaultRating		   : double

	Methods:

	Constructor        : void
	setName            : void
	setOffice          : void
	setTenure          : void
	setRating 				 : void
	setCourseList  	   : void
	addCourse 				 : void
	findCourse         : integer
	getCourse          : Course
	delCourse					 : void
	getOffice 				 : string
	getTenure          : boolean
	getName            : string
	getRating 				 : double




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
