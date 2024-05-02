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
    id = Column(String(25), nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    teacher_id = Column(String(60), ForeignKey('teachers.id'), nullable=False)
    school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)

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