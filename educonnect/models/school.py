#!/usr/bin/python3
"""School module for the school model"""
from sqlalchemy import Column, String, ForeignKey, Integer, Index
from sqlalchemy.orm import relationship
import uuid
from educonnect.models.base_model import BaseModel, Base

class School(BaseModel, Base):
    """School model"""
    __tablename__ = 'schools'
    id = Column(String(128), nullable=False, primary_key=True, unique=True, default='SC' + str(uuid.uuid4())[:6])
    name = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    county = Column(String(128))
    phone = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    website = Column(String(128), nullable=True)
    password = Column(String(128), nullable=False)
    admins = relationship('Admin', back_populates='school')
    classes = relationship('Classroom', back_populates='school')
    parents = relationship('Parent', back_populates='school')
    students = relationship('Student', back_populates='school')
    teachers = relationship('Teacher', back_populates='school')
    


    def __init__(self, *args, **kwargs):
        """initializes the school"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the school"""
        return "School: {}".format(self.name)
    
    