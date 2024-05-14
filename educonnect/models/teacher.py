#!/usr/bin/python3
"""Teacher module for the teacher model"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid
class Teacher(BaseModel, Base):
    """Teacher model"""
    __tablename__ = 'teachers'
    id = Column(String(128), nullable=False, primary_key=True, unique=True, default='TE' + str(uuid.uuid4())[:6])
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    image_file = Column(String(128), nullable=False, default='default.jpg')
    password = Column(String(128), nullable=False)
    school_id = Column(String(128), ForeignKey('schools.id'), nullable=False)
    school = relationship('School', back_populates='teachers')


    def __init__(self, *args, **kwargs):
        """initializes the teacher"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the teacher"""
        return "Teacher: {} {}".format(self.id, self.first_name, self.last_name,self.email)

