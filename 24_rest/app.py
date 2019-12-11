from flask import Flask, escape, request, render_template
import urllib3
import json

app = Flask(__name__)
@app.route('/')
def hello():
    print(__name__)

    http = urllib3.PoolManager()
    response = http.request(
        'GET', "https://api.nasa.gov/planetary/apod?api_key=XZwpcj1OVbMqNtKpVeQu7RDu1yrZ1gjyNxJyEe7c")
    dat = response.data

    print(dat)

    link = json.loads(dat)["url"]
    expl = json.loads(dat)["explanation"]

    return render_template("img.html", image=link, explanation=expl)


if __name__ == '__main__':
    app.debug = True
    app.run()
