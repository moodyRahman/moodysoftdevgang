# Moududur "Moody" Rahman, Hillary Zen
# SoftDev1 pd2
# K10 -- Jinja Tuning
# 2019-09-21





from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

allpasswords = {"hillary": "moody"}



@app.route("/")
def home():
	return "<a href='/login'>click here for login</a> <br>"

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/auth")
def auth():
	if request.args['name'] == 'hillary':
		if request.args['password'] == 'moody':
			return redirect("/welcome")
		else:
			return redirect('/login')
	else:
		return redirect('/login')

@app.route("/welcome")
def welcome():
	return "Hello"

if __name__ == "__main__":
    app.debug = True
    app.run()
