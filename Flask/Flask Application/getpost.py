# Basic Flask Structure.

from flask import Flask, render_template,request

app = Flask(__name__)



@app.route("/") # Attribute {Option-> Method-> Get/Post.}
def welcome_1():
    return render_template("index.html")

# Get Request.

@app.route("/about", methods = ["GET"]) 
def welcome_2():
    return render_template(["about.html"])

# Get and Post Both Request.

@app.route("/form", methods = ["POST", "GET"]) 
def welcome_3():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello {name}"
        # This section is used to handle user information.
    return render_template(["form.html"])



if __name__ == "__main__":
    app.run(debug= True)

