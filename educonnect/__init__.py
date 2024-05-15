#!/usr/bin/python3 
from flask import Flask, session, render_template, request, url_for, redirect
from flask_bcrypt import Bcrypt
from educonnect.engine.storage import DBStorage
from flask_login import LoginManager
from educonnect.config import Config

bcrypt = Bcrypt()
db_storage = DBStorage()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    bcrypt.init_app(app)
    db_storage
    login_manager.init_app(app)


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

    return app