#!/usr/bin/python3
"""Base model module for the base model"""
import models.storage as storage
from datetime import datetime
import uuid
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy import MetaData

time = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base(metadata=MetaData())

class BaseModel:
    """This class defines common attributes/methods for other classes"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """This method initializes an instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, time)
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                setattr(self, "id", str(uuid.uuid4()))
            time = "%Y-%m-%dT%H:%M:%S.%f"
            if "created_at" not in kwargs:
                setattr(self, "created_at", datetime.now())
            if "updated_at" not in kwargs:
                setattr(self, "updated_at", datetime.now())

    def __str__(self):
        """This method returns a string representation of an instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """This method updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """This method returns a dictionary representation of an instance"""
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """This method deletes the current instance from the storage"""
        storage.delete(self)
        storage.save()

    def __repr__(self):
        """This method returns a string representation of an instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
