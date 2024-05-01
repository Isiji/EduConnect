#!/usr/bin/python3
"""Admin module for the admin model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Admin(BaseModel, Base):
    """Admin model"""
    __tablename__ = 'admins'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)
    

    def __init__(self, *args, **kwargs):
        """initializes the admin"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the admin"""
        return "Admin: {} {}".format(self.first_name, self.last_name)