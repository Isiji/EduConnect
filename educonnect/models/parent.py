#!/bin/usr/python3
"""Parent module for the parent model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from educonnect.models.base_model import BaseModel, Base
class Parent(BaseModel, Base):
    """Parent model"""
    __tablename__ = 'parents'
    parent_id = Column(String(128), nullable=False, primary_key=True, unique=True, default='PA' + str(uuid.uuid4())[:6])
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    image_file = Column(String(128), nullable=False, default='default.jpg')    
    password = Column(String(128), nullable=False)
    school_id = Column(String(128), ForeignKey('schools.id'), nullable=False)
    school = relationship('School', back_populates='parents')

    
    def __init__(self, *args, **kwargs):
        """initializes the parent"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the parent"""
        return "Parent: {} {}".format(self.first_name, self.last_name)
    
