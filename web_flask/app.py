#!/usr/bin/python3
"""flask application"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    """home route"""
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
