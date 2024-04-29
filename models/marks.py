#!/usr/bin/python3
"""Marks module for the marks model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Marks(BaseModel, Base):
    """Marks model"""
    __tablename__ = 'marks'
    student_id = Column(String(60), ForeignKey('students.id'), nullable=False)
    assignment_id = Column(String(60), ForeignKey('assignments.id'), nullable=False)
    grade = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes the marks"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the marks"""
        return "Marks: {}".format(self.grade)
    
     
