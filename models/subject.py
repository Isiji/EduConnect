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
    teacher_id = Column(String(60), ForeignKey('teachers.id'), nullable=False)
    class_id = Column(String(60), ForeignKey('classes.id'), nullable=False)
    student_id = Column(String(60), ForeignKey('students.id'), nullable=False)
    

    def __init__(self, *args, **kwargs):
        """initializes the subject"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the subject"""
        return "Subject: {}".format(self.name)