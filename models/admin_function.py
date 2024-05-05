#!/usr/bin/python3
"""Admin function module for the admin function model"""

from models.subject import Subject
from models.parent import Parent
from models import utils
from models.engine.storage import DBStorage
from models.teacher import Teacher
from models.student import Student
from models.school import School
from models.classroom import Classroom
from models.admin_model import Admin
from models.engine import storage



#create a function for admin to add a new teacher to the database
def create_teacher():
    """creates a new teacher"""
    email = input("Enter teacher's email: ")
    password = input("Enter teacher's password: ")
    first_name = input("Enter teacher's first name: ")
    last_name = input("Enter teacher's last name: ")
    school_id = input("Enter teacher's school id: ")

    teacher = Teacher(email=email, password=password, first_name=first_name, last_name=last_name, school_id=school_id)
    storage.DBStorage().new(teacher)
    storage.DBStorage().save()
    print("Teacher added successfully")

#create a function for admin to add a new student to the database
def create_student():
    """creates a new student"""
    email = input("Enter student's email: ")
    password = input("Enter student's password: ")
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    school_id = input("Enter student's school id: ")
    classroom_id = input("Enter student's classroom id: ")

    student = Student(email=email, password=password, first_name=first_name, last_name=last_name, school_id=school_id, classroom_id=classroom_id)
    storage.DBStorage().new(student)
    storage.DBStorage().save()
    print("Student added successfully")

#create a function for admin to add a new school to the database
def create_school():
    """creates a new school"""
    name = input("Enter school's name: ")
    address = input("Enter school's address: ")
    phone = input("Enter school's phone number: ")

    school = School(name=name, address=address, phone=phone)
    storage.DBStorage().new(school)
    storage.DBStorage().save()
    print("School added successfully")

#create a function for admin to add a new classroom to the database
def create_classroom():
    """creates a new classroom"""
    name = input("Enter classroom's name: ")
    school_id = input("Enter classroom's school id: ")

    classroom = Classroom(name=name, school_id=school_id)
    storage.DBStorage().new(classroom)
    storage.DBStorage().save()
    print("Classroom added successfully")

#create a function for admin to add a new admin to the database
#create a function for admin to add a new parent to the database

def create_parent():
    """creates a new parent"""
    email = input("Enter parent's email: ")
    password = input("Enter parent's password: ")
    first_name = input("Enter parent's first name: ")
    last_name = input("Enter parent's last name: ")

    parent = Parent(email=email, password=password, first_name=first_name, last_name=last_name)
    storage.DBStorage().new(parent)
    storage.DBStorage().save()
    print("Parent added successfully")

#create a function for admin to add a new subject to the database
def create_subject():
    """creates a new subject"""
    name = input("Enter subject's name: ")
    classroom_id = input("Enter subject's classroom id: ")

    subject = Subject(name=name, classroom_id=classroom_id)
    storage.DBStorage().new(subject)
    storage.DBStorage().save()
    print("Subject added successfully")

#create a function for admin to delete a teacher from the database
def delete_teacher():
    """deletes a teacher"""
    teacher_id = input("Enter teacher's id: ")
    teacher = utils.get_all(Teacher)
    key = "Teacher." + teacher_id
    if key in teacher:
        storage.DBStorage().delete(teacher[key])
        storage.DBStorage().save()
        print("Teacher deleted successfully")
    else:
        print("Teacher not found")

#create a function for admin to delete a student from the database
def delete_student():
    """deletes a student"""
    student_id = input("Enter student's id: ")
    student = utils.get_all(Student)
    key = "Student." + student_id
    if key in student:
        storage.DBStorage().delete(student[key])
        storage.DBStorage().save()
        print("Student deleted successfully")
    else:
        print("Student not found")

#create a function for admin to delete a school from the database
def delete_school():
    """deletes a school"""
    school_id = input("Enter school's id: ")
    school = utils.get_all(School)
    key = "School." + school_id
    if key in school:
        storage.DBStorage().delete(school[key])
        storage.DBStorage().save()
        print("School deleted successfully")
    else:
        print("School not found")

#create a function for admin to delete a classroom from the database
def delete_classroom():
    """deletes a classroom"""
    classroom_id = input("Enter classroom's id: ")
    classroom = utils.get_all(Classroom)
    key = "Classroom." + classroom_id
    if key in classroom:
        storage.DBStorage().delete(classroom[key])
        storage.DBStorage().save()
        print("Classroom deleted successfully")
    else:
        print("Classroom not found")

#create a function for admin to delete an admin from the database
def delete_admin():
    """deletes an admin"""
    admin_id = input("Enter admin's id: ")
    admin = utils.get_all(Admin)
    key = "Admin." + admin_id
    if key in admin:
        storage.DBStorage().delete(admin[key])
        storage.DBStorage().save()
        print("Admin deleted successfully")
    else:
        print("Admin not found")

#create a function for admin to delete a parent from the database
def delete_parent():
    """deletes a parent"""
    parent_id = input("Enter parent's id: ")
    parent = utils.get_all(Parent)
    key = "Parent." + parent_id
    if key in parent:
        storage.DBStorage().delete(parent[key])
        storage.DBStorage().save()
        print("Parent deleted successfully")
    else:
        print("Parent not found")