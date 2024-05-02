#!/usr/bin/python3
"""flask application"""

from flask import Flask, session, render_template, request, url_for, redirect

app = Flask(__name__)
app.secret_key = 'secret_key'
@app.route('/')
def home():
    """home route"""
    return render_template('home.html')

@app.route('/login/', methods=['POST', 'GET'], strict_slashes=False)
def login():
    """login route"""
    return render_template('login.html')

@app.route('/admin/', methods=['POST', 'GET'], strict_slashes=False)
def admin():
    """admin route"""
    return render_template('admin.html')
@app.route('/teacher/', methods=['POST', 'GET'], strict_slashes=False)
def teacher():
    """teacher route"""
    return render_template('teacher.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
