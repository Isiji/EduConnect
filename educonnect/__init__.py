#!/usr/bin/python3 
from flask import Flask, session, render_template, request, url_for, redirect
from flask_bcrypt import Bcrypt
from educonnect.engine.storage import DBStorage


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
bycrpt = Bcrypt(app)
db_storage = DBStorage()

from educonnect import routes, models


