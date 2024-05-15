#!/usr/bin/python3
"""Forms for the students module"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

#class to delete a classroom
class DeleteClassroomForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Delete Classroom')

#class to create a form to register a classroom
class RegisterClassroomForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    school_id = StringField('School ID', validators=[DataRequired()])
    submit = SubmitField('Register Class')
    def validate_name(self, name):
        from engine.storage import DBStorage
        db_storage = DBStorage()
        from models.classroom import Classroom
        classrooms = db_storage.all(Classroom)
        for classroom in classrooms.values():
            if classroom.name == name.data:
                raise ValidationError('That classroom is already registered. Please choose a different one.')
#class where admin can view all teachers
class ViewTeachersForm(FlaskForm):
    submit = SubmitField('View Teachers')
#create a delete form  where the admin will use to delete other records like teachers, students and parents but must enter his password to confirm the delete action
class DeleteForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Delete')

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name',
                       validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    school_id = StringField('School ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        from engine.storage import DBStorage
        db_storage = DBStorage()
        from models.admin_model import Admin
        from models.teacher import Teacher
        from models.student import Student
        from models.parent import Parent
        from models.school import School

        print("debug point 1")
        user_data = {}
        for model_class in [Admin, Teacher, Student, Parent, School]:
            user_data.update(db_storage.all(model_class))
            

        print("debug point 2")
        print("the data generated is:", user_data)
        for user in user_data.values():
            if user.email == email.data:
                raise ValidationError('That email is taken. Please choose a different one.')
