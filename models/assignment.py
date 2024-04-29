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
    name = Column(String(128), nullable=False)
    subject_id = Column(String(60), ForeignKey('subjects.id'), nullable=False)
    subject = relationship('Subject', back_populates='assignments')
    teacher_id = Column(String(60), ForeignKey('teachers.id'), nullable=False)
    teacher = relationship('Teacher', back_populates='assignments')
    class_id = Column(String(60), ForeignKey('classes.id'), nullable=False)
    class_ = relationship('Class', back_populates='assignments')
    due_date = Column(String(128), nullable=False)
    description = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes the assignment"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the assignment"""
        return "Assignment: {}".format(self.name)
    
    