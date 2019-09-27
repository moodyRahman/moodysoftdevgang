# Moududur "Moody" Rahman
# SoftDev1 pd2
# K10 -- Jinja Tuning
# 2019-09-21





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
    print("######")
    print(request)
    print("#####")
    print(request.args)
    print("####")
    print(request.form)
    print("###")
    print(request.headers)
    return ("you wrote " + request.args["name"])


@app.route("/cond")
def condtest():
    if len(request.args) == 0:
        return render_template("roop.html")
    else:
        return ("you wrote "+request.args["name"])


if __name__ == "__main__":
    app.debug = True
    app.run()


