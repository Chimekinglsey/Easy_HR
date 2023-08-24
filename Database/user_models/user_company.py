from user_models.user_base import UserBaseModel, UserBase
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship


class Company(UserBaseModel, UserBase):
    """ the company branches """
    __tablename__ = 'companies'
    name = Column(String(128), nullable=False, unique=True)
    headquaters = Column(String(128),nullable=False)
    staff_strenght = Column(Integer, nullable=False)
    hr_user = relationship("HrUser", uselist=False, back_populates="company")  
 
    def __init__(self, name, headquaters, staff_strenght):
        super().__init__()
        self.name = name
        self.headquaters =  headquaters
        self.staff_strenght = staff_strenght