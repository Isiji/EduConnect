#!/usr/bin/python3
"""Student module for the student model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from models.base_model import BaseModel, Base
import uuid

class Student(BaseModel, Base):
    """Student model"""
    __tablename__ = 'students'
    id = Column(String(128), nullable=False, primary_key=True, unique=True, default='ST' + str(uuid.uuid4())[:6])
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    school_id = Column(String(128), ForeignKey('schools.id'), nullable=False)
    school = relationship('School', back_populates='students')

    def __init__(self, first_name, last_name, email, password, ):
        """initializes the student"""
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __str__(self):
        """string representation of the student"""
        return "Student: {}".format(self.first_name)
    
    def __repr__(self):
        """string representation of the student"""
        return "Student: {}".format(self.first_name)
    
