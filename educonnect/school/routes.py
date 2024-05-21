#!/usr/bin/python3
"""Routes for the school module"""

from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, current_user, logout_user, login_required
from educonnect import bcrypt
from educonnect.models.school import School
from educonnect.models.admin_model import Admin
from educonnect.school.forms import RegisterSchoolForm, RegisterAdminForm
from educonnect import db_storage
import logging

school_blueprint = Blueprint('school', __name__)

#function for the school homepage
@school_blueprint.route('/school', methods=['POST', 'GET'], strict_slashes=False)
def school():
    """school route"""
    if 'school_id' in session:
        school_id = session['school_id']
        school = db_storage.get(School, school_id)

        if school:
            school_name = school.name
            return render_template('school.html', school_name=school_name, school_id=school_id)
        else:
            logging.error(f"School not found with ID: {school_id}")
            return render_template('error.html', message="School not found"), 404
    else:
        logging.error("Error number 2, school ID not found in session")
        return render_template('error.html', message="School ID not found in session"), 404

#function to register a school
@school_blueprint.route('/register_school', methods=['POST', 'GET'], strict_slashes=False)
def register_school():
    """register route"""
    form = RegisterSchoolForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        school = School(email=form.email.data, password=hashed_password, name=form.name.data, address=form.address.data, county=form.county.data, phone=form.phone.data, website=form.website.data)
        db_storage.new(school)
        db_storage.save()
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register_school.html', title='Register Your School', form=form)


@school_blueprint.route('/register_admin', methods=['POST', 'GET'], strict_slashes=False)
@login_required
def register_admin():
    """Register admin"""
    if isinstance(current_user, School):
        form = RegisterAdminForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            school = current_user  # Use the current logged-in school
            admin = Admin(email=form.email.data, password=hashed_password, first_name=form.first_name.data, last_name=form.last_name.data, school=school)
            db_storage.new(admin)
            db_storage.save()
            flash(f'Account created for {form.email.data}!', 'success')
            return redirect(url_for('school.school'))
        return render_template('register_admin.html', title='Register Admin', form=form)
    else:
        flash('Only schools can register admins', 'danger')
        return redirect(url_for('main.login'))

