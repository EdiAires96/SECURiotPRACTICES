#!/usr/bin/python coding=utf-8

# Author : Édi Aires

# Work in Progress ...
# TO-DO -> generate a input file with the answers in the final of the questionnarie ; constrution of the final report

import os
from markdown import markdown
from xhtml2pdf import pisa
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


version = 1
list = []
input_list = []

newFile = open("design_schemes.txt", "a+")



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
	"2" : "Confidential Data ",
	"3" : "Critical Data ",
	"4" : ""
}

question_6 = {
	"1" : "No Authentication",
	"2" : "Username and Password",
	"3" : "Social Networks / Google",
	"4" : "SmartCard",
	"5" : "Biometrics",
	"6" : "Two Factor Authentication ",
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
	"1" : "User Activity ",
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

			# print file line
			# print (line.strip() )

			input_list.append(line.strip())
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
			question_1["9"] = str(value2)

		list.append("Q1-" + str(value))

		questions_and_answers["Q1"]=questions_and_answers["Q1"] + str(value) + ";"
		


		# processing...

		if value == 1:
			newFile.write("[Client] <-- https --> [Server]")	
		if value == 3:
			newFile.write("<-- -->[Desktop App]")
		if value == 4:
			newFile.write("<-- -->[Mobile]")
		if value == 6:
			newFile.write("<-- -->[Server]")


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
	list.append("Q2-" + str(value))
	questions_and_answers["Q2"]=str(value)
	
	
	if value == 1:
		# readAndWriteFile("data_ascii.txt")
		newFile.write("<-- -->[Database]")
		typeOfDatabase(version)
		whichDatabase(version)
		sensitiveData(version)
	else:
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
	list.append("Q3-" + str( value ) )
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
		# TO-DO change this funtion input
		value=validateInput(2)
	
	list.append("Q4-" + str(value))
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

	# list.append("Q5-" + str(value))
	
	while(1):
		value=validateInput(1,5)
		if value == 0:
			return 
		if value == 4 :
			print( "  Please specify the architeture: (name between quotes)  ")
			# TO-DO change this funtion input
			value2=validateInput(2)
			question_5["4"] = str(value2)

		list.append("Q5-" + str(value))
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
	list.append("Q6-" + str( value ))
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

	list.append("Q7-" + str(value))
	questions_and_answers["Q7"]=str(value)

	if value == 1 :
		typeOfUserRegist(version)


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
	list.append("Q8-" + str( value ))
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
			question_9["8"]  = str(value2)

		list.append("Q9-" + str(value))
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
	list.append("Q10-" + str(value))
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
	list.append("Q11-" + str( value ))
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
	list.append("Q12-" + str( value ))
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
'''


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
	print( cmd)
	# cmd2 = "graph-easy --as=ascii " + sInput + " > " + sOutput + ".txt")
	# print( cmd2
	
	os.system(cmd)
	# os.system(cmd2)

	# convert img svg to PNG
	drawing = svg2rlg("design_schemes.svg")
	renderPM.drawToFile(drawing, "design_schemes.png", fmt="PNG")


# ----------------------------------------------------------------------------
# function to convert the markdown report to html and pdf format
def writeReport():
	input_filename = ("guides/example_report.md")
	# input_filename = "some_markdown.md")

	output_filename = ("report99.html")

	with open(input_filename,"r") as f:
		html_text = markdown(f.read())


	out= open(output_filename,"w")
	out.write(html_text)

	# writing in pdf file, the html content

	resultFile = open("report99.pdf", "w+b")
	pisastatus = pisa.CreatePDF(html_text, dest=resultFile)
	print( pisastatus)


# ----------------------------------------------------------------------------
def printData():

	list_aux = []	
	# it is a multiple question
	for n in question_1:

		# cut the string in the delimitator ";" 
		aux = questions_and_answers["Q1"].split(";")

		#delete last item (= None)
		aux = aux[:-1]
		#print(aux)

		
		for i in aux:
			#print(n + " : " + question_1[n])
			item = i		
			if  item == n:
				list_aux.append( question_1[n] )
	
	#print("Architeture {:>18} ".format(":     ") + ' ; '.join(list_aux))
	print("{:25} {:3} {:40} ".format("Architeture", ":", ' ; '.join(list_aux) ) )

	
	# --------------------------------------------
	for n in question_2:
		item = questions_and_answers["Q2"]		
		if  item == n:
			# print( "Has DB {:>18} ".format(":     ") + question_2[n])
			print("{:25} {:3} {:40} ".format("Has DB", ":" , question_2[n]) ) 


	# --------------------------------------------
	for n in question_3:
		item = questions_and_answers["Q3"]		
		if  item == n:
			print( "{:25} {:3} {:40} ".format("Type of data storage", ":",  question_3[n]) )


	# --------------------------------------------
	for n in question_4:
		item = questions_and_answers["Q4"]		
		if  item == n:
			print("{:25} {:3} {:40} ".format( "Which DB", ":", question_4[n]) )


	# --------------------------------------------
	list_aux = []	
	# it is a multiple question
	for n in question_5:

		# cut the string in the delimitator ";" 
		aux = questions_and_answers["Q5"].split(";")

		#delete last item (= None)
		aux = aux[:-1]
		#print(aux)

		
		for i in aux:
			#print(n + " : " + question_1[n])
			item = i		
			if  item == n:
				list_aux.append( question_5[n] )
	
	print("{:25} {:3} {:40} ".format("Type of data stored" , ":" , ' ; '.join(list_aux) ) )


	# --------------------------------------------
	for n in question_6:
		item = questions_and_answers["Q6"]		
		if  item == n:
			print("{:25} {:3} {:40}".format("Authentication", ":" , question_6[n]) )


	# --------------------------------------------
	for n in question_7:
		item = questions_and_answers["Q7"]		
		if  item == n:
			print("{:25} {:3} {:40}".format("User Registration", ":" , question_7[n]) )


	# --------------------------------------------
	for n in question_8:
		item = questions_and_answers["Q8"]		
		if  item == n:
			print("{:25} {:3} {:40} ".format("Type of Registration", ": " , question_8[n]) )


	# --------------------------------------------
	list_aux = []	
	# it is a multiple question
	for n in question_9:

		# cut the string in the delimitator ";" 
		aux = questions_and_answers["Q9"].split(";")

		#delete last item (= None)
		aux = aux[:-1]
		#print(aux)

		
		for i in aux:
			#print(n + " : " + question_1[n])
			item = i		
			if  item == n:
				list_aux.append( question_9[n] )
	
	print("{:25} {:3} {:40} ".format("Programming Languages" , ":" , ' ; '.join(list_aux) ) )


	# --------------------------------------------
	for n in question_10:
		item = questions_and_answers["Q10"]		
		if  item == n:
			print("{:25} {:3} {:40} ".format("Input Forms" , ":" , question_10[n]) )


	# --------------------------------------------
	for n in question_11:
		item = questions_and_answers["Q11"]		
		if  item == n:
			print("{:25} {:3} {:40} ".format("Upload Files" , ":" , question_11[n]) )



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
		aux =[]
		aux2=[]

		for i in ( list[0].split(";") ):
			print (i)
			aux.append(i)

		# print(aux)

		for i in ( list[8].split("-") ):
			print (i)
			aux2.append(i)

		first_element = aux2[0]
		rest_elements = aux2[1:]
		print (aux2)
		print (first_element)
		print (rest_elements)
		'''






	# print(list)
	# for p in list: print p


	'''
	# teste para mostrar no terminal o esquema
	newFile=open("design_schemes.txt", "r")
	design=newFile.read()
	print( design
	'''
	newFile.close()




#############################################################################################################

# Processing Information main function
def processingInformation():
	print("")
	print("Processing information.....")
	print("")


	designWithGraphEasy()
	
	# escrever o esquema no report
	f2=open("guides/example_report.md","a")
	# f2.write("![alt text](design_schemes.png)")
	f2.write("![alt text](design_schemes.png)")
	f2.close()
	

	writeReport()


	# after have finished answering all the questions
	# generate a file with the answers

 




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
	# processingInformation()	


	print("")
	print("#############################################################") # after this is for debugging xD



	# for x, y in questions_and_answers.items():
  	#	print(x, y) 

	print("")
	for i in questions_and_answers:
  		# print(i + "    -> " + questions_and_answers[i])
		# print("{:<10s}{:>4s}{:^12s}".format(i,"->",questions_and_answers[i] ))
		print("{:7} {:4} {:10}".format(i,"->",questions_and_answers[i] ))

	print("")
	print("")
	print("")


	printData()

	generate_file = open("ans.txt", "w")
	for i in questions_and_answers:
		generate_file.write(questions_and_answers[i] +'\n')
	generate_file.close()



	



	exit(1)


# license Apache-2.0
