#!/usr/bin/python3
"""School module for the school model"""
import models
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from models.admin import Admin
from models.teacher import Teacher
from models.student import Student
from models.classroom import Classroom

Base = declarative_base()

class School(BaseModel, Base):
    """School model"""
    __tablename__ = 'schools'
    id = Column(String(15), nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    county = Column(String(128), nullable=False)
    phone = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    website = Column(String(128))
    #admin_id = Column(String(15), ForeignKey('admins.id'), nullable=False)
    #admin = relationship("Admin", back_populates="school")
    teachers = relationship("Teacher", back_populates="school")
    students = relationship("Student", back_populates="school")
    classrooms = relationship("Classroom", back_populates="school")



    def __init__(self, *args, **kwargs):
        """initializes the school"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the school"""
        return "School: {}".format(self.name)
    
    