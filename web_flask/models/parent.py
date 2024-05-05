#!/bin/usr/python3
"""Parent module for the parent model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Parent(BaseModel, Base):
    """Parent model"""
    __tablename__ = 'parents'
    id = Column(String(25), nullable=False, primary_key=True, unique=True)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)

    
    def __init__(self, *args, **kwargs):
        """initializes the parent"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the parent"""
        return "Parent: {} {}".format(self.first_name, self.last_name)
    
    @classmethod
    def register_parent(cls):
        """register a parent"""
        print("Register a parent")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        parent = cls(first_name=first_name, last_name=last_name, email=email, password=password)
        parent.save()