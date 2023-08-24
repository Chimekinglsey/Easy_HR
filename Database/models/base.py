#!/usr/bin/python3
""" This is the base class for all tables """


from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid
import models


Base = declarative_base()


class BaseModel:
    """This is the base class where all classes inherit from"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())


    def __init__(self, *args):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at


    def __str__(self):
        """string representation of the class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """saves an instance to the database"""
        self.updated_at = datetime.utcnow()
        models.storage.reload()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """deletes the instance"""
        models.storage.delete()