#!/usr/bin/python3
from models.base import BaseModel, Base
from sqlalchemy import String, Integer, ForeignKey, Column, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CheckConstraint
from datetime import datetime, timedelta


min_date = datetime.now() - timedelta(days=365*18)
class Employee(BaseModel, Base):
    """ the company branches """
    from models.nok import NextOfKin
    __tablename__ = 'employees'
    branch_id = Column(String(128), ForeignKey('branches.id'), nullable=False)
    dept_id = Column(String(128), ForeignKey('depts.id'), nullable=False)
    level_id = Column(String(128), ForeignKey('levels.id'), nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    date_of_birth = Column(DateTime)
    email = Column(String(128), nullable=False, unique=True)
    salary = Column(Integer,nullable=False)
    address = Column(String(128), nullable=False)
    phone_number = Column(String(20), nullable=False)
    nextKin = relationship(NextOfKin, back_populates='employee_n', cascade="all, delete, delete-orphan")
    branch = relationship("Branch", back_populates='employee')  
    depts = relationship("Department", back_populates='employees')
    levels = relationship("Level", back_populates='employee_l')

    def __init__(self, branch_id, dept_id, level_id, first_name, last_name,
                 date_of_birth, email, salary, address, phone_number):
        super().__init__()
        self.branch_id = branch_id
        self.dept_id = dept_id
        self.level_id = level_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.salary = salary
        self.address = address
        self.phone_number = phone_number