#!/usr/bin/python3
"""flask application"""

from flask import Flask, session, render_template, request, url_for, redirect
from forms import LoginForm, RegistrationForm, RegisterSchoolForm, DeleteForm, RegisterClassroomForm, ViewTeachersForm, PostAssignmentForm
from flask import flash
from models.engine.storage import DBStorage
from models.admin_model import Admin
from flask_bcrypt import Bcrypt
from models.teacher import Teacher
from models.student import Student
from models.school import School
from models.classroom import Classroom
from models.assignment import Assignment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
bycrpt = Bcrypt(app)
db_storage = DBStorage()


@app.route('/')
@app.route('/home/', methods=['POST', 'GET'], strict_slashes=False)
def home():
    """home route"""
    return render_template('home.html')

@app.route('/login/', methods=['POST', 'GET'], strict_slashes=False)
def login():
    """login route"""
    form = LoginForm()
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['password'] = form.password.data
        flash('You have been logged in!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/register_admin/', methods=['POST', 'GET'], strict_slashes=False)
def register_admin():
    """register route"""
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bycrpt.generate_password_hash(form.password.data).decode('utf-8')
        admin = Admin(email=form.email.data, password=hashed_password, first_name=form.first_name.data, last_name=form.last_name.data)
        db_storage.new(admin)
        db_storage.save()
        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register_admin.html', title='Register', form=form)

@app.route('/register_teacher/', methods=['POST', 'GET'], strict_slashes=False)
def register_teacher():
    """register route"""
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bycrpt.generate_password_hash(form.password.data).decode('utf-8')
        teacher = Teacher(email=form.email.data, password=hashed_password, first_name=form.first_name.data, last_name=form.last_name.data)
        db_storage.new(teacher)
        db_storage.save()
        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register_teacher.html', title='Register Teacher', form=form)
#should delete from database
@app.route('/register_student/', methods=['POST', 'GET'], strict_slashes=False)
def register_student():
    """register route"""
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bycrpt.generate_password_hash(form.password.data).decode('utf-8')
        student = Student(email=form.email.data, password=hashed_password, first_name=form.first_name.data, last_name=form.last_name.data)
        db_storage.new(student)
        db_storage.save()
        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register_student.html', title='Register', form=form)



@app.route('/register_school/', methods=['POST', 'GET'], strict_slashes=False)
def register_school():
    """register route"""
    form = RegisterSchoolForm()
    if form.validate_on_submit():
        hashed_password = bycrpt.generate_password_hash(form.password.data).decode('utf-8')
        school = School(email=form.email.data, password=hashed_password, name=form.name.data, address=form.address.data, county=form.county.data, phone=form.phone.data, website=form.website.data)
        db_storage.new(school)
        db_storage.save()
        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register_school.html', title='Register Your School', form=form)

@app.route('/register_classroom/', methods=['POST', 'GET'], strict_slashes=False)
def register_classroom():
    """register route"""
    form = RegisterClassroomForm()
    if form.validate_on_submit():
        classroom = Classroom(name=form.name.data)
        db_storage.new(classroom)
        db_storage.save()
        flash(f'Classroom created for {form.name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register_classroom.html', title='Register Classroom', form=form)
@app.route('/delete_teacher/', methods=['POST', 'GET'], strict_slashes=False)
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

@app.route('/view_teacher/', methods=['POST', 'GET'], strict_slashes=False)
def view_teacher():
    """view route"""
    form = ViewTeachersForm()
    if form.validate_on_submit():
        teacher = db_storage.all('Teacher')
        for t in teacher:
            print(t)
    return render_template('view_teacher.html', title='View Teacher', form=form)

@app.route('/post_assignment/', methods=['POST', 'GET'], strict_slashes=False)
def post_assignment():
    """post assignment route"""
    form = PostAssignmentForm()
    if form.validate_on_submit():
        assignment = Assignment(assignment_name=form.assignment_name.data, due_date=form.due_date.data, description=form.description.data, classroom=form.classroom.data)
        db_storage.new(assignment)
        db_storage.save()
        flash(f'Assignment created for {form.assignment_name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('post_assignment.html', title='Post Assignment', form=form)

@app.route('/view_assignment/', methods=['POST', 'GET'], strict_slashes=False)
def view_assignment():
    """view assignment route"""
    assignment = db_storage.all('Assignment')
    for a in assignment:
        print(a)
    return render_template('view_assignment.html', title='View Assignment')

@app.route('/view_student/', methods=['POST', 'GET'], strict_slashes=False)
def view_student():
    """view student route"""
    
    student = db_storage.all('Student')
    for s in student:
        print(s)
    return render_template('view_student.html', title='View Student')

@app.route('/view_classroom/', methods=['POST', 'GET'], strict_slashes=False)
def view_classroom():
    """view classroom route"""
    classroom = db_storage.all('Classroom')
    for c in classroom:
        print(c)
    return render_template('view_classroom.html', title='View Classroom')
@app.route('/logout/', methods=['POST', 'GET'], strict_slashes=False)
def logout():
    """logout route"""
    session.pop('email', None)
    session.pop('password', None)
    return redirect(url_for('home'))

@app.route('/about/', methods=['POST', 'GET'], strict_slashes=False)
def about():
    """about route"""
    return render_template('about.html')

@app.route('/contact/', methods=['POST', 'GET'], strict_slashes=False)
def contact():
    """contact route"""
    return render_template('contact.html')


@app.route('/admin/', methods=['POST', 'GET'], strict_slashes=False)
def admin():
    """admin route"""
    return render_template('admin.html')
@app.route('/teacher/', methods=['POST', 'GET'], strict_slashes=False)
def teacher():
    """teacher route"""
    return render_template('teacher.html')

@app.route('/student/', methods=['POST', 'GET'], strict_slashes=False)
def student():
    """student route"""
    return render_template('student.html')

@app.route('/parent/', methods=['POST', 'GET'], strict_slashes=False)
def parent():
    """parent route"""
    return render_template('parent.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
