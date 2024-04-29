#!/bin/usr/python3
"""Parent module for the parent model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Parent(BaseModel, Base):
    """Parent model"""
    __tablename__ = 'parents'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    student_id = Column(String(60), ForeignKey('students.id'), nullable=False)
    
    def __init__(self, *args, **kwargs):
        """initializes the parent"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the parent"""
        return "Parent: {} {}".format(self.first_name, self.last_name)