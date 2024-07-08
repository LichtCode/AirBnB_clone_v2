#!/usr/bin/python3
""" creating an html with flask
1. the server listens on 0.0.0.0 on port 5000
2. routs / - display 'Hello HBNB!
3. route /hbnb - dispay 'hbnb '
4. create a /c/<text> route - display the text on the page
"""

from flask import Flask

app = Flask("__name__")

# task 0


@app.route("/", strict_slashes=False)
def display():
    """ the root of the wed page"""

    return 'Hello HBNB!'

# task 1


@app.route("/hbnb", strict_slashes=False)
def hbnd():
    """the /hbnb page of the server"""

    return 'HBNB'

# task 2


@app.route("/c/<text>",  strict_slashes=False)
def c_text(text):
    """ (replace underscore _ symbols with a space)"""

    formated_text = text.replace('_', ' ')
    return "C {}".format(formated_text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)
