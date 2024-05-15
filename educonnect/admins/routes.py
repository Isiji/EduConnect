from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from educonnect import bcrypt
from educonnect.models.admin_model import Admin
from educonnect.models.teacher import Teacher
from educonnect.models.school import School
from educonnect.models.classroom import Classroom
from educonnect.admins.forms import RegistrationForm, DeleteForm, RegisterClassroomForm, DeleteClassroomForm
from educonnect import db_storage
from flask_pagination   import Pagination
from flask_paginate import get_page_args



admins = Blueprint('admins', __name__)

#function for the admin home page
admins.route('/admin', methods=['POST', 'GET'], strict_slashes=False)
def admin():
    """admin route"""
    return render_template('admin.html')

#create route for deleting a classroom
admins.route('/delete_classroom', methods=['POST', 'GET'], strict_slashes=False)
def delete_classroom():
    """delete classroom route"""
    form = DeleteClassroomForm()
    if form.validate_on_submit():
        classroom = db_storage.all(Classroom).values()
        for c in classroom:
            if c.name == form.name.data:
                db_storage.delete(c)
                db_storage.save()
                flash(f'Classroom deleted for {form.name.data}!', 'success')
                return redirect(url_for('admins.admin'))
    return render_template('delete_classroom.html', title='Delete Classroom', form=form)

#create a route for viewing all the teachers and paginate it
admins.route('/view_teacher', methods=['POST', 'GET'], strict_slashes=False)
def view_teacher():
    """view teachers paginated route"""
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    teachers_data = db_storage.all(Teacher)
    teachers = list(teachers_data.values())
    pagination = Pagination(page=page, per_page=per_page, total=len(teachers), css_framework='bootstrap4')
    return render_template('view_teacher.html', title='View Teacher', teachers=teachers[offset: offset + per_page], page=page, per_page=per_page, pagination=pagination)

#route for registering a classroom to a school, check if the school_id is present in the database
admins.route('/register_classroom', methods=['POST', 'GET'], strict_slashes=False)
def register_classroom():
    """register classroom route"""
    form = RegisterClassroomForm()
    if form.validate_on_submit():
        school = db_storage.get(School, form.school_id.data)
        if school:
            classroom = Classroom(name=form.name.data, school=school)
            db_storage.new(classroom)
            db_storage.save()
            flash(f'Classroom created for {form.name.data}!', 'success')
            return redirect(url_for('admins.admin'))
        else:
            flash(f'School ID not found', 'danger')
    return render_template('register_classroom.html', title='Register Classroom', form=form)

#create a route that allows the user to delete a teacher from the database, use the delete method from the storage class to delete the teacher
admins.route('/delete_teacher', methods=['POST', 'GET'], strict_slashes=False)
def delete_teacher():
    """delete route"""
    form = DeleteForm()
    if form.validate_on_submit():
        teacher = db_storage.all('Teacher')
        for t in teacher:
            if t.email == form.email.data:
                db_storage.delete(t)
                db_storage.save()
                flash(f'Account deleted for {form.email.data}!', 'success')
                return redirect(url_for('main.login'))
    return render_template('delete_teacher.html', title='Delete Teacher', form=form)

#create a route that registers a teacher to a school, check if the school_id is present in the database
admins.route('/register_teacher', methods=['POST', 'GET'], strict_slashes=False)
def register_teacher():
    """register teacher"""
    if current_user.is_authenticated:
        return redirect(url_for('teachers.teacher'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        school = db_storage.get(School, form.school_id.data)
        if school:
            teacher = Teacher(email=form.email.data, password=hashed_password, first_name=form.first_name.data, last_name=form.last_name.data, school=school)
            db_storage.new(teacher)
            db_storage.save()
            flash(f'Account created for {form.email.data}!', 'success')
            return redirect(url_for('main.login'))
        else:
            flash(f'School ID not found', 'danger')
    return render_template('register_teacher.html', title='Register Teacher', form=form)

