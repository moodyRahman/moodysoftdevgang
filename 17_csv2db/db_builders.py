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

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >


studf = open("students.csv", "r")
coursesf = open("courses.csv", "r")


stud = csv.DictReader(studf)
courses = csv.DictReader(coursesf)

# c.execute("CREATE TABLE students(name STRING, age INTEGER, id INTEGER);")
# c.execute("CREATE TABLE courses(code STRING, mark INTEGER, id INTEGER);")

for row in stud:
    # val = []
    # val.append(row["name"])
    # val.append(row["age"])
    # val.append(row["id"])
    # print(val)
    command = "INSERT INTO students VALUES('{}', '{}', '{}')".format(row["name"], row["age"], row["id"])
    c.execute(command)
    # c.execute("INSERT INTO students VALUES('mood', '13', '15')")
    # c.execute("INSERT INTO students VALUES(" + row["name"] + "," + row["age"] + ","+ row["id"]+ ");")

for row in courses:
    # val = []
    # val.append(row["name"])
    # val.append(row["age"])
    # val.append(row["id"])
    # print(val)
    command = "INSERT INTO courses VALUES('{}', '{}', '{}')".format(row["code"], row["mark"], row["id"])
    c.execute(command)
    # c.execute("INSERT INTO students VALUES('mood', '13', '15')")
    # c.execute("INSERT INTO students VALUES(" + row["name"] + "," + row["age"] + ","+ row["id"]+ ");")

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
