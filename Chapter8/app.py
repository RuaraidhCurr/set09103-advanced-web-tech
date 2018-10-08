from flask import Flask, request, template_rendered, render_template, url_for
import os
app = Flask(__name__)

@app.route("/")
def root():
    return "The default, 'route' route"

@app.route("/index/")
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)