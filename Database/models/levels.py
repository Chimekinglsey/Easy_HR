#!/usr/bin/python3
from models.base import BaseModel, Base
from sqlalchemy import String, ForeignKey, Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum


class Level(BaseModel, Base):
    """ the company branches """
    from models.employee import Employee
    __tablename__ = 'levels'
    dept_id = Column(String(128), ForeignKey('depts.id'), nullable=False)
    name = Column(String(128), nullable=False)
    level_type = Column(Enum('Graduate Assistant', 'Intern', 'Executive',
                             'Junior', 'Senior', name='level_enum'), unique=True, nullable=False )
    dep = relationship("Department", back_populates="lev")
    employee_l = relationship(Employee, back_populates='levels', cascade="all, delete, delete-orphan") 


    def __init__(self, dept_id, name, level_type):
        super().__init__()
        self.dept_id = dept_id
        self.name = name
        self.level_type = level_type