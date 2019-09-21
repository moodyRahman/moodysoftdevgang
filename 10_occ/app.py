# Moududur "Moody" Rahman
# SoftDev1 pd2
# K10 -- Jinja Tuning
# 2019-09-21




from flask import Flask, render_template
import csvtest
import csv

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__) # Printed onto console on refresh
    return "poopoopeepee"

@app.route("/jeff")
def jeff():
    print(__name__)
    return open("./static/index.html").read()

@app.route("/my_foist_template")
def disp():
    print(__name__) # Printed onto console on refresh
    coll = [0, 1,2, 3,4, 5]
    return render_template( "tempp.html", username = "doof")


@app.route("/occupyflaskst")
def hw1():
    allrows = []

    with open("static/occupations.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        for row in readCSV:
            allrows.append(row)

    print(__name__) # Printed onto console on refresh
    return render_template( "occupation.html", jobinp = csvtest.reee(), twat = allrows)



if __name__ == "__main__":
    app.debug = True
    app.run()
