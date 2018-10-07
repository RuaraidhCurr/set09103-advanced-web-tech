from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Method used: %s" % request.method

#allows different request methods see below
@app.route("/pst", methods=["GET", "POST"])
def pst():
    if request.method == "POST":
        return "you are using POST"
    else:
        return "you are probably using GET"

if __name__ == "__main__":
    app.run(debug=True)