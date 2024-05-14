#!/usr/bin/python3 
from flask import Flask, session, render_template, request, url_for, redirect
from flask_bcrypt import Bcrypt
from educonnect.engine.storage import DBStorage
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
bycrpt = Bcrypt(app)
db_storage = DBStorage()
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from educonnect import routes, models


