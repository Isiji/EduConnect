#!/usr/bin/python3

"""Class module for the class model"""
from models import base_model
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import uuid
class Classroom(BaseModel, Base):
    """Class model"""
    __tablename__ = 'classes'
    id = Column(String(120), nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    

    def __init__(self, *args, **kwargs):
        """initializes the class"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the class"""
        return "Class: {}".format(self.name)

    @staticmethod
    def register_classroom():
        """registers a class"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        short_id = str(uuid.uuid4())[:8]
        class_id = short_id
        teacher_id = input("Enter teacher id: ")
        school_id = input("Enter school id: ")
        class_name = input("Enter class name: ")

        classroom = Classroom(
            id = class_id,
            name = class_name,
            teacher_id = teacher_id,
            school_id = school_id
        )
        db_storage.new(classroom)
        db_storage.save()

        print("Class registered successfully")
    #for view classes
    @staticmethod
    def view_classes():
        """view all classes"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        classes = db_storage.all(Classroom)
        for class_ in classes.values():
            print(class_)

    #for view classes by teacher
    @staticmethod
    def view_classes_by_teacher():
        """view all classes by teacher"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        teacher_id = input("Enter teacher id: ")
        classes = db_storage.all(Classroom)
        for class_ in classes.values():
            if class_.teacher_id == teacher_id:
                print(class_)
    #for view classes by school
    @staticmethod
    def view_classes_by_school():
        """view all classes by school"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        school_id = input("Enter school id: ")
        classes = db_storage.all(Classroom)
        for class_ in classes.values():
            if class_.school_id == school_id:
                print(class_)

    #for update class
    @staticmethod
    def update_class():
        """updates a class"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()

        class_id = input("Enter class id: ")
        classes = db_storage.all(Classroom)
        for class_ in classes.values():
            if class_.id == class_id:
                class_.name = input("Enter new class name: ")
                class_.teacher_id = input("Enter new teacher id: ")
                class_.school_id = input("Enter new school id: ")
                db_storage.save()
                print("Class updated successfully")
                return
        print("Class not found")
        return
    
    #for delete class
    @staticmethod
    def delete_class():
        """deletes a class"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()

        class_id = input("Enter class id: ")
        classes = db_storage.all(Classroom)
        for class_ in classes.values():
            if class_.id == class_id:
                db_storage.delete(class_)
                db_storage.save()
                print("Class deleted successfully")
                return
        print("Class not found")
        return
    
    #for show class
    @staticmethod
    def show_class():
        """shows a specific class"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()

        class_id = input("Enter class id: ")
        classes = db_storage.all(Classroom)
        for class_ in classes.values():
            if class_.id == class_id:
                print(class_)
                return
        print("Class not found")
        return
    
    