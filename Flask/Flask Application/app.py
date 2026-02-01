## Install flask-> pip install flask.


from flask import Flask

'''

It creates an instanec of the Flask class,
which will be your WSGI(Web Server Gateway Interface) application.

'''

# 1st Step.


# WSGI Application.

app = Flask(__name__) # Instance of the flask and entry point. 

@app.route("/")# It is decorator.  # / is home page.○

def welcome():
    return "Welcome to this Flask  cource. This should be an amazing cource." 

if __name__ == "__main__":
    # This is entry point for any .py file.
    # Here execution start.

    app.run(debug= True) # This flask application will run.Automatically run and show changes.
    # host-> You can set host.

'''
This is running on Host.
'''


'''
So when we are enter / so it goes to @app.route("/") and return message.
'''

'''
So for display change you have to restart surver. Ctrl + Alt + n
'''