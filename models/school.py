#!/usr/bin/python3
"""School module for the school model"""
import models
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import uuid
class School(BaseModel, Base):
    """School model"""
    __tablename__ = 'schools'
    id = Column(String(15), nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    county = Column(String(128), nullable=False)
    phone = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    website = Column(String(128))



    def __init__(self, *args, **kwargs):
        """initializes the school"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the school"""
        return "School: {}".format(self.name)
    
    
    @staticmethod
    def register_school():
        """registers a school"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        short_id = str(uuid.uuid4())[:8]
        school = School(
            id = short_id,
            name = input("Enter school name: "),
            address = input("Enter school address: "),
            city = input("Enter city: "),
            county = input("Enter county: "),
            phone = input("Enter phone: "),
            email = input("Enter email: "),
            website = input("Enter website: ")
        )
        db_storage.new(school)
        db_storage.save()

        print("School registered successfully")