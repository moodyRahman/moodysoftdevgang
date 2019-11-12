from flask import Flask, escape, request, render_template
import urllib3
import json

app = Flask(__name__)
@app.route('/')
def hello():
	print(__name__)
	return render_template("img.html", image = "")

if __name__ == '__main__':
	app.debug = True app.run()
