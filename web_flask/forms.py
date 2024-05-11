from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sqlalchemy import text

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name',
                       validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        from models.engine.storage import DBStorage
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

                    



#create a form to post an assignment
class PostAssignmentForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    due_date = StringField('Due Date', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Post Assignment')

#class to create a form to register a classroom
class RegisterClassroomForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Register Class')

#class where admin can view all teachers
class ViewTeachersForm(FlaskForm):
    submit = SubmitField('View Teachers')
#create a delete form  where the admin will use to delete other records like teachers, students and parents but must enter his password to confirm the delete action
class DeleteForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Delete')





class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

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

    #create a class for a teacher to post assignments
class PostAssignmentForm(FlaskForm):
    assignment_name = StringField('Assignment Name', validators=[DataRequired()])
    due_date = StringField('Due Date', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    classroom = StringField('Classroom', validators=[DataRequired()])
    submit = SubmitField('Post Assignment')

    #class to view all students
class ViewStudentsForm(FlaskForm):
    submit = SubmitField('View Students')

    #class to view all parents