#!/usr/bin/python3
"""Database storage module"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.teacher import Teacher
from models.student import Student
from models.school import School
from models.classroom import Classroom
import sys
class DBStorage:
    """Database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the database storage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                       .format('root', 'Password123.', 'localhost', 'EduConnect'),
                                       pool_pre_ping=True)
        if 'test' in sys.argv:
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def all(self, cls=None):
        """Returns a dictionary of all objects"""
        classes = [Teacher, Student, School, Classroom]
        objects = {}
        if cls:
            if cls in classes:
                for obj in self.__session.query(cls).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        else:
            for c in classes:
                for obj in self.__session.query(c).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes the object from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(session_factory)
        self.__session.configure(bind=self.__engine)

    def close(self):
        """Closes the current session"""
        self.__session.remove()
        self.__session.close()