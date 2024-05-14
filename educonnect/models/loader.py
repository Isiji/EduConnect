#!/usr/bin/python3

from educonnect import login_manager

#create a user loader function that checks through the database for the user
@login_manager.user_loader
def load_user(user_id):
    """checks through the database for the user"""
    from educonnect.models.teacher import Teacher
    from educonnect.models.admin_model import Admin
    from educonnect.models.student import Student
    from educonnect.models.parent import Parent
    from educonnect.models.school import School

    user = Teacher.get(user_id) + Admin.get(user_id) + Student.get(user_id) + Parent.get(user_id) + School.get(user_id)
    return user

