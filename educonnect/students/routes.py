#!/usr/bin/python3
"""Routes for the students module"""

from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, current_user, logout_user, login_required
from educonnect.models.assignment import Assignment

from educonnect.students.forms import SubmitAssignmentForm
from educonnect import db_storage


students = Blueprint('students', __name__)

#function for the students home page
@students.route('/student', methods=['POST', 'GET'], strict_slashes=False)
def student():
    """student route"""
    return render_template('student.html')

#route for submitting assignments, check if the assignment_id is present in the database
@students.route('/submit_assignment', methods=['POST', 'GET'], strict_slashes=False)
def submit_assignment():
    """submit assignment route"""
    form = SubmitAssignmentForm()
    if form.validate_on_submit():
        assignment = db_storage.get(Assignment, form.assignment_id.data)
        if assignment:
            assignment.student_id = form.student_id.data
            assignment.submission = form.submission.data
            db_storage.save()
            flash(f'Assignment submitted for {form.assignment_id.data}!', 'success')
            return redirect(url_for('students.student'))
        else:
            flash(f'Assignment ID not found', 'danger')
    return render_template('submit_assignment.html', title='Submit Assignment', form=form)
