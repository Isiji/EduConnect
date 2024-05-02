#!/usr/bin/python3
"""Teacher session module for the teacher session model"""

from models.teacher import Teacher
from models.student import Student
from models.school import School
from models.classroom import Classroom
from models.engine.storage import DBStorage
from models.subject import Subject
from models.login import login
from models.marks import Marks
from models.assignment import Assignment
def teacher_session():
    """this function is for the teacher functionality"""
    print("Welcome the EduConnect  Teacher Panel")
    print(" ")

    while True:
        print(" ")
        print("What would you like to do?")
        print("0. login ")
        print("1. Register a student")
        print("2. View all students")
        print("3. View all classes")
        print("4. View all subjects")
        print("5. input student marks")
        print("6.update student marks")
        print("7. view student marks")
        print("8. post assignment")
        print("9. view assignment")
        print("10. post assignment marks")
        print("11. view assignment marks")
        print("12. view student performance")
        print("13. exit")

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
            Subject.view_subjects()
        elif choice == '5':
            Marks.input_marks()
        elif choice == '6':
            Marks.update_marks()
        elif choice == '7':
            Marks.view_marks()
        elif choice == '8':
            Assignment.post_assignment()
        elif choice == '9':
            Assignment.view_assignments_by_class_and_teacher()
        elif choice == '10':
            Marks.input_marks()
        elif choice == '11':
            Marks.view_marks_by_assignment()
        elif choice == '12':
            Marks.view_student_performance()
        elif choice == '13':
            break