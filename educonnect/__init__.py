#!/usr/bin/python3 
from flask import Flask, session, render_template, request, url_for, redirect
from flask_bcrypt import Bcrypt
from educonnect.engine.storage import DBStorage
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
bcrypt = Bcrypt(app)
db_storage = DBStorage()
login_manager = LoginManager(app)
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'

from educonnect.main.routes import main
from educonnect.school.routes import school_blueprint
from educonnect.students.routes import students
from educonnect.parents.routes import parents
from educonnect.admins.routes import admins
from educonnect.teachers.routes import teachers

app.register_blueprint(main)
app.register_blueprint(school_blueprint)
app.register_blueprint(students)
app.register_blueprint(parents)
app.register_blueprint(admins)
app.register_blueprint(teachers)
