#!/usr/bin/python3
"""Teacher module for the teacher model"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid
class Teacher(BaseModel, Base):
    """Teacher model"""
    __tablename__ = 'teachers'
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)


    def __init__(self, *args, **kwargs):
        """initializes the teacher"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the teacher"""
        return "Teacher: {} {}".format(self.first_name, self.last_name)

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
            school_id = input("Enter school id: ")
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
                teacher.school_id = input("Enter new school id: ")
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
    @staticmethod
    def show_school_teachers():
        """shows all teachers in a school"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()

        school_id = input("Enter school id: ")

        teachers = db_storage.all(Teacher)
        for teacher in teachers.values():
            if teacher.school_id == school_id:
                print(teacher)
                return
        print("No teachers found in this school")
