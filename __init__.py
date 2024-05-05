#!/usr/bin/python3 
from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)

"""Module for the models package"""
from web_flask.models.engine.storage import DBStorage

DBStorage().reload()

bycrpt = Bcrypt(app)

