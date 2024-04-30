#!/usr/bin/python3
"""Utility module for the models stores all the functions to be used in the models"""
from models.engine import storage
from models.admin import Admin
from models.teacher import Teacher
from models.student import Student
from models.school import School
from models.classroom import Classroom
from models.base_model import BaseModel
from models.parent import Parent
from models.subject import Subject

# create a dictionary of all objects
def get_all(cls):
    """Returns a dictionary of all objects"""
    classes = [Teacher, Student, School, Classroom, Parent, Subject]
    objects = {}
    if cls:
        if cls in classes:
            for obj in storage.all(cls).values():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
    else:
        for c in classes:
            for obj in storage.all(c).values():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
    return objects

# create a new object
def create(cls):
    """Creates a new instance of a class"""
    if not cls:
        return "** class name missing **"
    if cls not in ['Teacher', 'Student', 'School', 'Classroom', 'Parent', 'Subject']:
        return "** class doesn't exist **"
    new = eval(cls)()
    new.save()
    return new.id

# show an object
def show(cls, id):
    """Prints the string representation of an instance"""
    if not cls:
        return "** class name missing **"
    if cls not in ['Teacher', 'Student', 'School', 'Classroom', 'Parent', 'Subject']:
        return "** class doesn't exist **"
    if not id:
        return "** instance id missing **"
    key = "{}.{}".format(cls, id)
    if key not in storage.all():
        return "** no instance found **"
    return storage.all()[key]

# delete an object
def delete(cls, id):
    """Deletes an instance based on the class name and id"""
    if not cls:
        return "** class name missing **"
    if cls not in ['Teacher', 'Student', 'School', 'Classroom', 'Parent', 'Subject']:
        return "** class doesn't exist **"
    if not id:
        return "** instance id missing **"
    key = "{}.{}".format(cls, id)
    if key not in storage.all():
        return "** no instance found **"
    del storage.all()[key]
    storage.save()
    return

# update an object
def update(cls, id, attr, value):
    """Updates an instance based on the class name and id"""
    if not cls:
        return "** class name missing **"
    if cls not in ['Teacher', 'Student', 'School', 'Classroom', 'Parent', 'Subject']:
        return "** class doesn't exist **"
    if not id:
        return "** instance id missing **"
    key = "{}.{}".format(cls, id)
    if key not in storage.all():
        return "** no instance found **"
    obj = storage.all()[key]
    setattr(obj, attr, value)
    obj.save()
    return

# count the number of objects
def count(cls):
    """Counts the number of objects"""
    if not cls:
        return "** class name missing **"
    if cls not in ['Teacher', 'Student', 'School', 'Classroom', 'Parent', 'Subject']:
        return "** class doesn't exist **"
    return len(storage.all(cls).values())

# get the class name
def get_class_name(cls):
    """Returns the class name"""
    if not cls:
        return "** class name missing **"
    if cls not in ['Teacher', 'Student', 'School', 'Classroom', 'Parent', 'Subject']:
        return "** class doesn't exist **"
    return cls

# get the class name
def get_class_name(cls):
    """Returns the class name"""
    if not cls:
        return "** class name missing **"
    if cls not in ['Teacher', 'Student', 'School', 'Classroom', 'Parent', 'Subject']:
        return "** class doesn't exist **"
    return cls
