#!/usr/bin/python3
"""Register module for admin, student, teacher, school and classroom models"""

from models.admin_model import Admin
from models.student import Student
from models.teacher import Teacher
from models.school import School
from models.classroom import Classroom
from models.engine.storage import DBStorage
from models.parent import Parent
def register():
    """register function"""
    print("Welcome to the EduConnect Registration Panel")
    print(" ")

    while True:
        print("Select an option")
        print("1. Register a new admin")
        print("2. Register student")
        print("3. Register teacher")
        print("4. Register school")
        print("5. Register classroom")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Enter a number")
            continue

        if choice == 1:
            admin = Admin()
            admin.register_admin()

        elif choice == 2:
            student = Student()
            student.register_student()

        elif choice == 3:
            teacher = Teacher()
            teacher.register_teacher()

        elif choice == 4:
            parent = Parent()
            parent.register_parent()

        elif choice == 6:
            break
        else:
            print("Invalid choice")
            continue