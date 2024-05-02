#!/usr/bin/python3
"""flask application"""

from flask import Flask, session, render_template, request, url_for, redirect

app = Flask(__name__)
app.secret_key = 'secret_key'
@app.route('/')
def home():
    """home route"""
    return render_template('home.html')

@app.route('/login/', methods=['POST', 'GET'])
def login():
    """login route"""
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('home'))
    else:
        if user in session:
            return redirect(url_for('home'))
        
        return render_template('login.html')
@app.route('/logout/')
def logout():
    """logout route"""
    session.pop('user', None)
    return redirect(url_for('home'))
@app.route('user')
def user():
    """user route"""
    if "user" in session:
        user = session['user']
        return render_template('user.html')
    return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
