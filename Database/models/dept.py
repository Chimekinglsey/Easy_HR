#!/usr/bin/python3
from models.base import BaseModel, Base
from sqlalchemy import String, ForeignKey, Column
from sqlalchemy.orm import relationship


class Department(BaseModel, Base):
    """ the company branches """
    from models.levels import Level
    from models.employee import Employee
    __tablename__ = 'depts'
    branch_id = Column(String(128), ForeignKey('branches.id'), nullable=False)
    name = Column(String(128), nullable=False, unique=True)
    branch = relationship("Branch", back_populates="departments")
    lev = relationship(Level, back_populates='dep', cascade="all, delete, delete-orphan")
    employees = relationship(Employee, back_populates='depts', cascade="all, delete, delete-orphan") 


    def __init__(self, branch_id, name):
        super().__init__()
        self.branch_id = branch_id
        self.name = name