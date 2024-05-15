import os

class Config:
    """Configurations for the app"""
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:Password123.@localhost/EduConnect'