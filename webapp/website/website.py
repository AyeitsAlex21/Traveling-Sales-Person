"""
Flask-Login and Flask-WTF example
website.py
Source Code for Flask-Login and Flask-WTF or intereaction between Front-end and Genetic Algorithm/Google Maps API
Author(s): Kale Satta-Hutton, Anna Nguyen
NASAK CIS422 FA21
Last Modifed Date: 10/31/21
Description:
  This file contains two routes. The first route renders base.html when the user first navigates to the landing page.
  The second function, _min_path, gets the array of locations passsed in from the UI containing the place name, place 
  location (longitude, latitude) and place ID. This will be passed to the web app API to be processed by the GenAlgo.
"""
import flask
import jsons
from urllib.parse import urlparse, urljoin
from flask import (Flask, request, render_template, redirect, url_for, flash,
                    abort, session)
from flask_wtf import FlaskForm as Form
from wtforms import BooleanField, StringField, validators
from flask import Flask, render_template, request
import requests # allows the sending of HTTP requests


app = flask.Flask(__name__) # creates Flask instance

app.config.from_object(__name__) # import configuration into Flask instance

# Binds index function to base URL and renders template
@app.route("/")
def index():
    return render_template("base.html")

# Binds _min_path function to URL. 
@app.route("/_min_path", methods=["GET"])
def _min_path():
    """

    """
    # app.logger.debug("Got a JSON request")
    # app.logger.debug("request.args: {}".format(request.args))
    res = request.args.get('vals') # Retrieve jsonified array of locations from website
    # data = jsons.dumps(res)
    # app.logger.debug(type(res))
    # app.logger.debug("data={}".format(res))
    r = requests.get('http://restapi:5000/' + 'compute/' + res) # Passes data into API
    # app.logger.debug(r.text)
    # app.logger.debug(type(r.text))
    # app.logger.debug(jsons.loads(r.text))
    # vals = jsons.loads(r.text)
    # app.logger.debug(type(vals))
    # app.logger.debug(vals)
    return r.text # Return processed data


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
