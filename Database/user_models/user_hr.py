from user_models.user_base import UserBaseModel, UserBase
from sqlalchemy import String, ForeignKey, Column
from sqlalchemy.orm import relationship
import os


class HrUser(UserBaseModel, UserBase):
    """ the company branches """
    __tablename__ = 'hr_users'
    company_id = Column(String(128), ForeignKey('companies.id'), nullable=False)
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    password = Column(String(70), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=False)
    company = relationship("Company", back_populates="hr_user") 

    def __init__(self, company_id, first_name, last_name, password, email, phone_number):
        super().__init__()
        self.company_id = company_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.phone_number = phone_number

    def create_company_database(self):
        """create unqiue database for company"""
        os.environ['UHR_MYSQL_USER'] = self.first_name
        os.environ['UHR_MYSQL_PWD'] = self.password
        os.environ['UHR_MYSQL_HOST'] = 'localhost'
        os.environ['UHR_MYSQL_DB'] = self.company.name
    
    def create_branch(self, name, location):
        from models.branch import Branch
        branch = Branch(name, location)
        branch.save()
        return branch.id
    
    def create_dept(self, branch_id, name):
        from models.dept import Department
        dept = Department(branch_id, name)
        dept.save()
        return dept.id
    
    def create_level(self, name, level_type):
        from models.levels import Level
        level = Level(name, level_type)
        level.save()
        return level.id
    
    def create_employees(self, branch_id, dept_id, level_id, first_name, last_name,
                 date_of_birth, email, salary, address, phone_number):
        from models.employee import Employee
        employee = Employee(branch_id, dept_id, level_id, first_name, last_name,
                 date_of_birth, email, salary, address, phone_number)
        employee.save()
        return employee.id
    
    def create_nok(self, employee_id, first_name, last_name, email, address, phone_number):
        from models.nok import Nok
        nok = Nok(employee_id, first_name, last_name, email, address, phone_number)
        nok.save()
        return nok.id