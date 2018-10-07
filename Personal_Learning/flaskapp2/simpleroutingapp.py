from flask import Flask

app = Flask(__name__)

# tying a url from your website to a python function "@ signifies a decorator"
# -connecting a url to the return value-
@app.route("/")
def index():
    return "Home"

#defines a new page
@app.route("/first")
def first():
#return function can accept html!    
    return "<h1>Hello</h1>"

#when you want to pass a variable in the url the var needs to be in "< >" see below
@app.route("/profile/<username>")
def profile(username):
    return "wagwan %s" % username

#using any other variable type (anything other than a string value) within url 
@app.route("/article/<int:post_id>")
def article(post_id):
    return "Article ID: %s" % post_id

#starts app only if this file is called directly
if __name__ == "__main__":
    app.run(debug=True)