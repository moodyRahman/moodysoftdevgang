# Moududur "Moody" Rahman, Hillary Zen
# SoftDev1 pd2
# K10 -- Jinja Tuning
# 2019-09-21





from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash


app = Flask(__name__)
app.secret_key = 'hfjkafhrku'

allpasswords = {"hillary": "moody"}


# we start from the root directory
# test the existence of username and if it's "hillary"
# if so go to welcome (this only happens w active hillary session)
# otherwise go to login
@app.route("/")
def home():
	print("######")
	if 'username' in session:
		if session['username'] == 'hillary':
			return redirect('/welcome')
	return redirect('/login')


@app.route("/error")
def error():
	return "<a href='/'>ya doofed up <br> welcome to ur error page</a> <br>"

# render login depending on user at hand
@app.route("/login")
def login():
	if "username" in session:
		return render_template("login.html", uname = session["username"])
	return render_template("login.html", uname = "no one")

# from the login form, if there is a key called name
# check if name is hillary and password is Moody
# password has to exist to reach here is via login only
#
# the only other way is via the logout buttonbcbcvbcvbcvbvcb
# which fails the first cond and pops the user

@app.route("/auth")
def auth():
	if "name" in request.args:
		if request.args['name'] == 'hillary':
			if request.args['password'] == 'moody':
				session["username"] = "hillary"
				flash("log in successful!")
				return redirect("/welcome")
			else:
				return redirect("/login")
		else:
			return redirect("/login")
	else:
		session.pop("username", None)
		return redirect("/welcome")

@app.route("/welcome")
def welcome():
	if "username" in session:
		if session['username'] == "hillary":
			return render_template("welcome.html", uname = session["username"])
		else:
			return "You're not supposed to be here"
	return redirect("/login")

if __name__ == "__main__":
    app.debug = True
    app.run()
