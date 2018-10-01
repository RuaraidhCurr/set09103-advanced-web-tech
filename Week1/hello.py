from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
	return "The default, 'root' route"

@app.route("/hello/")
def hello_world():
	return "Hello Napier!!"

@app.route("/goodbye/")
def goodbye():
	return "Inabit"
