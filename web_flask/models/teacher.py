#!/usr/bin/python3
"""Teacher module for the teacher model"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid
class Teacher(BaseModel, Base):
    """Teacher model"""
    __tablename__ = 'teachers'
    id = Column(String(120), nullable=False, primary_key=True, default=uuid.uuid4().hex)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    image_file = Column(String(128), nullable=False, default='default.jpg')
    password = Column(String(128), nullable=False)


    def __init__(self, first_name, last_name, email, password, image_file='default.jpg'):
        """initializes the teacher"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.image_file = image_file
        self.password = password
    def __str__(self):
        """string representation of the teacher"""
        return "Teacher: {} {}".format(self.id, self.first_name, self.last_name,self.email)

    @staticmethod
    def register_teacher():
        """registers a teacher"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        short_id = str(uuid.uuid4())[:8]
        
        teacher = Teacher(
            id = short_id,
            first_name = input("Enter first name: "),
            last_name = input("Enter last name: "),
            email = input("Enter email: "),
            password = input("Enter password: "),
        )
        db_storage.new(teacher)
        db_storage.save()

        print("Teacher registered successfully")

    @staticmethod
    def login_teacher():
        """logs in a teacher"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()

        email = input("Enter email: ")
        password = input("Enter password: ")

        teachers = db_storage.all(Teacher)
        for teacher in teachers.values():
            if teacher.email == email and teacher.password == password:
                print("Login successful")
                return
        print("Login failed. Incorrect email or password!")

    #updates a teacher with new information
    @staticmethod
    def update_teacher():
        """updates a teacher"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()

        email = input("Enter email: ")
        password = input("Enter password: ")

        teachers = db_storage.all(Teacher)
        for teacher in teachers.values():
            if teacher.email == email and teacher.password == password:
                teacher.first_name = input("Enter new first name: ")
                teacher.last_name = input("Enter new last name: ")
                teacher.email = input("Enter new email: ")
                teacher.password = input("Enter new password: ")
                db_storage.save()
                print("Teacher updated successfully")
                return
        print("Teacher not found. Incorrect details")

    #deletes a teacher
    @staticmethod
    def delete_teacher():
        """deletes a teacher"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()

        email = input("Enter email: ")
        password = input("Enter password: ")

        teachers = db_storage.all(Teacher)
        for teacher in teachers.values():
            if teacher.email == email and teacher.password == password:
                db_storage.delete(teacher)
                db_storage.save()
                print("Teacher deleted successfully")
                return
        print("Teacher not found. Incorrect details")

    #shows all teachers
    @staticmethod
    def view_all_teachers():
        """shows all teachers"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()

        teachers = db_storage.all(Teacher)
        for teacher in teachers.values():
            print(teacher)

    #shows a specific teacher
    @staticmethod
    def show_teacher():
        """shows a specific teacher"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()

        email = input("Enter email: ")

        teachers = db_storage.all(Teacher)
        for teacher in teachers.values():
            if teacher.email == email:
                print(teacher)
                return
        print("Teacher not found. Incorrect details")

    #shows all teachers in a school
