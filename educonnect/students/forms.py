#!/usr/bin/python3
"""Forms for the students module"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

#class to submit assignment
class SubmitAssignmentForm(FlaskForm):
    assignment_id = StringField('Assignment ID', validators=[DataRequired()])
    student_id = StringField('Student ID', validators=[DataRequired()])
    assignment_file = StringField('Assignment File', validators=[DataRequired()])
    submit = SubmitField('Submit Assignment')

