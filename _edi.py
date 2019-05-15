#!/usr/bin/python coding=utf-8

# Author : Édi Aires

# Work in Progress ...
# TO-DO -> full integration of input file with answers ; constrution of the final report

import os
from markdown import markdown
# import markdown2 
from xhtml2pdf import pisa
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


version = 1

# list that contains to answers in the written file
input_list = []

# add the answers (output) to a list to write as the respective answers and comments in the generated file with answers
answers_list=[]
comments_list=[]
table_for_report=[]



# TO-DO -> a dict is unordered so the questions will appear in different order
# maybe better use OrderedDict ( from collection import OrderedDict )

# create a dictionairy to store the answers to the questions
questions_and_answers = {
	"Q1": "",
	"Q2": "",
	"Q3": "",
	"Q4": "",
	"Q5": "",
	"Q6": "",
	"Q7": "",
	"Q8": "",
	"Q9": "",
	"Q10": "",
	"Q11": ""
}

# Questions
# Q1   -> Architeture
# Q2   -> Has a DB
# Q3   -> Type of data storage
# Q4   -> Which db
# Q5   -> Type of data
# Q6   -> Authentication
# Q7   -> User Registration
# Q8   -> Way of user registration
# Q9   -> Programming Languages
# Q10  -> Input Forms
# Q11  -> Upload Files


# TO -DO -> in case of answer "others" (user input), 
# at the time of execution add to respective dict

question_1 = {
	"1" : "Web Application",
	"2" : "Web Service",
	"3" : "Desktop Application",
	"4" : "Mobile Application",
	"5" : "ClientServer > Client Component",
	"6" : "ClientServer > Server Component ",
	"7" : "API Service",
	"8" : "Embedded System",
	"9" : ""
}

question_2 = {
	"1" : "Yes",
	"2" : "No"
}

question_3 = {
	"1" : "SQL",
	"2" : "NoSQL",
	"3" : "Local Storage",
	"4" : "Distributed Storage"
}

question_4 = {
	"1" : "SQL Server",
	"2" : "MySQL",
	"3" : "PostgreSQL",
	"4" : "SQLite",
	"5" : "OracleDB",
	"6" : "MariaDB",
	"7" : "MongoDB",
	"8" : "CosmosDB",
	"9" : "DynamoDB",
	"10" : "Cassandra",
	"11" : ""
}

question_5 = {
	"1" : "Personal Information",
	"2" : "Confidential Data",
	"3" : "Critical Data",
	"4" : ""
}

question_6 = {
	"1" : "No Authentication",
	"2" : "Username and Password",
	"3" : "Social Networks / Google",
	"4" : "SmartCard",
	"5" : "Biometrics",
	"6" : "Two Factor Authentication",
	"7" : "Multi Factor Authentication"
}

question_7 = {
	"1" : "Yes",
	"2" : "No"
}

question_8 = {
	"1" : "The users will register themselves",
	"2" : "Will be a administrator that will register the users"
}

question_9 = {
	"1" : "C#",
	"2" : "C / C++",
	"3" : "Java",
	"4" : "Javascript",
	"5" : "PHP",
	"6" : "Python",
	"7" : "Ruby",
	"8" : ""
}

question_10 = {
	"1" : "Yes",
	"2" : "No",
}

question_11 = {
	"1" : "Yes",
	"2" : "No",
}


question_12 = {
	"1" : "User Activity",
	"2" : "Error Messages",
	"3" : "Security Violations"
}



# print(questions_and_answers)
'''	
for i in questions_and_answers:
  	print(i + "  : " + questions_and_answers[i])

	
print (question_1)
print (question_2)
print (question_3)
print (question_4)
print (question_5)
print (question_6)
print (question_7)
print (question_8)
print (question_9)
print (question_10)
print (question_11)
'''

'''
for k, v in questions_and_answers.items():
    print(k, v)
'''



'''
>template para as perguntas
def NAME():
	print("  : ")
	print("")
	print( "  1 -   ")
	print( "  2 -   ")
	print( "  3 -   ")
	print( "  4 -   ")
	print("")

	list.append("Q6-" + str(input("  > ")))

'''

# ----------------------------------------------------------------------------
def readInputFromFile():

	# user inputs the file name and checks if the file exists
	while True:
		filepath = validateInput(2)
		if not os.path.isfile(filepath):
			print("File path {} does not exist...".format(filepath))
		else:
			break


	with open(filepath,'r') as file:
		line = file.readline()
		while line:

			# print (line.strip())
			# print (line.split('#')[0].strip() )

			# read line until character '#' which means after that is a comment
			input_list.append(line.split('#')[0].strip())
			line = file.readline()





# ----------------------------------------------------------------------------
# funtion to validate input and implemts dynamic arguments:
# if one argument is pass, it means what to validate
# if two arguments are pass it means that is to valide a int and
# there is a number of options to put in range

# means of arguments respectively
# arg(1) what to validate -> if it is to validate a int or a string (1 or 2)
# arg(2) n_options -> number of options in the question (==range)

def validateInput(*arg):

    # print("i was called with", len(arg),"arguments:",arg)
    # print (arg[0])
    # print (arg[1])

    while True:

        # validate a int
        if arg[0] == 1:
            try:
                user_input = input("  > ")

            # syntax error, name error
            except (SyntaxError, NameError, TypeError):
                print("  Not a valid answer!  ")
                print("")
                continue
            else:
                if (type(user_input) is int) and (user_input in range(0, arg[1])):
                    break
                else:
                    print("  Not a valid answer!  ")
                    print("")


        # validate a string
        if arg[0] == 2:
            try:
                user_input = input("  > ")

            # syntax error, name error
            except (SyntaxError, NameError, TypeError):
                print("  Not a valid answer!  ")
                print("")
                continue
            else:
                if type(user_input) is str:
                    break
                else:
                    print("  Not a valid answer!  ")
                    print("")

    return user_input


# ----------------------------------------------------------------------------
def arqui(version):
	print("---")
	print("")
	if version==1:
		print("  **Which will be the architecture of the system ?**  ")
	else:
		print("  **What is the architecture of the system ?**  ")

	print("  (This is a multiple choice question. Enter several options and end with 0.)  ")
	print("")
	print( "  1 - Web Application  ")
	print( "  2 - Web Service  ")
	print( "  3 - Desktop Application  ")
	print( "  4 - Mobile Application  ")
	print( "  5 - Client-Server > Client Component  ")
	print( "  6 - Client-Server > Server Component  ")
	print( "  7 - API Service  ")
	print( "  8 - Embedded System  ")
	print( "  9 - Others  ")
	print("")

	# function input() interprets the input
	# get user input differs from python 2.x and 3.x --> input() = version 3 | raw_input() = version 2.x
	# TO-DO change this funtion input (to enter a string it needs quotes)
	# maybe getting the python version and adapt the funtions or just using input() and enter string with quotes (current version)
 

	while(1):
		# validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
		value=validateInput(1,10)
		if value == 0:
			return 
		if value == 9:
			print( "  Please specify the architeture: (name between quotes)  ")			
			value2=validateInput(2)
			# question_1["9"] = str(value2)
			questions_and_answers["Q1"]=questions_and_answers["Q1"] + str(value2) + ";"

		else:
			questions_and_answers["Q1"]=questions_and_answers["Q1"] + str(value) + ";"
		


# ----------------------------------------------------------------------------
def hasDB(version):	
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **The system will use a Database ?**  ")
	else:
		print("  **The system use a Database ?**  ")
	print("")
	print( "  1 - Yes  ")	
	print( "  2 - No  ")
	print("")

	value=validateInput(1,3)
	questions_and_answers["Q2"]=str(value)
	
	
	if value == 1:
		typeOfDatabase(version)
		whichDatabase(version)
		sensitiveData(version)

	else:
		questions_and_answers["Q3"]="N/A"
		questions_and_answers["Q4"]="N/A"
		questions_and_answers["Q5"]="N/A"
		return


# ----------------------------------------------------------------------------
def typeOfDatabase(version):
	print("")
	print("---")
	print("")
	if version == 1 :
		print("  **Which will be type of data storage ?**  ")
	else:
		print("  **What is type of data storage ?**  ")
	print("")
	print( "  1 - SQL  ")	
	print( "  2 - NoSQL  ")
	print( "  3 - Local Storage  ")
	print( "  4 - Distributed Storage  ")
	print("")

	value = validateInput(1,5) 
	questions_and_answers["Q3"]=str(value)


# ----------------------------------------------------------------------------
def whichDatabase(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **Which Database will be used ?**  ")
	else:
		print("  **What is the Database used ?**  ")
	
	print("")
	print( "  1 - SQL Server  ")	
	print( "  2 - MySQL  ")
	print( "  3 - PostgreSQL  ")
	print( "  4 - SQLite  ")
	print( "  5 - OracleDB  ")
	print( "  6 - MariaDB  ")
	print( "  7 - MongoDB  ")
	print( "  8 - CosmosDB  ")
	print( "  9 - DynamoDB  ")
	print( "  10 - Cassandra  ")
	print( "  11 - Other  ")
	print("")
	
	value=validateInput(1,12)
	if value == 11:
		print( "  Please specify the name of database: (name between quotes)  ")
		value2=validateInput(2)
		questions_and_answers["Q4"]=str(value2)
	else:
		questions_and_answers["Q4"]=str(value)


# ----------------------------------------------------------------------------
def sensitiveData(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **Which type of data will be stored ?**  ")
	else:
		print("  **What is the type of data stored ?**  ")

	print("  (This is a multiple choice question. Enter several options and end with 0.)  ")
	print("")
	print( "  1 - Personal Information (Names, Address,...)  ")
	print( "  2 - Confidential Data  ")
	print( "  3 - Critical Data  ")
	print( "  4 - Other  ")
	print("")
	
	while(1):
		value=validateInput(1,5)
		if value == 0:
			return 
		if value == 4 :
			print( "  Please specify the architeture: (name between quotes)  ")
			# TO-DO change this funtion input
			value2=validateInput(2)
			#question_5["4"] = str(value2)
			questions_and_answers["Q5"]=questions_and_answers["Q5"] + str(value2) + ";"

		else:
			questions_and_answers["Q5"]=questions_and_answers["Q5"] + str(value) + ";"


# ----------------------------------------------------------------------------
def authentication(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **Which type of authentication will be implemented ?**  ")
	else:
		print("  **What is the type of authentication implemented in the system ?**  ")
	print("")
	print( "  1 - No Authentication  ")
	print( "  2 - Username and Password  ")
	print( "  3 - Social Networks / Google  ")
	print( "  4 - SmartCard  ")
	print( "  5 - Biometrics  ")
	print( "  6 - Two Factor Authentication  ")
	print( "  7 - Multi Factor Authentication  ")
	print("")

	value = validateInput(1,8)
	questions_and_answers["Q6"]=str(value)


# ----------------------------------------------------------------------------
def userRegist(version):
	print("")
	print("---")
	print("")
	if version == 1 :
		print("  **There will be a user registration ?**  ")
	else:
		print("  **There is a user registration ?**  ")
	print("")
	print( "  1 - Yes  ")
	print( "  2 - No  ")
	print("")

	value = validateInput(1,3)
	questions_and_answers["Q7"]=str(value)

	if value == 1 :
		typeOfUserRegist(version)
	else:
		questions_and_answers["Q8"] = "N/A"


# ----------------------------------------------------------------------------
def typeOfUserRegist(version):
	print("")
	print("---")
	print("")
	if version == 1 :
		print(" **Which way of user registration will be used ?**  ")
	else:
		print(" **Which way of user registration it's used ?**  ")
	print("")
	print( "  1 - The users will register themselves  ")
	print( "  2 - Will be a administrator that will register the users  ")
	print("")

	value = validateInput(1,3)
	questions_and_answers["Q8"]=str(value)


# ----------------------------------------------------------------------------
def languages(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **Which programming languages will be used in the implementation of the system ?**  ")	
	else:
		print("  **What is the programming languages used in the implementation of the system ?**  ")	
	
	print("  (This is a multiple choice question. Enter several options and end with 0.)  ")
	print("")
	print( "  1 - C#  ")
	print( "  2 - C / C++  ")
	print( "  3 - Java  ")
	print( "  4 - Javascript  ")
	print( "  5 - PHP  " )
	print( "  6 - Python  " )
	print( "  7 - Ruby  ")
	print( "  8 - Other / Property Language  ")
	print("")

	while(1):
		value=validateInput(1,9)
		if value == 0:
			return 
		if value == 8:
			print( "  Please specify the programming language: (name between quotes)  ")
			# TO-DO change this funtion input
			value2=validateInput(2)
			# question_9["8"]  = str(value2)
			questions_and_answers["Q9"]=questions_and_answers["Q9"] + str(value2) + ";"

		else:
			questions_and_answers["Q9"]=questions_and_answers["Q9"] + str(value) + ";"


# ----------------------------------------------------------------------------
def inputForms(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **The system will allow user input forms ?**  ")
	else:
		print("  **The system has user input forms ?**  ")
	print("")
	print( "  1 -Yes  ")
	print( "  2 - No  ")
	print("")

	value = validateInput(1,3)
	questions_and_answers["Q10"]=str(value)


# ----------------------------------------------------------------------------
def allowUploadFiles(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **The system will allow upload files ?**  ")
	else:
		print("  **The system allow upload files ?**  ")
	print("")
	print( "  1 - Yes  ")	
	print( "  2 - No  ")
	print("")

	value = validateInput(1,3)
	questions_and_answers["Q11"]=str(value)


# ----------------------------------------------------------------------------
def systemLogs(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **What type of information will show in logs files ?**  ")
	else:
		print("  **What is the type of information shown in logs files ?**  ")
	print("  (This is a multiple choice question. Enter several options and end with 0.)  ")
	print("")
	print( "  1 - User Activity  ")
	print( "  2 - Error Messages  ")
	print( "  3 - Security Violations  " )
	print("")

	value = validateInput(1,4)
	questions_and_answers["Q12"]=questions_and_answers["Q12"] + str(value) + ";"



'''
def users(version):
	print("---")
	print("")
	if version == 1:
		print("  **Users of the system?**  ")
	else:
		print("  **Users of the system?**  ")
	print("")
	print( "  1 - Internal and External Users  ")
	print( "  2 - Only Internal Users  ")
	print( "  3 -  Only External Users  " )
	print( "  4 -  Admins  " )
	print("")

	list.append("Q6-" + str(input("  > ")))



def deployment():
	print("Deployment : ")
	print("")
	print( "  1 - Public - Internet  ")
	print( "  2 - Private - internal infrastructure  ")
	print( "  3 - Public Cloud  ")
	print( "  4 - Private Cloud  ")
	print("")
	list.append("Q5-" + str(input("  > ")))



def nameOfWebServer(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **Name of Web Server ?**  ")
	else:
		print("  **Name of Web Server ?**  ")
	print("")
	print( "  1 - Apache  ")
	print( "  2 - Microsoft IIS  ")
	print( "  3 - Nginx  " )
	print( "  4 - Xamp  ")
	print( "  5 - The system doesn't use a web server  " )
	print("")

	list.append("Q-" + str(input("  > ")))
'''

##############################################################################################


# function to use graph easy to make the schematic using a call to the system
def designWithGraphEasy():
	# v=1
	sInput = ("design_schemes.txt")

	'''
	sOutput = "design_schemes" + str(v) 
	sOutput_html = "design_schemes" + str(v) + ".html")

	
	cmd1 = "graph-easy --input " + sInput + " > " + sOutput 
	cmd2 = "graph-easy --as=ascii " + sInput + " > " + sOutput
	cmd3 = "graph-easy --as=boxart " + sInput + " > " + sOutput
	cmd4 = "graph-easy --as=html " + sInput + " > " + sOutput_html
	
	'''
	cmd = ("graph-easy --as=svg " + sInput +" > design_schemes.svg")
	#print( cmd)
	# cmd2 = "graph-easy --as=ascii " + sInput + " > " + sOutput + ".txt")
	# print( cmd2
	
	os.system(cmd)
	# os.system(cmd2)

	# convert img svg to PNG
	drawing = svg2rlg("design_schemes.svg")
	renderPM.drawToFile(drawing, "design_schemes.png", fmt="PNG")


# ----------------------------------------------------------------------------
# function to convert the markdown report to html and pdf format
def convertReport():
	# input_filename = ("guides/example_report.md")
	# input_filename = "some_markdown.md")
	input_filename = ("FINAL_REPORT.md")

	output_filename = ("FINAL_REPORT.html")

	with open(input_filename,"r" ) as f:
		html_text= markdown(f.read(), extensions=[ 'markdown.extensions.tables','markdown.extensions.sane_lists'])  
	

	out= open(output_filename,"w")
	out.write(html_text)

	# writing in pdf file, the html content

	resultFile = open("FINAL_REPORT.pdf", "w+b")
	pisa.CreatePDF(html_text, dest=resultFile)
	# print( pisastatus)


# ----------------------------------------------------------------------------
def printData():

	generate_file = open("ans.txt", "w")	

	list_aux = []		
	# it is a multiple question

	# find if the answer correspond to option "others" (means that is user input text) OR fix this buy make it simple, verify if it the answer has only letters xD
	# find if the first caracter is a letter and if the answer has no more options
	if questions_and_answers["Q1"][0].isdigit() == False and questions_and_answers["Q1"].find(";") == -1 :
		list_aux.append( questions_and_answers["Q1"])

	else:

		# variable aux is a list that contains the answers chosen by the user to the question in cause
		# cut the string in the delimitator ";" 
		aux = questions_and_answers["Q1"].split(";")

		#delete last item (= None)
		aux = aux[:-1]
		# print(aux)

		# iterate the answers chosen by the user
		for item in aux:

			# iterate the options of the question and check what the chosen answers match
			for option in question_1:
				if item == option:
					list_aux.append( question_1[option] )

			# case of user input text
			if item.isdigit() == False: 
				list_aux.append (item)

		'''
		can put this code above (case of user input text) in other way : 
		if cant find the answer in the options of the question_1, add the item(= user input text)
		'''

	# print(list_aux)
	print("{:22} {:3} {:40} ".format("Architeture", ":", ' ; '.join(list_aux) ) )
	table_for_report.append([ "Architeture" , ' ; '.join(list_aux) ])

	answers_list.append(questions_and_answers["Q1"])
	comments_list.append(' ; '.join(list_aux))

	
	# --------------------------------------------
	for n in question_2:
		item = questions_and_answers["Q2"]		
		if  item == n:
			# print( "Has DB {:>18} ".format(":     ") + question_2[n])
			print("{:22} {:3} {:40} ".format("Has DB", ":" , question_2[n]) )

			table_for_report.append( [ "Has DB" , question_2[n] ])

			answers_list.append(questions_and_answers["Q2"])
			comments_list.append(question_2[n])


	# --------------------------------------------
	item = questions_and_answers["Q3"]
	# case this question is not answered, and the answer it will be "N/A"
	if questions_and_answers["Q3"].isdigit() == False :
		print( "{:22} {:3} {:40} ".format("Type of data storage", ":",  item) )

		table_for_report.append(["Type of data storage",  item ])

		answers_list.append(questions_and_answers["Q3"])
		comments_list.append(item)
	
	else:

		for n in question_3:					
			if  item == n:
				print( "{:22} {:3} {:40} ".format("Type of data storage", ":",  question_3[n]) )

				table_for_report.append([ "Type of data storage", question_3[n] ])

				answers_list.append(questions_and_answers["Q3"])
				comments_list.append(question_3[n])

	# --------------------------------------------

	item = questions_and_answers["Q4"]	
	for n in question_4:		
		if  item == n :
			print("{:22} {:3} {:40} ".format( "Which DB", ":", question_4[n]) )

			table_for_report.append( [ "Which DB",  question_4[n] ])
	
			answers_list.append(questions_and_answers["Q4"])
			comments_list.append(question_4[n])

	# case of user input text
	if item.isdigit() == False: 
		print("{:22} {:3} {:40} ".format( "Which DB", ":", item ) )

		table_for_report.append( [ "Which DB", item ])

		answers_list.append(questions_and_answers["Q4"])
		comments_list.append(item)


	# --------------------------------------------	
	list_aux = []	
	# it is a multiple question

	# find if the answer correspond to option "others" (means that is user input text) or not answered
	if questions_and_answers["Q5"][0].isdigit() == False and questions_and_answers["Q5"].find(";") == -1:
		list_aux.append( questions_and_answers["Q5"])

	else:

		# variable aux is a list that contains the answers chosen by the user to the question in cause
		# cut the string in the delimitator ";" 
		aux = questions_and_answers["Q5"].split(";")

		#delete last item (= None)
		aux = aux[:-1]

		for item in aux:
			for option in question_5:		
				if  item == option:
					list_aux.append( question_5[option] )

			# case of user input text
			if item.isdigit() == False: 
				list_aux.append (item)

	print("{:22} {:3} {:40} ".format("Type of data stored" , ":" , ' ; '.join(list_aux) ) )

	table_for_report.append( ["Type of data stored" , ' ; '.join(list_aux) ])

	answers_list.append(questions_and_answers["Q5"])
	comments_list.append(' ; '.join(list_aux))



	# --------------------------------------------
	for n in question_6:
		item = questions_and_answers["Q6"]		
		if  item == n:
			print("{:22} {:3} {:40}".format("Authentication", ":" , question_6[n]) )

			table_for_report.append( [ "Authentication" , question_6[n] ])

			answers_list.append(questions_and_answers["Q6"])
			comments_list.append(question_6[n])


	# --------------------------------------------
	for n in question_7:
		item = questions_and_answers["Q7"]		
		if  item == n:
			print("{:22} {:3} {:40}".format("User Registration", ":" , question_7[n]) )

			table_for_report.append( ["User Registration" , question_7[n] ])

			answers_list.append(questions_and_answers["Q7"])
			comments_list.append(question_7[n])


	# --------------------------------------------
	item = questions_and_answers["Q8"]
	if questions_and_answers["Q8"].isdigit() == False:
		print("{:22} {:3} {:40} ".format("Type of Registration", ": " , item) )

		table_for_report.append( ["Type of Registration", item ])

		answers_list.append(questions_and_answers["Q8"])
		comments_list.append(item)

	else :
		for n in question_8:
			if  item == n:
				print("{:22} {:3} {:40} ".format("Type of Registration", ": " , question_8[n]) )

				table_for_report.append( [ "Type of Registration", question_8[n] ])

				answers_list.append(questions_and_answers["Q8"])
				comments_list.append(question_8[n])


	# --------------------------------------------
	list_aux = []	
	# it is a multiple question
	
	# find if the answer correspond to option "others" (means that is only user input text)
	if questions_and_answers["Q9"][0].isdigit() == False and questions_and_answers["Q9"].find(";") == -1:
		list_aux.append( questions_and_answers["Q9"])

	else:

		# cut the string in the delimitator ";" 
		aux = questions_and_answers["Q9"].split(";")

		#delete last item (= None)
		aux = aux[:-1]

			
		for item in aux:
			for option in question_9:		
				if  item == option:
					list_aux.append( question_9[option] )

			# case of user input text
			if item.isdigit() == False: 
				list_aux.append (item)
	
	print("{:22} {:3} {:40} ".format("Programming Languages" , ":" , ' ; '.join(list_aux) ) )
	
	table_for_report.append( [ "Programming Languages" , ' ; '.join(list_aux) ])

	answers_list.append(questions_and_answers["Q9"])
	comments_list.append(' ; '.join(list_aux))


	# --------------------------------------------
	for n in question_10:
		item = questions_and_answers["Q10"]		
		if  item == n:
			print("{:22} {:3} {:40} ".format("Input Forms" , ":" , question_10[n]) )

			table_for_report.append( ["Input Forms" , question_10[n] ])

			answers_list.append(questions_and_answers["Q10"])
			comments_list.append(question_10[n])
			


	# --------------------------------------------
	for n in question_11:
		item = questions_and_answers["Q11"]		
		if  item == n:
			print("{:22} {:3} {:40} ".format("Upload Files" , ":" , question_11[n]) )

			table_for_report.append( [ "Upload Files" , question_11[n] ])

			answers_list.append(questions_and_answers["Q11"])
			comments_list.append(question_11[n])

	# -------------------------------------------
	# write / generate a file with all answers
	for i in range(0,len(answers_list)):
		generate_file.write( "{:20}{:3}{:20}\n".format(answers_list[i] , " # " , comments_list[i] ) )

	generate_file.close()

#############################################################################################################

# Information Capture main function
def informationCapture():

	print("---")
	print("")	
	print( "  **What is the status of development of the system ?**  ")
	print("")
	print("  1 - The system is yet to be developed.  ")
	print("  2 - The system is already developed.  ")
	print("")
	version=validateInput(1,3)
	print("")


	print("---")
	print("")	
	print( "  **Which way do you want to run this tool ?**  ")
	print("")
	print("  1 - Answer the questions one by one.  ")
	print("  2 - Use a text file with the answers already written.  ")
	print("")

	input_choice = validateInput(1,3)
	print("")

	# answer the qustions by hand
	if input_choice == 1:
		
		arqui(version)
		hasDB(version)

		authentication(version)
		userRegist(version)
		languages(version)
		inputForms(version)
		allowUploadFiles(version)
		# systemLogs()


		# users()
		# nameOfWebServer()


	# answers already written in the input file	
	else:
		print("---")
		print("")
		print("  **What is the name of the input file ?**  ")
		print("")
		readInputFromFile()

		'''
		for i in ( input_list[0].split(";") ):
			print ("{} is {}".format(i, type(i)))
		'''

		
		questions_and_answers["Q1"] = input_list[0]	
		questions_and_answers["Q2"] = input_list[1]
		questions_and_answers["Q3"] = input_list[2]
		questions_and_answers["Q4"] = input_list[3]
		questions_and_answers["Q5"] = input_list[4]
		questions_and_answers["Q6"] = input_list[5]
		questions_and_answers["Q7"] = input_list[6]
		questions_and_answers["Q8"] = input_list[7]
		questions_and_answers["Q9"] = input_list[8]
		questions_and_answers["Q10"] = input_list[9]
		questions_and_answers["Q11"] = input_list[10]



	'''
	# teste para mostrar no terminal o esquema
	designFile=open("design_schemes.txt", "r")
	design=designFile.read()
	print( design
	'''
	




#############################################################################################################

# Processing Information main function
def processingInformation():
	print("")
	print("Processing information.....")
	print("")

	printData()



	report = open("FINAL_REPORT.md", "w")
	report.write("# Final Report  " +'\n')
	report.write("\n")
	

	report.write("|	 |  | \n")
	report.write("| :-------- |:---------| \n")

	for i in range( 0,len(table_for_report) ):
		report.write("| " + table_for_report[i][0] + " | " + table_for_report[i][1] + " | \n" )
		

	report.write("\n")
	
	

	# constrution of the system model (achiteture)
	# file to write code that will design the schematics
	designFile = open("design_schemes.txt", "w")

	designFile.write("[.]")


	if questions_and_answers["Q1"].find("1") != -1:
		designFile.write("<-- -->[Client] <-- https --> [Server]")

	if questions_and_answers["Q1"].find("2") != -1:
		designFile.write("<-- -->[Web Service]")
	
	if questions_and_answers["Q1"].find("3") != -1:
		designFile.write("<-- -->[Desktop App]")

	if questions_and_answers["Q1"].find("4") != -1:
		designFile.write("<-- -->[Mobile]")
	
	if questions_and_answers["Q1"].find("5") != -1:
		designFile.write("<-- -->[Cliente Component]")
	
	if questions_and_answers["Q1"].find("6") != -1:
		designFile.write("<-- -->[Server Component]")
	
	if questions_and_answers["Q1"].find("7") != -1:
		designFile.write("<-- -->[API Service]")

	if questions_and_answers["Q1"].find("8") != -1:
		designFile.write("<-- -->[Embedded System]")

	# ---------------------------------------------------
	if questions_and_answers["Q2"].find("1") != -1:
		designFile.write("[.]<-- -->[Database]")


	 #designFile.write("<-- -->[..]")
	designFile.close()
	designWithGraphEasy()
	
	# escrever o esquema no report
	report.write("![alt text](design_schemes.png)")
	report.write("\n")
	report.write("\n")
	report.write("## Authentication  ")
	report.write("\n")
	report.write("**Authentication** is the process of verification that an individual, entity or website is who it claims to be. " +
	 			"Authentication in the context of web applications is commonly performed by submitting a user name or ID and one or " + 
				"more items of private information that only a given user should know. \n")

	report.write("\n")
	report.write("**User ID's**		\n" +
				"Make sure your usernames/userids are case insensitive.	\n" +
				"User 'smith' and user 'Smith' should be the same user.	\n" +
				"User names should also be unique. For high security applications usernames could be assigned and secret instead of user-defined public data.	\n" +
				"Email address as a USER ID.	\n")
	
	report.write("\n")
	report.write("**Password Length**		\n" +
				"Longer passwords provide a greater combination of characters and consequently make it more difficult for an attacker to guess.		\n"+
				"Minimum length of the passwords should be enforced by the application.		\n"+
				"Passwords shorter than 10 characters are considered to be weak		\n"+
				"Maximum password length should not be set too low, as it will prevent users from creating passphrases.	\n"+
				"Typical maximum length is 128 characters. \n")
	
	report.write("\n")
	report.write("**Password Complexity**		\n" +  
				"Applications should enforce password complexity rules to discourage easy to guess passwords.	\n" + 
				"Password mechanisms should allow virtually any character the user can type to be part of their password, " +  
				"including the space character. Passwords should, obviously, be case sensitive in order to increase their complexity.	\n\n" +  
				"The password change mechanism should require a minimum level of complexity that makes sense for the application and its user population.	\n\n" +
				" * Password must meet at least 3 out of the following 4 complexity rules	\n" + 
				" * at least 1 uppercase character (A-Z) \n" +
				" * at least 1 lowercase character (a-z) \n" +
				" * at least 1 digit (0-9) \n" +
				" * at least 1 special character (punctuation) space included \n" +
				" * at least 10 characters \n" +
				" * at most 128 characters \n" +
				" * not more than 2 identical characters in a row (e.g. 111 not allowed) \n" )
	
	report.write("\n")
	report.write("**Require Re-authentication for Sensitive Features**	\n" + 
				"In order to mitigate CSRF and session hijacking, it's important to require the current credentials for an account " +
				"before updating sensitive account information such as the user's password, user's email, or before sensitive transactions, " +
				"such as shipping a purchase to a new address. \n" )
	
	report.write("\n")
	report.write("**Authentication and Error Messages**	\n" + 
				"Incorrectly implemented error messages in the case of authentication functionality can be used for " +
				"the purposes of user ID and password enumeration. An application should respond (both HTTP and HTML) in a generic manner. \n"
				"An application should respond with a generic error message regardless of whether the user ID or password was incorrect. " + 
				"It should also give no indication to the status of an existing account. \n\n" + 
				"Incorrect Response Examples : \n\n" + 
				" * Login for User foo: invalid password \n"  +
				" * Login failed, invalid user ID \n" +
				" * Login failed; account disabled \n" +
				" * Login failed; this user is not active \n\n" +
				"Correct Response Example : \n\n " +
				" * Login failed; Invalid userID or password")
	
	# check if database is choosed


	report.write("\n")
	report.write("\n")
	report.write("## SQL Injection  ")
	report.write("\n")
	report.write(" An SQL injection attack consists of insertion or \"injection\" of either a partial or complete SQL query via " +
				"the data input or transmitted from the client (browser) to the web application. \n" +
				" SQL Injection flaws are introduced when software developers create dynamic database queries that include user " +
				" supplied input. To avoid SQL injection flaws is simple. Developers need to either: \n" +
				"a) stop writing dynamic queries; \n" +
				"b) prevent user supplied input which contains malicious SQL from affecting the logic of the executed query. \n\n" +
				"Primary Defenses: \n\n" +
				"* Option 1: Use of Prepared Statements (with Parameterized Queries) \n" + 
				"* Option 2: Use of Stored Procedures \n" +
				"* Option 3: White List Input Validation \n" +
				"* Option 4: Escaping All User Supplied Input \n\n" +
				"Additional Defenses: \n\n" +
				"* Also: Enforcing Least Privilege \n" +
				"* Also: Performing White List Input Validation as a Secondary Defense \n")


	# check if input forms is used
	
	report.write("\n")
	report.write("\n")
	report.write("##  Input Validation ")
	report.write("\n")
	report.write("**Input validation** is performed to ensure only properly formed data is entering the workflow in an information system, " +
				"preventing malformed data from persisting in the database and triggering malfunction of various downstream components. \n")
	report.write("\n")
	report.write("**Implementing input validation**	\n\n" + 
				" * Data type validators available natively in web application frameworks \n" +
				" * Validation against JSON Schema and XML Schema (XSD) for input in these formats. \n" +
				" * Type conversion (e.g. Integer.parseInt() in Java, int() in Python) with strict exception handling \n" +
				" * Minimum and maximum value range check for numerical parameters and dates \n" +
				" * Minimum and maximum length check for strings. \n" +
				" * Array of allowed values for small sets of string parameters (e.g. days of week). \n" +
				" * Regular expressions for any other structured data covering the whole input string (^...$) and not using \"any character\" wildcard (such as . or \\S) \n")


	report.write("\n")
	report.write("If it's well structured data, like dates, social security numbers, zip codes, e-mail addresses, etc. " +
				"then the developer should be able to define a very strong validation pattern, usually based on regular expressions, " +
				"for validating such input. \n " +
				"If the input field comes from a fixed set of options, like a drop down list or radio buttons, then the input needs " +
				"to match exactly one of the values offered to the user in the first place. \n" +
				"Free-form text, especially with Unicode characters, is perceived as difficult to validate due to a relatively "+
				"large space of characters that need to be whitelisted. \n"+
				"The primary means of input validation for free-form text input should be: \n\n" +

				" * Normalization: Ensure canonical encoding is used across all the text and no invalid characters are present. \n" +
				" * Character category whitelisting: Unicode allows whitelisting categories such as \"decimal digits\" or \"letters\" which " +
				" not only covers the Latin alphabet but also various other scripts used globally (e.g. Arabic, Cyryllic, CJK ideographs etc). \n" +
				" * Individual character whitelisting: If you allow letters and ideographs in names and also want to allow apostrophe ' for Irish names, but don't want to allow the whole punctuation category. \n")

	report.write("\n")
	report.write("**Client Side vs Server Side Validation**		\n" + 
				"Be aware that any JavaScript input validation performed on the client can be bypassed by an attacker that disables \n" +
				"JavaScript or uses a Web Proxy. Ensure that any input validation performed on the client is also performed on the server. \n") 

	report.write("\n")
	report.write("**Email Validation Basics**		\n" +
				" Many web applications do not treat email addresses correctly due to common misconceptions about what constitutes \n" +
				" a valid address. Specifically, it is completely valid to have an mailbox address which: \n\n" +
				" * Is case sensitive in the local portion of the address (left of the rightmost @ character). \n" +
				" * Has non-alphanumeric characters in the local-part (including + and @). \n" +
				" * Has zero or more labels. \n\n" +
				" Following RFC 5321, best practice for validating an email address would be to: \n\n" +
				" * Check for presence of at least one @ symbol in the address. \n" +
				" * Ensure the local-part is no longer than 64 octets. \n" +
				" * Ensure the domain is no longer than 255 octets. \n" +
				" * Ensure the address is deliverable. \n")


	report.write("\n")
	report.write("##  Cross Site Scripting (XSS)	\n" +
				" Given the way browsers parse HTML, each of the different types of slots has slightly different security rules. \n" +
				"When you put untrusted data into these slots, you need to take certain steps to make sure that the data " + 
				"does not break out of that slot into a context that allows code execution. \n\n" +
				"HTML entity encoding is okay for untrusted data that you put in the body of the HTML document, " +
				"such as inside a \"div\" tag. It even sort of works for untrusted data that goes into attributes, " +
				"particularly if you're religious about using quotes around your attributes. But HTML entity encoding  " +
				"doesn't work if you're putting untrusted data inside a \"script\" tag anywhere, or an event handler attribute  " +
				"like onmouseover, or inside CSS, or in a URL. \n" )
	
	report.write("\n")
	report.write("**XSS Prevention Rules**	\n\n" + 
				" * Never Insert Untrusted Data Except in Allowed Locations - The first rule is to deny all \n" +
				" * HTML Escape Before Inserting Untrusted Data into HTML Element Content \n" +
				" * Attribute Escape Before Inserting Untrusted Data into HTML Common Attributes \n" +
				" * JavaScript Escape Before Inserting Untrusted Data into JavaScript Data Values \n" +
				" * HTML escape JSON values in an HTML context and read the data with JSON.parse \n" +
				" * Ensure returned Content-Type header is application/json and not text/html.  \n" +
				" * CSS Escape And Strictly Validate Before Inserting Untrusted Data into HTML Style Property Values\n" +
				" * URL Escape Before Inserting Untrusted Data into HTML URL Parameter Values \n" +
				" * Sanitize HTML Markup with a Library Designed for the Job \n" +
				" * Prevent DOM-based XSS \n" +	
				" * Use HTTPOnly cookie flag \n" +
				" * Implement Content Security Policy \n" +
				" * Use an Auto-Escaping Template System \n" +
				" * Use the X-XSS-Protection Response Header \n" +
				" * Properly use modern JS frameworks like Angular (2+) or ReactJS \n")


	report.write("\n")
	report.write("## Access Control	\n" + 
				"Authorization is the process where requests to access a particular resource should be granted or denied. "+
				"It should be noted that authorization is not equivalent to authentication - as these terms and their definitions are frequently confused. \n" + 
				"Authentication is providing and validating identity. \n" +
				"Authorization includes the execution rules that determines what functionality and data the user " +
				"(or Principal) may access, ensuring the proper allocation of access rights after authentication is successful. \n\n" +
				"Web applications need access controls to allow users (with varying privileges) to use the application. They also need "+
				"administrators to manage the applications access control rules and the granting of permissions or entitlements to users and other entities. \n\n")

	
	report.write("\n")
	report.write("**Role Based Access Control (RBAC)**	\n" + 
				"Access decisions are based on an individual's roles and responsibilities within the organization or user base. " +
				"An RBAC access control framework should provide web application security administrators with the ability to "+
				"determine who can perform what actions, when, from where, in what order, and in some cases under what relational circumstances. \n\n"	+	
				"Advantages: \n\n"
				" * Roles are assigned based on organizational structure with emphasis on the organizational security policy \n" +
	    		" * Easy to use \n" +
	    		" * Easy to administer \n" +
	    		" * Built into most frameworks \n" +
	    		" * Aligns with security principles like segregation of duties and least privileges \n\n" +	
				"Problems: \n\n"	
				" * Documentation of the roles and accesses has to be maintained stringently. \n" +	
    			" * Multi-tenancy can not be implemented effectively unless there is a way to associate the roles with multi-tenancy capability requirements e.g. OU in Active 	Directory	\n" +
    			" * There is a tendency for scope creep to happen e.g. more accesses and privileges can be given than intended for. Or a user might be included in two roles if proper access reviews and subsequent revocation is not performed.\n" +
    			" * Does not support data based access control \n\n" +	
				"Areas of caution: \n\n"
				"* Roles must be only be transferred or delegated using strict sign-offs and procedures. \n" +	
	    		"* When a user changes his role to another one, the administrator must make sure that the earlier access is revoked such that at any given point of time, a user is assigned to only those roles on a need to know basis.  \n" +	
	    		"* Assurance for RBAC must be carried out using strict access control reviews. \n")


	report.write("\n")
	report.write("**Discretionary Access Control (DAC)** \n " +
				"is a means of restricting access to information based on the identity of users and/or membership in certain groups. "+			
				"Access decisions are typically based on the authorizations granted to a user based on the credentials he presented at the time of authentication. " +
				"The owner of information or any resource is able to change its permissions at his discretion. \n\n " +
				"Advantages: \n\n " +
				" * Easy to use \n " +
				" * Easy to administer \n " +
				" * Aligns to the principle of least privileges. \n " +
				" * Object owner has total control over access granted \n\n " +
				"Problems:  \n\n " +
				" * Documentation of the roles and accesses has to be maintained stringently. \n " +
				" * Multi-tenancy can not be implemented effectively unless there is a way to associate the roles with multi-tenancy capability requirements   \n " +
				" * There is a tendency for scope creep to happen e.g. more accesses and privileges can be given than intended for. \n\n " +
				"Areas of caution: \n\n " +
				" * While granting trusts \n " +
				" * Assurance for DAC must be carried out using strict access control reviews.\n")


	report.write("\n")
	report.write("**Mandatory Access Control (MAC)** \n" +
				"Ensures that the enforcement of organizational security policy does not rely on voluntary web application user compliance. " +
				"MAC secures information by assigning sensitivity labels on information and comparing this to the level of sensitivity a user is operating at." +
				"MAC is usually appropriate for extremely secure systems including multilevel secure military applications or mission critical data applications. \n\n" +
				"Advantages : \n\n" +
			    " * Access to an object is based on the sensitivity of the object \n" +
			    " * Access based on need to know is strictly adhered to and scope creep has minimal possibility \n" +
			    " * Only an administrator can grant access \n\n" +
				"Problems : \n\n" +
			    " * Difficult and expensive to implement \n" +
			    " * Not agile \n\n" +
				"Areas of caution : \n\n" +
			    " * Classification and sensitivity assignment at an appropriate and pragmatic level \n" +
			    " * Assurance for MAC must be carried out to ensure that the classification of the objects is at the appropriate level. \n")

	report.write("\n")
	report.write("**Permission Based Access Control**	\n" +
				"Is the abstraction of application actions into a set of permissions. " +
				"A permission may be represented simply as a string based name, for example \"READ\". " +
				"Access decisions are made by checking if the current user has the permission associated with the requested application action. \n\n" +
				"The has relationship between the user and permission may be satisfied by creating a direct relationship between the user " +
				"and permission (called a grant), or an indirect one. In the indirect model the permission grant is to an intermediate entity such as user group. \n\n"+
				"A user is considered a member of a user group if and only if the user inherits permissions from the user group.  " +
				"Systems that provide fine-grained domain object level access control, permissions may be grouped into classes. " +
				"The system can be associated with a class which determines the permissions applicable to the respective domain object. \n" +
				">In such a system a \"DOCUMENT\" class may be defined with the permissions \"READ\", \"WRITE\" and \"DELETE\"; a \"SERVER\" class may be defined with the permissions \"START\", \"STOP\", and \"REBOOT\". \n\n")

	
	report.write("\n")
	report.write("## Cryptography	\n" +
				"An architectural decision must be made to determine the appropriate method to protect data at rest. " +
				"There are such wide varieties of products, methods and mechanisms for cryptographic storage." +
				"The general practices and required minimum key length depending on the scenario listed below: \n\n" +				
				" * Key exchange: Diffie-Hellman key exchange with minimum 2048 bits \n" +
				" * Message Integrity: HMAC-SHA2 \n" +
				" * Message Hash: SHA2 256 bits \n" +
				" * Asymmetric encryption: RSA 2048 bits \n" +
				" * Symmetric encryption: AES 128 bits \n" +
				" * Password Hashing: Argon2, PBKDF2, Scrypt, Bcrypt \n\n"+
				"**Secure Cryptographic Storage Design:** \n\n" +
				" * All protocols and algorithms for authentication and secure communication should be well vetted by the cryptographic community. \n" +
				" * Ensure certificates are properly validated against the hostnames users  whom they are meant for. \n" +
				" * Avoid using wildcard certificates unless there is a business need for it \n" +
				" * Maintain a cryptographic standard to ensure that the developer community knows about the approved ciphersuits " +
				"for network security protocols, algorithms, permitted use, cryptoperiods and Key Management. \n" +
				" * Only store sensitive data that you need \n")
	
	report.write("\n")
	report.write("**Use strong approved Authenticated Encryption**		\n" +
	 			"CCM or GCM are approved Authenticated Encryption modes based on AES algorithm. \n\n" +
				"**Use strong approved cryptographic algorithms** \n\n" +
				"* Do not implement an existing cryptographic algorithm on your own, no matter how easy it appears. " +
				"* Instead, use widely accepted algorithms and widely accepted implementations.  \n " +
				"* Only use approved public algorithms such as AES, RSA public key cryptography, and SHA-256 or better for hashing. \n " +
				"* Do not use weak algorithms, such as MD5 or SHA1. \n " +
				"* Avoid hashing for password storage,instead use Argon2, PBKDF2, bcrypt or scrypt.  \n " +
				"* See NIST approved algorithms or ISO TR 14742 \"Recommendations on Cryptographic Algorithms or Algorithms\", " +
			 	"key size and parameters by  European Union Agency for Network and Information Security.  \n " +
				"* If a password is being used to protect keys then the password strength should be sufficient for the strength of the keys it is protecting.  " +
				"* When 3DES is used, ensure K1 != K2 != K3, and the minimum key length must be 192 bits .  \n" + 
				"* Do not use ECB mode for encrypting lots of data (the other modes are better because they chain the blocks of data together to improve the data security).\n")
	
	report.write("\n")
	report.write("**Use strong random numbers**	\n\n " +
	 			" * Ensure that all random numbers, especially those used for cryptographic parameters (keys, IV's, MAC tags), " +
				"random file names, random GUIDs, and random strings are generated in a cryptographically strong fashion. \n" +
	 			" * Ensure that random algorithms are seeded with sufficient entropy. \n" +
	 			" * Tools like NIST RNG Test tool can be used to comprehensively assess the quality of a Random Number Generator by \n" +
				"reading e.g. 128MB of data from the RNG source and then assessing its randomness properties with the tool. \n\n" +
	 			"The following libraries are considered weak random numbers generators and should not be used: \n\n" +
				"C library: random(), rand(), use getrandom(2) instead		\n" +
				"Java library: java.util.Random() instead use java.security.SecureRandom instead		\n" +
				"For secure random number generation, refer to NIST SP 800-90A. CTR-DRBG, HASH-DRBG, HMAC-DRBG are recommended	\n" )




	report.close()
	convertReport()

	
 	


if __name__ == "__main__":

	print("---")
	print("")
	print("#  Welcome to ")
	print("")
	print("#  SECURiotPRACTICES")
	print("")
	print ("  The **SECURiotPRACTICES** is a custom made program.") 
	print("  This program implements a questionnaire about the development")
	print("  of a system and generate a report with secure development guides.")
	print("  It is part of the outputs of project Project SECURIoTESIGN, with funding  ")
	print("  with funding by FCT-Fundação para a Ciência e Tecnologia (Portugal)  ")
	print("  through the research grant SFRH//BD//133838//2017.")
	print("")
	print("## License")
	print("")
	print("  Developed by Edi Aires and Pedro R. M. Inácio")
	print("  Department of Computer Science")
	print("  Universidade da Beira Interior")
	print("")
	print("  Copyright 2019 Edi Aires and Pedro R. M. Inácio")
	print("")
	print("  SPDX-License-Identifier: Apache-2.0")
	print("")

	
	informationCapture()
	processingInformation()	


	print("")
	print("#############################################################") # after this is for debugging xD

	print("")
	print("")
	print("")

	
	
	exit(1)


# license Apache-2.0
