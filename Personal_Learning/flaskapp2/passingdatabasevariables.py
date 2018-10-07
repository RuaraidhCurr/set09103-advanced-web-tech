from flask import Flask, request, render_template, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return "Home Page"

posts = [
    {
        "author": "Ruaraidh Curran",
        "title": "First Dummy",
        "content": "Wagwan",
        "date_posted": "07/10/2018"
    },
    {
        "author": "Ruaraidh Curran",
        "title": "Second Post",
        "content": "wagwan2",
        "date_posted": "08/10/2018"
    },
    {
        "author": "Ruaraidh Curran",
        "title": "Third Post",
        "content": "wagwan3",
        "date_posted": "09/10/2018"
    },
]

@app.route("/articles")
def articles():
    return render_template ("articles.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

if __name__ == "__main__":
    app.run(debug=True)