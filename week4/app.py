from flask import Flask, request, template_rendered, url_for
import os
app = Flask(__name__)

@app.route("/")
def root():
    return "The default, 'route' route"

@app.route("/account/", methods=["GET", "POST"])
def accounts():
    if request.method == "POST":
        print request.form
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        name = firstname + " " + lastname
        username = firstname + lastname[:4]
        age = request.form["age"]
        return "Users Name: %s <br>  Username: %s <br> Users age: %s" %(name, username, age)
    else:

        #small user input form asking for name then 
        page ='''
        <html><body>
            <form action="" method="post" name="form">

                <label for="name">First Name:</label><br>
                <input type="text" name="firstname" id="name"/><br>

                <label for="name">Last Name:</label><br>
                <input type="text" name="lastname" id="name"/><br>

                <label for="name">Age:</label><br>
                <input type"text" name="age" id="age"/><br>

                <input type="submit" name="submit" id="submit"/>
            </form>
        </body></html>
        '''
        return page

@app.route("/wagwan/<name>")
def wagwan(name):
    return "wagwan %s" % name

#allows user to enter ?name="name" to make valid search params
@app.route("/hello/")
def hello():
    name = request.args.get("name", "")
    if name == "":
        return "No Search Params given"
    else:
        return "Hello %s" %name


#FILE UPLOAD!
@app.route("/upload/", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        f = request.files["datafile"]
        if not os.path.exists("static/uploads"):
            os.makedirs("static/uploads")
            f.save("static/uploads/upload.png")
        else:
            f.save("static/uploads/upload.png")

        return "File Uploaded!"
    else:
        page='''
        <html><body>
        <form action="" method="post" name="form" enctype="multipart/form-data">
            <input type="file" name="datafile"  />
            <input type="submit" name="submit" id="submit"  />
        </form>
        </body></html>
        '''
        return page, 200

#FILE DISPLAY
@app.route("/display/")
def display():
    return "<img src='"+url_for("static", filename="uploads/upload.png")+"'/>"


if __name__=="__main__":
    app.run(debug=True)