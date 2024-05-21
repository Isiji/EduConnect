#!/usr/bin/python3
"""Routes for the main module"""

from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, current_user, logout_user, login_required
from educonnect import bcrypt
from educonnect.models.admin_model import Admin
from educonnect.models.teacher import Teacher
from educonnect.models.student import Student
from educonnect.models.parent import Parent
from educonnect.models.school import School
from educonnect.models.classroom import Classroom
from educonnect.models.assignment import Assignment
from educonnect.main.forms import RegistrationForm, LoginForm, UpdateAccountForm
from educonnect import db_storage
from educonnect.main.utils import save_picture
from flask_paginate import Pagination, get_page_args


main = Blueprint('main', __name__)

@main.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def login():
    """login route"""
    form = LoginForm()
    if form.validate_on_submit():
        user_data = {}
        for model_class in [Admin, Teacher, Student, Parent, School]:
            user_data.update(db_storage.all(model_class))
        for user in user_data.values():
            if user.email == form.email.data and bcrypt.check_password_hash(user.password, form.password.data):
                session['email'] = form.email.data
                session['password'] = form.password.data
                login_user(user, remember=form.remember.data)
                
                if isinstance(user, Admin):
                    return redirect(url_for('admins.admin'))
                elif isinstance(user, Teacher):
                    return redirect(url_for('teachers.teacher'))
                elif isinstance(user, Student):
                    return redirect(url_for('student.student'))
                elif isinstance(user, Parent):
                    return redirect(url_for('parents.parent'))
                elif isinstance(user, School):
                    session['school_id'] = user.id
                    return redirect(url_for('school.school'))
        flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


#function for home route
@main.route('/')
@main.route('/home', methods=['POST', 'GET'], strict_slashes=False)
def home():
    """home route"""
    return render_template('home.html')

#function for about route
@main.route('/about', methods=['POST', 'GET'], strict_slashes=False)
def about():
    """about route"""
    return render_template('about.html')

#function for contact route
@main.route('/contact', methods=['POST', 'GET'], strict_slashes=False)
def contact():
    """contact route"""
    return render_template('contact.html')

#a route for general registration of a parent or student
@main.route('/register', methods=['POST', 'GET'], strict_slashes=False)
def register():
    """register route"""
    return render_template('registrationpage.html')


@main.route('/account', methods=['POST', 'GET'], strict_slashes=False)
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db_storage.save()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('main.account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

#function for the logout route
@main.route('/logout', methods=['POST', 'GET'], strict_slashes=False)
@login_required
def logout():
    """logout route"""
    logout_user()
    session.clear()
    return redirect(url_for('main.home'))

#create route for view_classsroom and use paginate to display the data
@main.route('/view_classroom', methods=['POST', 'GET'], strict_slashes=False)
def view_classroom():
    """view classroom route"""
    classroom_data = db_storage.all(Classroom)
    classrooms = list(classroom_data.values())
    return render_template('view_classroom.html', title='View Classroom', classrooms=classrooms)

#create a route that allows the user to view the assignments that have been posted, query the database without using the all method
@main.route('/view_assignment', methods=['POST', 'GET'], strict_slashes=False)
def view_assignment():
    """view assignment route"""
    assignment_data = db_storage.all(Assignment)
    assignments = list(assignment_data.values())
    return render_template('view_assignment.html', title='View Assignment', assignments=assignments)

#route for viewings the students
@main.route('/view_student', methods=['POST', 'GET'], strict_slashes=False)
def view_student():
    """view student route"""
    
    student_data = db_storage.all(Student)
    students = list(student_data.values())
    print(students)
    return render_template('view_student.html', title='View Student', students=students)

#create route for registration of a parent to a school, check if the school_id is present in the database
@main.route('/register_parent', methods=['POST', 'GET'], strict_slashes=False)
def register_parent():
    """register parent"""
    if current_user.is_authenticated:
        return redirect(url_for('parents.parent'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        school = db_storage.get(School, form.school_id.data)
        if school:
            parent = Parent(email=form.email.data, password=hashed_password, first_name=form.first_name.data, last_name=form.last_name.data, school=school)
            db_storage.new(parent)
            db_storage.save()
            flash(f'Account created for {form.email.data}!', 'success')
            return redirect(url_for('main.login'))
        else:
            flash(f'School ID not found', 'danger')
    return render_template('register_parent.html', title='Register Parent', form=form)

#create a route for registering a student to a school, check if the school_id is present in the database
@main.route('/register_student', methods=['POST', 'GET'], strict_slashes=False)
def register_student():
    """register student"""
    if current_user.is_authenticated:
        return redirect(url_for('students.student'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        school = db_storage.get(School, form.school_id.data)
        if school:
            student = Student(email=form.email.data, password=hashed_password, first_name=form.first_name.data, last_name=form.last_name.data, school=school)
            db_storage.new(student)
            db_storage.save()
            flash(f'Account created for {form.email.data}!', 'success')
            return redirect(url_for('main.login'))
        else:
            flash(f'School ID not found', 'danger')
    return render_template('register_student.html', title='Register Student', form=form)

#create a route for viewing all the teachers and paginate it
@main.route('/view_teacher', methods=['POST', 'GET'], strict_slashes=False)
def view_teacher():
    """view teachers paginated route"""
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    teachers_data = db_storage.all(Teacher)
    teachers = list(teachers_data.values())
    pagination = Pagination(page=page, per_page=per_page, total=len(teachers), css_framework='bootstrap4')
    return render_template('view_teacher.html', title='View Teacher', teachers=teachers[offset: offset + per_page], page=page, per_page=per_page, pagination=pagination)
