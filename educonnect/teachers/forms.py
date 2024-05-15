#!/usr/bin/python3
"""Forms for the students module"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


#create a function to delete an assignment
class DeleteAssignmentForm(FlaskForm):
    assignment_id = StringField('Assignment ID', validators=[DataRequired()])
    submit = SubmitField('Delete Assignment')


    #create a class for a teacher to post assignments
class PostAssignmentForm(FlaskForm):
    assignment_name = StringField('Assignment Name', validators=[DataRequired()])
    due_date = StringField('Due Date', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    classroom_id = StringField('Classroom', validators=[DataRequired()])
    submit = SubmitField('Post Assignment')

#create a form to post an assignment
class PostAssignmentForm(FlaskForm):
    assignment_name = StringField('Assignment Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    due_date = StringField('Due Date', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    classroom_id = StringField('Classroom ID', validators=[DataRequired()])
    submit = SubmitField('Post Assignment')
