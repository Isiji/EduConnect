#!/usr/bin/python3
"""Admin module for the admin model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from educonnect.models.base_model import BaseModel, Base

class Admin(BaseModel, Base):
    """Admin model"""
    __tablename__ = 'admins'
    id = Column(String(128), nullable=False, primary_key=True, unique=True, default='AD' + str(uuid.uuid4())[:6])
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    image_file = Column(String(128), nullable=False, default='default.jpg')
    school_id = Column(String(128), ForeignKey('schools.id'), nullable=False)
    school = relationship('School', back_populates='admins')
    def __init__(self, *args, **kwargs):
        """initializes the admin"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the admin"""
        return "Admin: {} {}".format(self.first_name, self.last_name)
    
