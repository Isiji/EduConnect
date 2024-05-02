#!/usr/bin/python3
"""ParentSession module for the parent session model"""

from models.parent import Parent
from models.student import Student
from models.teacher import Teacher
from models.school import School
from models.classroom import Classroom
from models.login import login
from models.subject import Subject
from models.marks import Marks
from models.assignment import Assignment
def parent_session():
    """this function is for the parent functionality"""
    print("Welcome the EduConnect Parent Panel")
    print(" ")

    while True:
        print(" ")
        print("What would you like to do?")
        print("0. login ")
        print("2. View all students")
        print("3. View all classes")
        print("4. View all subjects")
        print("5. view student marks")
        print("6. view student performance")
        print("7. view assigments")
        print("8. exit")

        choice = input("Enter choice: ")

        if choice == '0':
            login()
        elif choice == '1':
            Student.register_student()
        elif choice == '2':
            Student.view_all_students()
        elif choice == '3':
            Classroom.view_classes()
        elif choice == '4':
            Subject.view_subjects_by_class()
        elif choice == '5':
            Marks.view_marks_by_student()
        elif choice == '6':
            Marks.view_student_performance()
        elif choice == '7':
            Assignment.view_assignments_by_class()
        elif choice == '8':
            break