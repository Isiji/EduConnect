#!/usr/bin/python3
"""Subject module for the subject model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Subject(BaseModel, Base):
    """Subject model"""
    __tablename__ = 'subjects'
    id = Column(String(15), nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    

    def __init__(self, *args, **kwargs):
        """initializes the subject"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the subject"""
        return "Subject: {}".format(self.name)
    
    @staticmethod
    def register_subject():
        """registers a subject"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        subject_id = input("Enter subject id: ")
        subject_name = input("Enter subject name: ")

        subject = Subject(
            id = subject_id,
            name = subject_name,
        )
        db_storage.new(subject)
        db_storage.save()

        print("Subject registered successfully")
    #viewing subjects
    @staticmethod
    def view_subjects():
        """view all subjects"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        subjects = db_storage.all(Subject)
        for subject in subjects.values():
            print(subject)

    #delete subject
    @staticmethod
    def delete_subject():
        """delete a subject"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        subject_id = input("Enter subject id: ")
        subjects = db_storage.all(Subject)
        for subject in subjects.values():
            if subject.id == subject_id:
                db_storage.delete(subject)
                db_storage.save()
                print("Subject deleted successfully")
                return
        print("Subject not found")

        
        #view subject by class
