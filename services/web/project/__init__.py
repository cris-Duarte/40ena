from flask import Flask, jsonify, render_template, request, abort, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
from datetime import datetime, date, timedelta
import calendar
import json
import os
import string
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify(hello="world")


@app.route("/personas")
def personas():
    return render_template('personas.html')
