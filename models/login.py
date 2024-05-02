#!/usr/bin/python3
"""Login module for the login model"""



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
            return
    for teacher in teachers:
        if teacher.email == email and teacher.password == password:
            print("Login successful")
            return
    for student in students:
        if student.email == email and student.password == password:
            print("Login successful")
            return
    for admin in admins:
        if admin.email == email and admin.password == password:
            print("Login successful")
            return
    print("Login failed. Incorrect email or password!")