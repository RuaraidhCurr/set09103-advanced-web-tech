from flask import Flask, redirect, url_for, abort
app = Flask(__name__)

@app.route("/")
def root():
	return "The default, 'root' route!"

# THIS SHOWS ME HOW TO REDIRECT A USER

@app.route("/private")
def private():
    #test for user logged in failed
    #so redirect to login url
    return redirect(url_for("login"))

@app.route("/login")
def login():
    return "Now we would get username & password"

# This section will show me how to create my own error page
@app.errorhandler(404)
def page_not_found(error):
    return "Couldnt find the page you requested.", 404

# This section shows us how to use the abort function
# can be used to force all error types (400, 401, 403, 404, 500, 502, 503, 504)
# Should impliment a custome page for each error message (Good Practise)
@app.route("/force400")
def force400():
    abort(400)

# intoducing a static folder to hold things like css etc
@app.route("/static-examples/img")
def static_examples_img():
    start = '<img src="'
    url = url_for("static", filename="vmask.jpg")
    end = '">'
    return start+url+end, 200

if __name__ == "__main__":
    app.run("127.0.0.1", debug=Ture)
