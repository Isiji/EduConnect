#!/usr/bin/python3
"""Assignment module for the assignment model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Assignment(BaseModel, Base):
    """Assignment model"""
    __tablename__ = 'assignments'
    id = Column(String(15), nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    subject_id = Column(String(60), ForeignKey('subjects.id'), nullable=False)
    teacher_id = Column(String(60), ForeignKey('teachers.id'), nullable=False)
    class_id = Column(String(60), ForeignKey('classes.id'), nullable=False)
    due_date = Column(String(128), nullable=False)
    description = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes the assignment"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the assignment"""
        return "Assignment: {}".format(self.name)
    
    