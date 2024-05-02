#!/usr/bin/python3
"""Admin session module for the admin session model"""

from models.admin_model import Admin
from models.student import Student
from models.teacher import Teacher
from models.school import School
from models.classroom import Classroom

#create a function that enters into admin session and allows admin to do his functions
def admin_session():
    """this function is for the admin functionality"""
    print("Welcome the EduConnect  Admin Panel")
    print(" ")

    while True:
        print("Select an option")
        print("1. Register a new admin")
        print("2. Register student")
        print("3. Register teacher")
        print("4. Register school")
        print("5. Register classroom")
        print("6. View all students")
        print("7. View all teachers")
        print("8. View all schools")
        print("9. View all classrooms")
        print("10. Delete student")
        print("11. Delete teacher")
        print("12. Delete school")
        print("13. Delete classroom")
        print("14. Exit")

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
            school = School()
            school.register_school()

        elif choice == 5:
            classroom = Classroom()
            classroom.register_classroom()

        elif choice == 6:
            Student.view_all_students()

        elif choice == 7:
            Teacher.view_all_teachers()

        elif choice == 8:
            School.view_all_schools()

        elif choice == 9:
            Classroom.view_all_classrooms()

        elif choice == 10:
            student = Student()
            student.delete_student()

        elif choice == 11:
            teacher = Teacher()
            teacher.delete_teacher()

        elif choice == 12:
            school = School()
            school.delete_school()

        elif choice == 13:
            classroom = Classroom()
            classroom.delete_classroom()

        elif choice == 14:
            print("Thank you for using the EduConnect Admin Panel")
            break
