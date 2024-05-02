#!/usr/bin/python3

"""Login module for the login model"""

from models.admin_session import admin_session
from models.parent_session import parent_session
from models.teacher_session import teacher_session
from models.student_session import student_session


# a login function that queries the database tables in parents, teachers, students and admins for the user's email and password
def login():
    """login function"""
    from models.engine.storage import DBStorage
    db_storage = DBStorage()

    email = input("Enter email: ")
    password = input("Enter password: ")

    parents = db_storage.all('Parent')
    teachers = db_storage.all('Teacher')
    students = db_storage.all('Student')
    admins = db_storage.all('Admin')

    for parent in parents:
        if parent.email == email and parent.password == password:
            print("Login successful")
            parent_session(parent)
            return
    for teacher in teachers:
        if teacher.email == email and teacher.password == password:
            print("Login successful")
            teacher_session(teacher)
            return
    for student in students:
        if student.email == email and student.password == password:
            print("Login successful")
            student_session(student)
            return
    for admin in admins:
        if admin.email == email and admin.password == password:
            print("Login successful")
            admin_session(admin)
            return
    print("Login failed. Incorrect email or password!")