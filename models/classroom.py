#!/usr/bin/python3

"""Class module for the class model"""
from models import base_model
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Classroom(BaseModel, Base):
    """Class model"""
    __tablename__ = 'classes'
    id = Column(String(25), nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    teacher_id = Column(String(60), ForeignKey('teachers.id'), nullable=False)
    school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)
    def __init__(self, *args, **kwargs):
        """initializes the class"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the class"""
        return "Class: {}".format(self.name)

