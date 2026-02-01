# We will see how to integrate Flask with html.

# Basic Structure.

# SO we can use html inside it also life it.
# def welcome():
    ###     return "<html> <h1> Welcome to Flask Integration. </h1> </html>"


# We want we import new html file and import it in our program.
    ###     we also import "render_tempalte"


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html> <h1> Welcome to Flask Integration. </h1> </html>"

@app.route("/index")
def index():
    return render_template("index.html" ) 
    
    
    ##We use jihnge-2 template and this heplp in navigation and execute to this render_template().

    ## So we will create a folder name "templates" amd that Jinga-2 navigate to that particular folder whose name is "template" and search file.

if __name__ == "__main__":
    app.run(debug= True)