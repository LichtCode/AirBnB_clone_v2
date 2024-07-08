#!/usr/bin/python3
""" creating an html with flask
1. the server listens on 0.0.0.0 on port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def display():
    """ the root of the wed page"""

    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)
