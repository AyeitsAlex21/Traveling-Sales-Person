"""
Flask-Login and Flask-WTF example
"""
import flask
import jsons
from urllib.parse import urlparse, urljoin
from flask import (Flask, request, render_template, redirect, url_for, flash,
                    abort, session)
from flask_wtf import FlaskForm as Form
from wtforms import BooleanField, StringField, validators
from flask import Flask, render_template, request
import requests


app = flask.Flask(__name__)

app.config.from_object(__name__)



@app.route("/")
def index():
    return render_template("base.html")

@app.route("/_min_path", methods=["GET"])
def _min_path():
    """

    """
    app.logger.debug("Got a JSON request")
    app.logger.debug("request.args: {}".format(request.args))
    res = request.args.get('vals')
    # data = jsons.dumps(res)
    app.logger.debug(type(res))
    app.logger.debug("data={}".format(res))
    r = requests.get('http://restapi:5000/' + 'compute/' + res)
    return r.text
    #return flask.jsonify(result=res)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
