#!/usr/bin/python3
"""flask application"""
from flask import Flask, render_template, url_for, flash, redirect, session
from educonnect import app, bycrpt, db_storage
from models.engine.storage import DBStorage
from models.admin_model import Admin
from models.teacher import Teacher
from models.student import Student
from models.school import School
from models.classroom import Classroom
from models.assignment import Assignment
from models.parent import Parent
from forms import RegistrationForm, LoginForm, SubmitAssignmentForm, PostAssignmentForm, RegisterClassroomForm, DeleteForm, DeleteAssignmentForm, DeleteClassroomForm, RegisterSchoolForm
from flask_paginate import Pagination, get_page_args
import logging



@app.route('/')
@app.route('/home', methods=['POST', 'GET'], strict_slashes=False)
def home():
    """home route"""
    return render_template('home.html')

#create a login route that first checks if the user is in the database then directs the user to the specific page
@app.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def login():
    """login route"""
    form = LoginForm()
    if form.validate_on_submit():
        user_data = {}
        for model_class in [Admin, Teacher, Student, School]:
            user_data.update(db_storage.all(model_class))
        for user in user_data.values():
            if user.email == form.email.data and bycrpt.check_password_hash(user.password, form.password.data):
                session['email'] = form.email.data
                session['password'] = form.password.data
                if isinstance(user, Admin):
                    return redirect(url_for('admin'))
                elif isinstance(user, Teacher):
                    return redirect(url_for('teacher'))
                elif isinstance(user, Student):
                    return redirect(url_for('student'))
                elif isinstance(user, School):
                    session['school_id'] = user.id
                    print("school id is stored in session:", session['school_id'])
                    return redirect(url_for('school'))
        flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
#admin registration route that checks id school_id entered is present in the database, then creates a new admin and assigns to that school
@app.route('/register_admin', methods=['POST', 'GET'], strict_slashes=False)
def register_admin():
    """register admin"""
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bycrpt.generate_password_hash(form.password.data).decode('utf-8')
        school = db_storage.get(School, form.school_id.data)
        if school:
            admin = Admin(email=form.email.data, password=hashed_password, first_name=form.first_name.data, last_name=form.last_name.data, school=school)
            db_storage.new(admin)
            db_storage.save()
            flash(f'Account created for {form.email.data}!', 'success')
            return redirect(url_for('login'))
        else:
            flash(f'School ID not found', 'danger')
    return render_template('register_admin.html', title='Register Admin', form=form)

#create a route that registers a teacher to a school, check if the school_id is present in the database
@app.route('/register_teacher', methods=['POST', 'GET'], strict_slashes=False)
def register_teacher():
    """register teacher"""
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bycrpt.generate_password_hash(form.password.data).decode('utf-8')
        school = db_storage.get(School, form.school_id.data)
        if school:
            teacher = Teacher(email=form.email.data, password=hashed_password, first_name=form.first_name.data, last_name=form.last_name.data, school=school)
            db_storage.new(teacher)
            db_storage.save()
            flash(f'Account created for {form.email.data}!', 'success')
            return redirect(url_for('login'))
        else:
            flash(f'School ID not found', 'danger')
    return render_template('register_teacher.html', title='Register Teacher', form=form)

#create a route that allows the user to delete a teacher from the database, use the delete method from the storage class to delete the teacher
@app.route('/delete_teacher', methods=['POST', 'GET'], strict_slashes=False)
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
                return redirect(url_for('login'))
    return render_template('delete_teacher.html', title='Delete Teacher', form=form)


#create a route for registering a student to a school, check if the school_id is present in the database
@app.route('/register_student', methods=['POST', 'GET'], strict_slashes=False)
def register_student():
    """register student"""
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bycrpt.generate_password_hash(form.password.data).decode('utf-8')
        school = db_storage.get(School, form.school_id.data)
        if school:
            student = Student(email=form.email.data, password=hashed_password, first_name=form.first_name.data, last_name=form.last_name.data, school=school)
            db_storage.new(student)
            db_storage.save()
            flash(f'Account created for {form.email.data}!', 'success')
            return redirect(url_for('login'))
        else:
            flash(f'School ID not found', 'danger')
    return render_template('register_student.html', title='Register Student', form=form)

#create route for registration of a parent to a school, check if the school_id is present in the database
@app.route('/register_parent', methods=['POST', 'GET'], strict_slashes=False)
def register_parent():
    """register parent"""
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bycrpt.generate_password_hash(form.password.data).decode('utf-8')
        school = db_storage.get(School, form.school_id.data)
        if school:
            parent = Parent(email=form.email.data, password=hashed_password, first_name=form.first_name.data, last_name=form.last_name.data, school=school)
            db_storage.new(parent)
            db_storage.save()
            flash(f'Account created for {form.email.data}!', 'success')
            return redirect(url_for('login'))
        else:
            flash(f'School ID not found', 'danger')
    return render_template('register_parent.html', title='Register Parent', form=form)
@app.route('/register_school', methods=['POST', 'GET'], strict_slashes=False)
def register_school():
    """register route"""
    form = RegisterSchoolForm()
    if form.validate_on_submit():
        hashed_password = bycrpt.generate_password_hash(form.password.data).decode('utf-8')
        school = School(email=form.email.data, password=hashed_password, name=form.name.data, address=form.address.data, county=form.county.data, phone=form.phone.data, website=form.website.data)
        db_storage.new(school)
        db_storage.save()
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register_school.html', title='Register Your School', form=form)

#a route for general registration of a parent or student
@app.route('/register', methods=['POST', 'GET'], strict_slashes=False)
def register():
    """register route"""
    return render_template('registrationpage.html')

#route for registering a classroom to a school, check if the school_id is present in the database
@app.route('/register_classroom', methods=['POST', 'GET'], strict_slashes=False)
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
            return redirect(url_for('admin'))
        else:
            flash(f'School ID not found', 'danger')
    return render_template('register_classroom.html', title='Register Classroom', form=form)


#create a route for viewing all the teachers and paginate it
@app.route('/view_teacher', methods=['POST', 'GET'], strict_slashes=False)
def view_teacher():
    """view teachers paginated route"""
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    teachers_data = db_storage.all(Teacher)
    teachers = list(teachers_data.values())
    pagination = Pagination(page=page, per_page=per_page, total=len(teachers), css_framework='bootstrap4')
    return render_template('view_teacher.html', title='View Teacher', teachers=teachers[offset: offset + per_page], page=page, per_page=per_page, pagination=pagination)

#route for submitting assignments, check if the assignment_id is present in the database
@app.route('/submit_assignment', methods=['POST', 'GET'], strict_slashes=False)
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
            return redirect(url_for('student'))
        else:
            flash(f'Assignment ID not found', 'danger')
    return render_template('submit_assignment.html', title='Submit Assignment', form=form)
@app.route('/post_assignment', methods=['POST', 'GET'], strict_slashes=False)
def post_assignment():
    """post assignment route"""
    form = PostAssignmentForm()
    if form.validate_on_submit():
        assignment = Assignment(assignment_name=form.assignment_name.data, due_date=form.due_date.data, description=form.description.data, classroom_id=form.classroom_id.data)
        db_storage.new(assignment)
        db_storage.save()
        flash(f'Assignment created for {form.assignment_name.data}!', 'success')
        return redirect(url_for('teacher'))
    return render_template('post_assignment.html', title='Post Assignment', form=form)

#create a route that allows the user to view the assignments that have been posted, query the database without using the all method
@app.route('/view_assignment', methods=['POST', 'GET'], strict_slashes=False)
def view_assignment():
    """view assignment route"""
    assignment_data = db_storage.all(Assignment)
    assignments = list(assignment_data.values())
    return render_template('view_assignment.html', title='View Assignment', assignments=assignments)


@app.route('/view_student', methods=['POST', 'GET'], strict_slashes=False)
def view_student():
    """view student route"""
    
    student_data = db_storage.all(Student)
    students = list(student_data.values())
    print(students)
    return render_template('view_student.html', title='View Student', students=students)

#create route for view_classsroom and use paginate to display the data
@app.route('/view_classroom', methods=['POST', 'GET'], strict_slashes=False)
def view_classroom():
    """view classroom route"""
    classroom_data = db_storage.all(Classroom)
    classrooms = list(classroom_data.values())
    return render_template('view_classroom.html', title='View Classroom', classrooms=classrooms)

#create route for deleting a classroom
@app.route('/delete_classroom', methods=['POST', 'GET'], strict_slashes=False)
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
                return redirect(url_for('admin'))
    return render_template('delete_classroom.html', title='Delete Classroom', form=form)

#a route for deleting the assignment, use the delete method from the storage class to delete the assignment using the assignment id
@app.route('/delete_assignment', methods=['POST', 'GET'], strict_slashes=False)
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
                return redirect(url_for('teacher'))
    return render_template('delete_assignment.html', title='Delete Assignment', form=form)

@app.route('/logout', methods=['POST', 'GET'], strict_slashes=False)
def logout():
    """logout route"""
    session.pop('email', None)
    session.pop('password', None)
    return redirect(url_for('home'))

@app.route('/about', methods=['POST', 'GET'], strict_slashes=False)
def about():
    """about route"""
    return render_template('about.html')

@app.route('/school', methods=['POST', 'GET'], strict_slashes=False)
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

@app.route('/contact', methods=['POST', 'GET'], strict_slashes=False)
def contact():
    """contact route"""
    return render_template('contact.html')


@app.route('/admin', methods=['POST', 'GET'], strict_slashes=False)
def admin():
    """admin route"""
    return render_template('admin.html')
@app.route('/teacher', methods=['POST', 'GET'], strict_slashes=False)
def teacher():
    """teacher route"""
    return render_template('teacher.html')

@app.route('/student', methods=['POST', 'GET'], strict_slashes=False)
def student():
    """student route"""
    return render_template('student.html')

@app.route('/parent', methods=['POST', 'GET'], strict_slashes=False)
def parent():
    """parent route"""
    return render_template('parent.html')
@app.route('/account', methods=['POST', 'GET'], strict_slashes=False)
def account():
    """account route"""
    return render_template('account.html')
