# Moududur "Moody" Rahman
# SoftDev1 pd2
# K10 -- Jinja Tuning
# 2019-09-21




from flask import Flask, render_template
import csvtest
import csv
from googlesearch import search

app = Flask(__name__)



allrows = []

with open("static/occupations.csv") as csvfile:  #reads file for the html table
    readCSV = csv.reader(csvfile, delimiter=",")
    for row in readCSV:
        allrows.append(row)



@app.route("/")     # this is the "homepage"
def hello_world():
    print(__name__) # Printed onto console on refresh
    return '''<a href="/occupyflaskst">click here for 10_occ !!</a> <br>
                <a href="/jeff">old index page</a> <br>
                <a href="/my_foist_template">jinja test</a> <br>
            '''

@app.route("/jeff")   #testing a dumb method to read html
def jeff():
    print(__name__)
    return open("./static/index.html").read()

@app.route("/goog")
def googtest():
    print(__name__)
    x = [next(search(x, num=1, stop=1, pause=.01)) for x in [y for y in allrows[0]] ]
    out = ""
    for z in x:
        out += (z + ", ")
    return out

@app.route("/a")
def a():
    print(__name__)    # dont go here
    return csvtest.allrows   #this is just me playing around lmao


@app.route("/my_foist_template")
def disp():
    print(__name__) # Printed onto console on refresh
    coll = [0, 1,2, 3,4, 5]
    return render_template( "tempp.html", username = "doof")   #jinja attempt one!


@app.route("/occupyflaskst")
def hw1():

    print(__name__) # Printed onto console on refresh
    #twat is a 2d array of the jobs
    #.getjob() is an imported function to return the weighted randomly chosen job
    return render_template( "occupation.html", jobinp = csvtest.getjob(), twat = allrows[1:])



if __name__ == "__main__":
    app.debug = True
    app.run()
