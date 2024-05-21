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
        from educonnect.engine.storage import DBStorage
        db_storage = DBStorage()
        from educonnect.models.admin_model import Admin
        from educonnect.models.teacher import Teacher
        from educonnect.models.student import Student
        from educonnect.models.parent import Parent
        from educonnect.models.school import School

        print("debug point 1")
        user_data = {}
        for model_class in [Admin, Teacher, Student, Parent, School]:
            user_data.update(db_storage.all(model_class))
            

        print("debug point 2")
        print("the data generated is:", user_data)
        for user in user_data.values():
            if user.email == email.data:
                raise ValidationError('That email is taken. Please choose a different one.')


#function for registering the admin
class RegisterAdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, email):
        from educonnect.engine.storage import DBStorage
        db_storage = DBStorage()
        from educonnect.models.admin_model import Admin
        from educonnect.models.teacher import Teacher
        from educonnect.models.student import Student
        from educonnect.models.parent import Parent
        from educonnect.models.school import School

        print("debug point 1")
        user_data = {}
        for model_class in [Admin, Teacher, Student, Parent, School]:
            user_data.update(db_storage.all(model_class))
            

        print("debug point 2")
        print("the data generated is:", user_data)
        for user in user_data.values():
            if user.email == email.data:
                raise ValidationError('That email is taken. Please choose a different one.')
