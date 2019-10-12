#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

studf = open("students.csv", "r")
coursesf = open("courses.csv", "r")


stud = csv.DictReader(studf)
courses = csv.DictReader(coursesf)


for row in stud:
    command = "INSERT INTO students VALUES('{}', '{}', '{}')".format(row["name"], row["age"], row["id"])
    c.execute(command)

for row in courses:
    command = "INSERT INTO courses VALUES('{}', '{}', '{}')".format(row["code"], row["mark"], row["id"])
    c.execute(command)


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

db.commit() #save changes
db.close()  #close database
