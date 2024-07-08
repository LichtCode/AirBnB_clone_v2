#!/usr/bin/python3
""" creating an html with flask
1. the server listens on 0.0.0.0 on port 5000
2. routs / - display 'Hello HBNB!
3. route /hbnb - dispay 'hbnb '
"""

from flask import Flask

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def display():
    """ the root of the wed page"""

    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnd():
    """the /hbnb page of the server"""

    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)
