from flask import Flask, request, render_template
app = Flask(__name__)

# allows us to pass variables from our python into our html templates
@app.route("/profile/<username>")
def profile(username):
    return render_template("profile.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)