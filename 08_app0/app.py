from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    print(__name__)
    return "<a href='/mood'>link text</a>"
def noot():
    return "peepoo in my drawer"


@app.route("/doof")
def remy():
    print(__name__)
    return "oh? you're approaching me"


@app.route("/mood")
def bb():
    print(__name__)
    return "i cant beat your ass if you're not closer"


@app.route("/static")
def aa():
    print(__name__)
    return open("./static/index.html").read()

if __name__ == "__main__":
    app.debug = True
    app.run()
