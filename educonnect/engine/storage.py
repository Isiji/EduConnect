#!/usr/bin/python3
"""Database storage module"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from educonnect.models.teacher import Teacher
from educonnect.models.student import Student
from educonnect.models.school import School
from educonnect.models.classroom import Classroom
from educonnect.models.parent import Parent
from educonnect.models.marks import Marks
from educonnect.models.assignment import Assignment
from educonnect.models.subject import Subject
from educonnect.models.admin_model import Admin
from educonnect.models.base_model import Base
import sys
from sqlalchemy.exc import SQLAlchemyError
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
        objects = {}
        try:
            if cls is not None:
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    key = "{}.{}".format(cls.__name__, obj.id)
                    objects[key] = obj
            else:
                classes = [Admin, Teacher, Student, School, Classroom, Parent, Marks, Assignment, Subject]
                for cls in classes:
                    query_result = self.__session.query(cls).all()
                    for obj in query_result:
                        key = "{}.{}".format(cls.__name__, obj.id)
                        objects[key] = obj
        except SQLAlchemyError as e:
            print("An Error Occurred:", e)
        return objects

    
    def new(self, obj):
        """Adds the object to the current database session"""
        try:
            self.__session.add(obj)
        except SQLAlchemyError as e:
            print("An Error Occured:", e)

    def save(self):
        """Commits all changes to the database"""
        try:
            self.__session.commit()
        except SQLAlchemyError as e:
            print("An Error Occured:", e)
        
    def get(self, model_class, object_id):
            """Retrieve an object from the database by its ID"""
            return self.__session.query(model_class).filter_by(id=object_id).first()

    def delete(self, obj=None):
        """Deletes the object from the current database session"""
        try:
            if obj:
                self.__session.delete(obj)
        except SQLAlchemyError as e:
            print("An Error Occured:", e)

    def reload(self):
        """Creates all tables in the database"""
        try:
            Base.metadata.create_all(self.__engine)
            session_factory = sessionmaker(bind=self.__engine)
            self.__session = scoped_session(session_factory)
            self.__session.configure(bind=self.__engine)
        except SQLAlchemyError as e:
            print("An Error Occured:", e)


    def close(self):
        """Closes the current session"""
        try:    
            self.__session.remove()
            self.__session.close()
        except SQLAlchemyError as e:
            print("An Error Occured:", e)