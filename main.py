from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .model_user import User, Employee
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def landing_page():
    return render_template('landing_page.html')

@main.route('/dashboard')
@login_required
def dashboard():
    users=User.query.all()
    count = 0
    for user in users:
        count += 1
    return render_template('dashboard.html', user=current_user.first_name, emp_count=count)

@main.route('/dashboard/manage_emp')
@login_required
def manage_emp():
    return render_template('manage_employee.html')

@main.route('user/add_employee', methods=['GET', 'POST'])
@login_required
def add_emp():
    if request.method is 'POST':
        firstName = request.form.get("firstName") 
        middleName = request.form.get("middleName") 
        lastName = request.form.get("lastName")
        email = request.form.get("email")
        phoneNumber = request.form.get("phoneNumber") 
        address = request.form.get("address") 
        nationality = request.form.get("nationality") 
        stateOfOrigin = request.form.get("stateOfOrigin") 
        employeeID = request.form.get("employeeID") 
        level = request.form.get("level") 
        salary = request.form.get("salary") 
        branch = request.form.get("branch") 
        department = request.form.get("department") 
        DateOfEmployment = request.form.get("DateOfEmployment") 
        dateOfBirth = request.form.get("dateOfBirth") 
        gender = request.form.get("gender")

        new_employee = Employee(firstName=firstName, middleName=middleName,
                                lastName=lastName, email=email, phoneNumber=phoneNumber,
                                address=address, nationality=nationality, stateOfOrigin=stateOfOrigin,
                                employeeID=employeeID, level=level, salary=salary,
                                branch=branch, department=department, DateOfEmployment=DateOfEmployment,
                                dateOfBirth=dateOfBirth, gender=gender)
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('main.manage_emp'))
    return url_for('main.manage_emp')