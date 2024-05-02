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