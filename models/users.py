#!/usr/bin/python3
"""This module contains the User class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table, Integer
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship

#create a class for the table user which will have data for teachers, admin, students and parents and will be used to login
#and access the system. this class will relate with other tables, and will affect other tables as well when a change is made to it.
class User(BaseModel, Base):
    """This class defines the User class"""
    __tablename__ = "users"
    id = Column(String(60), primary_key=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    phone_number = Column(String(128), nullable=False)
    user_type = Column(String(128), nullable=False)
    user_id = Column(String(128), nullable=False, unique=True)

    def __init__(self, *args, **kwargs):
        """This method initializes an instance"""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")

    def __str__(self):
        """This method returns a string representation of an instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
    