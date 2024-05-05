#!/usr/bin/python3
"""Admin module for the admin model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Admin(BaseModel, Base):
    """Admin model"""
    __tablename__ = 'admins'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    

    def __init__(self, *args, **kwargs):
        """initializes the admin"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the admin"""
        return "Admin: {} {}".format(self.first_name, self.last_name)
    
    #create for admin registration
    @staticmethod
    def register_admin():
        """registers an admin"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        admin = Admin(
            first_name = input("Enter first name: "),
            last_name = input("Enter last name: "),
            email = input("Enter email: "),
            password = input("Enter password: "),

        )
        db_storage.new(admin)
        db_storage.save()

        print("Admin registered successfully")

    #create for admin view all admins
    @staticmethod
    def view_all_admins():
        """view all admins"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        admins = db_storage.all('Admin')
        for admin in admins:
            print(admin)
        return admins
    
    #create for admin update admin
    @staticmethod
    def update_admin():
        """updates an admin"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()

        email = input("Enter email: ")
        password = input("Enter password: ")

        admins = db_storage.all('Admin')
        for admin in admins:
            if admin.email == email and admin.password == password:
                admin.email = input("Enter new email: ")
                admin.password = input("Enter new password: ")
                db_storage.save()
                print("Admin updated successfully")
                return
        print("Admin not found")