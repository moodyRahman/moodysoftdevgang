#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O
import sys

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

studf = open("students.csv", "r")
coursesf = open("courses.csv", "r")

stud = csv.DictReader(studf)
courses = csv.DictReader(coursesf)


def run():

	# for row in stud:
	#     command = "INSERT INTO students VALUES('{}', '{}', '{}')".format(row["name"], row["age"], row["id"])
	#     c.execute(command)
	#
	# for row in courses:
	#     command = "INSERT INTO courses VALUES('{}', '{}', '{}')".format(row["code"], row["mark"], row["id"])
	#     c.execute(command)

	command = "SELECT * FROM students"
	allstudents = c.execute(command).fetchall()
	for stud in allstudents:
		command = "SELECT * FROM courses WHERE id = {};".format(stud[2])
		classes = c.execute(command).fetchall()
		s = ("HELLO I AM {}, OF ID {} AND I AM TAKING {}").format(stud[0], stud[2], [x[0] for x in classes])
		print(s)
		# for z in classes:
		cumsum = 0
		for cl in classes:
			cumsum += cl[1]
		sss = ("MY AVERAGE IS {}").format(round(cumsum / len(classes), 2))
		print(sss)
		print("")



	command = ""          # test SQL stmt in sqlite3 shell, save as string
	c.execute(command)    # run SQL statement

	db.commit() #save changes
	db.close()  #close database

def lookup(student):
	command = "SELECT * FROM students WHERE name = '{}'".format(student)
	c.execute(command)
	stud = c.fetchall()
	s =  '''
	HELLO I AM {}, AGE {}
	'''.format(stud[0], stud[2])

if __name__ == '__main__':
	while True:
		z = input("what u want: ")
		z = z.split(" ")
		if z[0] == "allstudents":
			run()
			sys.exit(1)
		elif z[0] == "lookup":
			lookup(z[1])
