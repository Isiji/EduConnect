#!/usr/bin/python3
"""Marks module for the marks model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from educonnect.models.base_model import BaseModel, Base
class Marks(BaseModel, Base):
    """Marks model"""
    __tablename__ = 'marks'
    id = Column(String(128), nullable=False, primary_key=True, unique=True, index=True)
    grade = Column(String(8), nullable=False)


    def __init__(self, *args, **kwargs):
        """initializes the marks"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the marks"""
        return "Marks: {}".format(self.grade)
    