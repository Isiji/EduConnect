#!/usr/bin/python3
"""Assignment module for the assignment model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Assignment(BaseModel, Base):
    """Assignment model"""
    __tablename__ = 'assignments'
    id = Column(String(100), nullable=False, primary_key=True, unique=True)
    assignment_name = Column(String(128), nullable=False)
    classroom = Column(String(128), nullable=False)
    due_date = Column(String(128), nullable=False)
    description = Column(String(128), nullable=False)
    
    

    def __init__(self, *args, **kwargs):
        """initializes the assignment"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the assignment"""
        return "Assignment: {}".format(self.name)
    
    
    #create for assignment registration
    @staticmethod
    def post_assignment():
        """registers an assignment"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        assignment_id = input("Enter assignment id: ")
        assignment_name = input("Enter assignment name: ")
        subject_id = input("Enter subject id: ")
        teacher_id = input("Enter teacher id: ")
        class_id = input("Enter class id: ")
        due_date = input("Enter due date: ")
        description = input("Enter description: ")

        assignment = Assignment(
            id = assignment_id,
            name = assignment_name,
            subject_id = subject_id,
            teacher_id = teacher_id,
            class_id = class_id,
            due_date = due_date,
            description = description
        )
        db_storage.new(assignment)
        db_storage.save()

        print("Assignment posted successfully")

    #create for assignment view all assignments
    @staticmethod
    def view_assignments():
        """view all assignments"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        assignments = db_storage.all(Assignment)
        for assignment in assignments.values():
            print(assignment)

    #create for assignment update assignment
    @staticmethod
    def update_assignment():
        """updates an assignment"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()

        assignment_id = input("Enter assignment id: ")
        assignments = db_storage.all(Assignment)
        for assignment in assignments.values():
            if assignment.id == assignment_id:
                assignment.name = input("Enter new assignment name: ")
                assignment.subject_id = input("Enter new subject id: ")
                assignment.teacher_id = input("Enter new teacher id: ")
                assignment.class_id = input("Enter new class id: ")
                assignment.due_date = input("Enter new due date: ")
                assignment.description = input("Enter new description: ")
                db_storage.save()
                print("Assignment updated successfully")
                return
            
        print("Assignment not found")

    #create for assignment delete assignment
    @staticmethod
    def delete_assignment():
        """delete an assignment"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        assignment_id = input("Enter assignment id: ")
        assignments = db_storage.all(Assignment)
        for assignment in assignments.values():
            if assignment.id == assignment_id:
                db_storage.delete(assignment)
                db_storage.save()
                print("Assignment deleted successfully")
                return
            
        print("Assignment not found")

    #view assignments by class
    @staticmethod
    def view_assignments_by_class():
        """view all assignments by class"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        class_id = input("Enter class id: ")
        assignments = db_storage.all(Assignment)
        for assignment in assignments.values():
            if assignment.class_id == class_id:
                print(assignment)

    #view assignments by teacher
    @staticmethod
    def view_assignments_by_teacher():
        """view all assignments by teacher"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        teacher_id = input("Enter teacher id: ")
        assignments = db_storage.all(Assignment)
        for assignment in assignments.values():
            if assignment.teacher_id == teacher_id:
                print(assignment)

    #view assignments by subject
    @staticmethod
    def view_assignments_by_subject():
        """view all assignments by subject"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        subject_id = input("Enter subject id: ")
        assignments = db_storage.all(Assignment)
        for assignment in assignments.values():
            if assignment.subject_id == subject_id:
                print(assignment)

    #view assignments by due date
    @staticmethod
    def view_assignments_by_due_date():
        """view all assignments by due date"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        due_date = input("Enter due date: ")
        assignments = db_storage.all(Assignment)
        for assignment in assignments.values():
            if assignment.due_date == due_date:
                print(assignment)

    #view assignments by class and subject
    @staticmethod
    def view_assignments_by_class_and_subject():
        """view all assignments by class and subject"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        class_id = input("Enter class id: ")
        subject_id = input("Enter subject id: ")
        assignments = db_storage.all(Assignment)
        for assignment in assignments.values():
            if assignment.class_id == class_id and assignment.subject_id == subject_id:
                print(assignment)

    #view assignments by class and teacher  
    @staticmethod
    def view_assignments_by_class_and_teacher():
        """view all assignments by class and teacher"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        class_id = input("Enter class id: ")
        teacher_id = input("Enter teacher id: ")
        assignments = db_storage.all(Assignment)
        for assignment in assignments.values():
            if assignment.class_id == class_id and assignment.teacher_id == teacher_id:
                print(assignment)

    #view assignments by class and due date
    @staticmethod
    def view_assignments_by_class_and_due_date():
        """view all assignments by class and due date"""
        from models.engine.storage import DBStorage
        db_storage = DBStorage()
        class_id = input("Enter class id: ")
        due_date = input("Enter due date: ")
        assignments = db_storage.all(Assignment)
        for assignment in assignments.values():
            if assignment.class_id == class_id and assignment.due_date == due_date:
                print(assignment)

