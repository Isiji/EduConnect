#!/usr/bin/python3
"""School module for the school model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class School(BaseModel, Base):
    """School model"""
    __tablename__ = 'schools'
    name = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    state = Column(String(128), nullable=False)
    zip_code = Column(String(128), nullable=False)
    phone = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    admins = relationship('Admin', back_populates='school')
    teachers = relationship('Teacher', back_populates='school')
    students = relationship('Student', back_populates='school')

    def __init__(self, *args, **kwargs):
        """initializes the school"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the school"""
        return "School: {}".format(self.name)
    
    