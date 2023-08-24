#!/usr/bin/python3
""" This is the base class for all tables """


from sqlalchemy import Column, String, DateTime, event
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid
import user_models


UserBase = declarative_base()


class UserBaseModel:
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
        user_models.storage.reload()
        user_models.storage.new(self)
        user_models.storage.save()

    def delete(self):
        """deletes the instance"""
        user_models.storage.delete()

    @classmethod
    def create_after_event_listeners(cls):
        @event.listens_for(cls, 'after_insert')
        def after_employee_insert(cls,mapper, connection, target):
            # Access the generated id of the inserted Employee instance
            id = target.id
            # Print some information about the inserted Employee
            print(f"Employee inserted with id: {id}")
            print(f"Employee name: {target.first_name} {target.last_name}")
            return id