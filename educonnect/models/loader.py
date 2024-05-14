#!/usr/bin/python3

from educonnect import login_manager

#create a user loader function that checks through the database for the user id
@login_manager.user_loader
def load_user(user_id):
    """checks through the database for the user"""
    from educonnect.models.teacher import Teacher
    from educonnect.models.admin_model import Admin
    from educonnect.models.student import Student
    from educonnect.models.parent import Parent
    from educonnect.models.school import School
    from educonnect import db_storage

    user = db_storage.get(Teacher, user_id)
    if user is None:
        user = db_storage.get(Admin, user_id)
    if user is None:
        user = db_storage.get(Student, user_id)
    if user is None:
        user = db_storage.get(Parent, user_id)
    if user is None:
        user = db_storage.get(School, user_id)
    return user
    
