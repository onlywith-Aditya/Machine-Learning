### Building URL Dynamically.
### Variable Rule.
### Jinja-2 Template Engine.


from flask import Flask, request, render_template

# app = Flask(__name__)

# @app.route("/")
# def welcome_1():
#     return None

# @app.route("/index")
# def welcome_2():
#     return None

# @app.route("/success/<score>") # Normal String
# #@app.route("/success/<int: score>") # Strict Int
# def success(score):
#     return f"The marks you got is {score}" 




# if __name__ == "__main__":
#     app.run()


### Building URL Dynamically.

app = Flask(__name__)

@app.route("/")
def welcome_1():
    return "Hey_Page-1"

@app.route("/index")
def welcome_2():
    return "Hey_Page-2"

#@app.route("/success/<score>") # Normal String
@app.route("/success/<int:score>") # Strict Int
def success(score):
    res = ""
    if score > 50:
        res = "Pass"
    else:
        res = "Fail"

    return render_template("result.html", results = res)




if __name__ == "__main__":
    app.run(debug=True)


### Jinja-2 Template Engine.
'''

{{  }} | Expression to print output in html.
{%...%} | Conditional statement.
{#...#} | Comments.

'''