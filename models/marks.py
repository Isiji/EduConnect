#!/usr/bin/python3
"""Marks module for the marks model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Marks(BaseModel, Base):
    """Marks model"""
    __tablename__ = 'marks'
    student_id = Column(String(60), ForeignKey('students.id'), nullable=False)
    assignment_id = Column(String(60), ForeignKey('assignments.id'), nullable=False)
    grade = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes the marks"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the marks"""
        return "Marks: {}".format(self.grade)
    
    #inputing marks   
    @staticmethod
    def register_marks():
        """registers marks"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        student_id = input("Enter student id: ")
        assignment_id = input("Enter assignment id: ")
        grade = input("Enter grade: ")

        marks = Marks(
            student_id = student_id,
            assignment_id = assignment_id,
            grade = grade
        )
        db_storage.new(marks)
        db_storage.save()

        print("Marks registered successfully")

    #viewing marks
    @staticmethod
    def view_marks():
        """view all marks"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        marks = db_storage.all(Marks)
        for mark in marks.values():
            print(mark)

    #delete marks
    @staticmethod
    def delete_marks():
        """delete a mark"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        mark_id = input("Enter mark id: ")
        marks = db_storage.all(Marks)
        for mark in marks.values():
            if mark.id == mark_id:
                db_storage.delete(mark)
                db_storage.save()
                print("Mark deleted successfully")
                return
        print("Mark not found")

    #view marks by student
    @staticmethod
    def view_marks_by_student():
        """view all marks by student"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        student_id = input("Enter student id: ")
        marks = db_storage.all(Marks)
        for mark in marks.values():
            if mark.student_id == student_id:
                print(mark)

    #view marks by assignment
    @staticmethod
    def view_marks_by_assignment():
        """view all marks by assignment"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        assignment_id = input("Enter assignment id: ")
        marks = db_storage.all(Marks)
        for mark in marks.values():
            if mark.assignment_id == assignment_id:
                print(mark)

    #update marks
    @staticmethod
    def update_marks():
        """update marks"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        mark_id = input("Enter mark id: ")
        marks = db_storage.all(Marks)
        for mark in marks.values():
            if mark.id == mark_id:
                mark.grade = input("Enter new grade: ")
                db_storage.save()
                print("Mark updated successfully")
                return
        print("Mark not found")

    #view marks by class
    @staticmethod
    def view_marks_by_class():
        """view all marks by class"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        class_id = input("Enter class id: ")
        marks = db_storage.all(Marks)
        for mark in marks.values():
            if mark.class_id == class_id:
                print(mark)

    #view marks by subject
    @staticmethod
    def view_marks_by_subject():
        """view all marks by subject"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        subject_id = input("Enter subject id: ")
        marks = db_storage.all(Marks)
        for mark in marks.values():
            if mark.subject_id == subject_id:
                print(mark)

