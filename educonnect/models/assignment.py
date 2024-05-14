#!/usr/bin/python3
"""Assignment module for the assignment model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from educonnect.models.base_model import BaseModel, Base

class Assignment(BaseModel, Base):
    """Assignment model"""
    __tablename__ = 'assignments'
    id = Column(String(128), nullable=False, primary_key=True, unique=True, default='AS' + str(uuid.uuid4())[:6], index=True)
    assignment_name = Column(String(128), nullable=False)
    due_date = Column(String(128), nullable=False)
    description = Column(String(128), nullable=False)
    classroom_id = Column(String(128), ForeignKey('classes.id'), nullable=False)
    classroom = relationship('Classroom', back_populates='assignments')
    def __init__(self, *args, **kwargs):
        """initializes the assignment"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the assignment"""
        return "Assignment: {}".format(self.name)