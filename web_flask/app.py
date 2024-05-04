#!/usr/bin/python3
"""flask application"""

from flask import Flask, session, render_template, request, url_for, redirect
from forms import LoginForm, RegistrationForm
from flask import flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
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
        session['username'] = form.username.data
        session['email'] = form.email.data
        session['password'] = form.password.data
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
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
