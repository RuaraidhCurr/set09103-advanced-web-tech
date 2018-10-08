from flask import Flask, request, template_rendered, render_template, url_for
import os
app = Flask(__name__)

@app.route("/")
def root():
    return "The default, 'route' route"


# all of the following routes will all go to the index.html
@app.route("/index/")
@app.route("/index/<name>")
@app.route("/index/<name>/<age>")
def index(name=None, age=None):
    user = {"name": name, "age": age}
    currentusers = [{"name": "bob", "age": "34"},
                    {"name": "jeff", "age": "23"}, 
                    {"name": "jessica", "age": "54"}]
    return render_template("index.html", user=user, currentusers=currentusers)

if __name__=="__main__":
    app.run(debug=True)