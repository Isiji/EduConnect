#!/usr/bin/python3 
from flask import Flask, session, render_template, request, url_for, redirect
from flask import flash
from flask_bcrypt import Bcrypt
from flask_login import  LoginManager, login_user, current_user, logout_user, login_required
import logging
from flask_paginate import Pagination, get_page_args
from educonnect.models.engine.storage import DBStorage


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
bycrpt = Bcrypt(app)
db_storage = DBStorage()

from educonnect import routes, models


