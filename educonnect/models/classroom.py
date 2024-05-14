#!/usr/bin/python3

"""Class module for the class model"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import uuid
class Classroom(BaseModel, Base):
    """Class model"""
    __tablename__ = 'classes'
    id = Column(String(128), nullable=False, primary_key=True, unique=True, default='CL' + str(uuid.uuid4())[:6])
    name = Column(String(128), nullable=False, unique=True)
    school_id = Column(String(128), ForeignKey('schools.id'), nullable=False)
    school = relationship('School', back_populates='classes')
    assignments = relationship('Assignment', back_populates='classroom')

    def __init__(self, *args, **kwargs):
        """initializes the class"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the class"""
        return "Class: {}".format(self.name)

