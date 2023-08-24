#!/usr/bin/python3
from models.base import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship



class Branch(BaseModel, Base):
    """ the company branches """
    from models.dept import Department
    from models.employee import Employee
    __tablename__ = 'branches'
    name = Column(String(128), nullable=False, unique=True)
    location = Column(String(128),nullable=False)
    departments = relationship(Department, back_populates="branch", cascade="all, delete, delete-orphan", lazy="select")
    employee = relationship(Employee, back_populates="branch", cascade="all, delete, delete-orphan", lazy="select")  


    def __init__(self, name, location ):
        super().__init__()
        self.name = name
        self.location = location