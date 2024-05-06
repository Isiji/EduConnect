#!/usr/bin/python3
"""Student module for the student model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
import uuid
class Student(BaseModel, Base):
    """Student model"""
    __tablename__ = 'students'
    id = Column(String(70), nullable=False, primary_key=True, unique=True)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes the student"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the student"""
        return "Student: {} {}".format(self.first_name, self.last_name)
    @staticmethod
    def register_student():
        """registers a student"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        short_id = str(uuid.uuid4())[:8]
        student = Student(
            id = short_id,
            first_name = input("Enter first name: "),
            last_name = input("Enter last name: "),
            email = input("Enter email: "),
            password = input("Enter password: "),
            
        )
        db_storage.new(student)
        db_storage.save()

    @staticmethod
    def view_all_students():
        """view all students"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        students = db_storage.all('Student')
        for student in students:
            print(student)
        return students
    
    #view students by class
    @staticmethod
    def view_students_by_class():
        """view all students by class"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        class_id = input("Enter class id: ")
        students = db_storage.all('Student')
        for student in students:
            if student.class_id == class_id:
                print(student)