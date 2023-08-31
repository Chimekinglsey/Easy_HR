from datetime import date
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    first_name = db.Column(db.String(300))
    last_name = db.Column(db.String(300))
    DOB = db.Column(db.Date, default=date.today)
    company_name = db.Column(db.String(300))
    official_email = db.Column(db.String(100), unique=True)
    company_size = db.Column(db.Enum('1 - 50', '51 - 100', '101 - 200', '201 - 500', 'Above 500'), nullable=False)
    password = db.Column(db.String(100))