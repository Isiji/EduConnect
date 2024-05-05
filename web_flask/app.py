#!/usr/bin/python3
"""flask application"""

from flask import Flask, session, render_template, request, url_for, redirect
from forms import LoginForm, RegistrationForm
from flask import flash
from models.engine.storage import DBStorage
from models.admin_model import Admin
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
bycrpt = Bcrypt(app)
db_storage = DBStorage()
@app.route('/')
def home():
    """home route"""
    return render_template('home.html')

@app.route('/login/', methods=['POST', 'GET'], strict_slashes=False)
def login():
    """login route"""
    form = LoginForm()
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['password'] = form.password.data
        flash('You have been logged in!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/register/', methods=['POST', 'GET'], strict_slashes=False)
def register():
    """register route"""
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bycrpt.generate_password_hash(form.password.data).decode('utf-8')
        admin = Admin(email=form.email.data, password=hashed_password, first_name=form.first_name.data, last_name=form.last_name.data)
        db_storage.new(admin)
        db_storage.save()
        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register_admin.html', title='Register', form=form)
@app.route('/admin/', methods=['POST', 'GET'], strict_slashes=False)
def admin():
    """admin route"""
    return render_template('admin.html')
@app.route('/teacher/', methods=['POST', 'GET'], strict_slashes=False)
def teacher():
    """teacher route"""
    return render_template('teacher.html')

@app.route('/student/', methods=['POST', 'GET'], strict_slashes=False)
def student():
    """student route"""
    return render_template('student.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
