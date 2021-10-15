"""
Flask-Login and Flask-WTF example
"""
from urllib.parse import urlparse, urljoin
from flask import (Flask, request, render_template, redirect, url_for, flash,
                    abort, session)
from flask_wtf import FlaskForm as Form
from wtforms import BooleanField, StringField, validators
from flask import Flask, render_template, request
import requests


app = Flask(__name__)

app.config.from_object(__name__)



@app.route("/")
def index():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
