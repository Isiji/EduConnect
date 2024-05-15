#!/bin/usr/python3
"""Routes for the parents module"""

from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, current_user, logout_user, login_required
from educonnect.models.parent import Parent
from educonnect import db_storage

parents = Blueprint('parents', __name__)

#a function for the parents homepage
@parents.route('/parent', methods=['POST', 'GET'], strict_slashes=False)
def parent():
    """parent route"""
    return render_template('parent.html')



