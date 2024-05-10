#!/usr/bin/python3
"""Assignment module for the assignment model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Assignment(BaseModel, Base):
    """Assignment model"""
    __tablename__ = 'assignments'
    id = Column(String(100), nullable=False, primary_key=True, unique=True)
    assignment_name = Column(String(128), nullable=False)
    classroom = Column(String(128), nullable=False)
    due_date = Column(String(128), nullable=False)
    description = Column(String(128), nullable=False)


    def __init__(self, *args, **kwargs):
        """initializes the assignment"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the assignment"""
        return "Assignment: {}".format(self.name)
    
    
    @staticmethod
    def view_assignments():
        """view all assignments"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        
        assignments = db_storage.all('Assignment')
        for assignment in assignments:
            print(assignment)