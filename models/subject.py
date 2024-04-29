#!/usr/bin/python3
"""Subject module for the subject model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Subject(BaseModel, Base):
    """Subject model"""
    __tablename__ = 'subjects'
    name = Column(String(128), nullable=False)
    teacher_id = Column(String(60), ForeignKey('teachers.id'), nullable=False)
    teacher = relationship('Teacher', back_populates='subjects')
    classes = relationship('Class', back_populates='subject')
    assignments = relationship('Assignment', back_populates='subject')

    def __init__(self, *args, **kwargs):
        """initializes the subject"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the subject"""
        return "Subject: {}".format(self.name)