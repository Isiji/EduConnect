#!/usr/bin/python3
"""Forms for the students module"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegisterSchoolForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    address = StringField('Address', validators=[DataRequired()])
    county = StringField('County')
    phone = StringField('Phone', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    website = StringField('Website', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register School')

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
