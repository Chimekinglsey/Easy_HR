# model for user and employee tables
from flask_login import UserMixin
from datetime import date, datetime
from create_app import db


class User(UserMixin, db.Model):
    """Attributes of each User object"""
    id = db.Column(db.Integer, primary_key=True) # primary key unique for each  user
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    DOB = db.Column(db.Date, default=date.today)
    company_name = db.Column(db.String(300))
    official_email = db.Column(db.String(100), unique=True)
    company_size = db.Column(db.Enum('1 - 50', '51 - 100', '101 - 200', '201 - 500', 'Above 500'), nullable=False)
    password = db.Column(db.String(100))
    employees = db.relationship('Employee', backref='user', lazy=True, cascade="all, delete-orphan") # allows many employees to associate to a user
    employee_archives = db.relationship('Employee_archive', backref='user', lazy=True, cascade="all, delete-orphan") # allows many employees to associate to a user


class Employee(db.Model):
    """Attributes of each employee managed by a user"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # associates an employee to a particular user
    firstName = db.Column(db.String(30), nullable=False)
    middleName = db.Column(db.String(30), nullable=False)
    lastName = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phoneNumber = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    nationality = db.Column(db.String(30), nullable=False)
    stateOfOrigin = db.Column(db.String(30), nullable=False)
    employeeID = db.Column(db.String(30), nullable=False)
    level = db.Column(db.String(30), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    branch = db.Column(db.String(30), nullable=False)
    department = db.Column(db.String(30), nullable=False)
    DateOfEmployment = db.Column(db.Date, nullable=False, default=datetime)
    dateOfBirth = db.Column(db.Date, nullable=False, default=datetime)
    gender = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

class Employee_archive(db.Model):
    """
    Archive data base for employees
    Attributes of each employee managed by a user
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # associates an employee to a particular user
    firstName = db.Column(db.String(30), nullable=False)
    middleName = db.Column(db.String(30), nullable=False)
    lastName = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phoneNumber = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    nationality = db.Column(db.String(30), nullable=False)
    stateOfOrigin = db.Column(db.String(30), nullable=False)
    employeeID = db.Column(db.String(30), nullable=False)
    level = db.Column(db.String(30), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    branch = db.Column(db.String(30), nullable=False)
    department = db.Column(db.String(30), nullable=False)
    DateOfEmployment = db.Column(db.Date, nullable=False, default=datetime)
    dateOfBirth = db.Column(db.Date, nullable=False, default=datetime)
    gender = db.Column(db.String(30), nullable=False)
    pension_status = db.Column(db.String(30), nullable=True)
    reason_for_archive = db.Column(db.String(100), nullable=False)
    archived_at = db.Column(db.DateTime, nullable=False, default=datetime.now)