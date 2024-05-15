#!/usr/bin/python3
"""Routes for the teachers module"""

from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from educonnect.models.assignment import Assignment
from educonnect.teachers.forms import PostAssignmentForm, DeleteAssignmentForm
from educonnect import db_storage

teachers = Blueprint('teachers', __name__)

#function for the teachers home page
@teachers.route('/teacher', methods=['POST', 'GET'], strict_slashes=False)
def teacher():
    """teacher route"""
    return render_template('teacher.html')

#a route for deleting the assignment, use the delete method from the storage class to delete the assignment using the assignment id
@teachers.route('/delete_assignment', methods=['POST', 'GET'], strict_slashes=False)
def delete_assignment():
    """delete assignment route"""
    form = DeleteAssignmentForm()
    if form.validate_on_submit():
        assignment = db_storage.all('Assignment')
        for a in assignment:
            if a.id == form.id.data:
                db_storage.delete(a)
                db_storage.save()
                flash(f'Assignment deleted for {form.id.data}!', 'success')
                return redirect(url_for('teachers.teacher'))
    return render_template('delete_assignment.html', title='Delete Assignment', form=form)

#funtion for posting assignments
@teachers.route('/post_assignment', methods=['POST', 'GET'], strict_slashes=False)
def post_assignment():
    """post assignment route"""
    form = PostAssignmentForm()
    if form.validate_on_submit():
        assignment = Assignment(assignment_name=form.assignment_name.data, due_date=form.due_date.data, description=form.description.data, classroom_id=form.classroom_id.data)
        db_storage.new(assignment)
        db_storage.save()
        flash(f'Assignment created for {form.assignment_name.data}!', 'success')
        return redirect(url_for('teachers.teacher'))
    return render_template('post_assignment.html', title='Post Assignment', form=form)
