#!/usr/bin/python3
"""Starts a Flask web application
"""
from flask import Flask


if __name__ == '__main__':
    app = Flask(__name__)


    @app.route('/', strict_slashes=False)
    def index():
        """Display 'Hello HBNB!'
        """
        return 'Hello HBNB!'


    app.run('0.0.0.0')
