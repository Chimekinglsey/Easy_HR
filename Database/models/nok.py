#!/usr/bin/python3
from models.base import BaseModel, Base
from sqlalchemy import String, ForeignKey, Column
from sqlalchemy.orm import relationship


class NextOfKin(BaseModel, Base):
    """ the company branches """
    __tablename__ = 'nextKins'
    employee_id = Column(String(128), ForeignKey('employees.id'), nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    address = Column(String(128), nullable=False)
    phone_number = Column(String(20), nullable=False)
    employee_n = relationship("Employee", back_populates="nextKin") 
    


    def __init__(self, employee_id, first_name, last_name, email, address, phone_number):
        super().__init__()
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.phone_number = phone_number