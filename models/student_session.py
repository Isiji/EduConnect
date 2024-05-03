#!/usr/bin/python3
"""StudentSession module for the student session model"""

from models.student import Student
from models.engine.storage import DBStorage
from models.marks import Marks
from models.assignment import Assignment
from models.subject import Subject
from models.classroom import Classroom
from models.school import School

def student_session():
    """this function is for the student functionality"""
    print("Welcome the EduConnect Student Panel")
    print(" ")

    while True:
        print(" ")
        print("What would you like to do?")
        print("1. View all subjects")
        print("2. View all classes")
        print("3. View assignments by class")
        print("4. View all marks")
        print("5. View student performance")
        print("6. exit")

        choice = input("Enter choice: ")

    
        if choice == '1':
            Subject.view_subjects()
        elif choice == '2':
            Classroom.view_classes()
        elif choice == '3':
            Assignment.view_assignments_by_class()
        elif choice == '4':
            Marks.view_marks_by_student()
        elif choice == '5':
            Marks.view_student_performance()
        elif choice == '6':
            return
        else:
            print("Invalid choice")
            continue