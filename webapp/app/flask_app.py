"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request, abort, render_template, jsonify, redirect, url_for
import os
import config
import logging
from json import loads
###
# Globals
###

app = flask.Flask(__name__)
CONFIG = config.configuration()

###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


@app.errorhandler(400)
def submit_error(error):
    app.logger.debug("Bad Request")
    return flask.render_template('400.html'), 400

@app.errorhandler(503)
def display_error(error):
    app.logger.debug("Service Unavailable")
    return flask.render_template('503.html'), 503



#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
