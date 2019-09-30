# Moududur "Moody" Rahman and Hannah Fried
# SoftDev1 pd2
# K12 -- Echo Echo Echo
# 2019-09-25





from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/foo")
def reeee():
    print(__name__)
    print(app)
    print(request.args)
    return render_template("foop.html")

@app.route("/frick")
def twoo():
    print(__name__)
    print(app)
    print(request.args)
    return request.args["name"]

# @app.route("/")
# def landing():
#     return render_template("d.html")

@app.route("/")
def landing():
    return render_template("foop.html")

@app.route("/auth")
def auth():
    if "name" in request.args:
        return render_template("auth.html", header = request.headers, uname = request.args["name"], method = request.method)
    else:
        return render_template("foop.html")





if __name__ == "__main__":
    app.debug = True
    app.run()
