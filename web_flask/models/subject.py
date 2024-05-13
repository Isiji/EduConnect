#!/usr/bin/python3
"""Subject module for the subject model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import uuid
class Subject(BaseModel, Base):
    """Subject model"""
    __tablename__ = 'subjects'
    id = Column(String(128), nullable=False, primary_key=True, unique=True, default='SU' + str(uuid.uuid4())[:6])
    name = Column(String(128), nullable=False)
    

    def __init__(self, *args, **kwargs):
        """initializes the subject"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the subject"""
        return "Subject: {}".format(self.name)
    
