#!/usr/bin/python3
"""Student module for the student model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Student(BaseModel, Base):
    """Student model"""
    __tablename__ = 'students'
    id = Column(String(25), nullable=False, primary_key=True, unique=True)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)
    class_id = Column(String(60), ForeignKey('classes.id'), nullable=False)
    

    def __init__(self, *args, **kwargs):
        """initializes the student"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the student"""
        return "Student: {} {}".format(self.first_name, self.last_name)
    
    def register_student(self):
        """registers a student"""
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
        self.email = input("Enter email: ")
        self.password = input("Enter password: ")
        self.school_id = input("Enter school id: ")
        self.class_id = input("Enter class id: ")
        self.save()

    def view_all_students():
        """views all students"""
        all_students = Student.query.all()
        for student in all_students:
            print(student)
        return all_students
    