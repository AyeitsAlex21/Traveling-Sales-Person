"""
website.py
Source Code for flask webpage interaction between html/javascript and Genetic Algorithm to Google Maps API.
Author(s): Kale Satta-Hutton, Anna Nguyen
Group: NASAK
CIS422 F21
Last Modifed Date: 10/31/21
Description:
  This file contains two routes. The first route renders base.html when the user first navigates to the landing page.
  The second function, _min_path, gets the array of locations passsed in from the UI containing the place name, place
  location (longitude, latitude) and place ID. This will be passed to the web app API to be processed by the GenAlgo.
"""
import flask
from urllib.parse import urlparse, urljoin
from flask import (Flask, request, render_template, redirect, url_for, flash,
                    abort, session)
from flask import Flask, render_template, request
import requests # allows the sending of HTTP requests


app = flask.Flask(__name__) # creates Flask instance

app.config.from_object(__name__) # import configuration into Flask instance

# Binds index function to base URL and renders template
@app.route("/")
def index():
    """
    Open the base.html file, the only acessible route
    """
    return render_template("base.html")

# Binds _min_path function to URL.
@app.route("/_min_path", methods=["GET"])
def _min_path():
    """
    Creates a call to the restful api container
    """
    res = request.args.get('vals') # Retrieve jsonified array of locations from website
    r = requests.get('http://restapi:5000/' + 'compute/' + res) # Passes data into API
    return r.text # Return processed data


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
