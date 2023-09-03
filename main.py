from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime
from .model_user import User, Employee
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def landing_page():
    return render_template('landing_page.html')

@main.route('/dashboard')
@login_required
def dashboard():
    # users=User.query.all()
    # count = 0
    # for user in users:
    #     count += 1
    count1 = 0 
    emps = count1
    numEmp = current_user.employees
    if numEmp:
        for employee in numEmp:
            count1 += 1
        if count1 < 2:
            employee = 'employee'
        else:
            employee = 'employees'
        emps = count1
    else:
        employee = "employees"
    return render_template('dashboard.html', user=current_user.first_name,
                           employee=employee, emp_count=emps)

@main.route('/manage_emp')
@login_required
def manage_emp():
    return render_template('manage_employee.html', employee=current_user.employees)

@main.route('/add_employee', methods=['GET', 'POST'])
@login_required
def add_emp():
    if request.method == 'POST':
        user_id = current_user.id

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
        DateOfEmployment = datetime.strptime(request.form.get("DateOfEmployment"), '%Y-%m-%d').date()
        dateOfBirth = datetime.strptime(request.form.get("dateOfBirth"), '%Y-%m-%d').date() 
        gender = request.form.get("gender")

        #to ensure emails are unqiue per employee
        emps = current_user.employees
        for emp in emps:
            if emp.email == email:
        # [employee_emails for employees.email in  current_user.employees]
        # [exists for email in employee_emails]
        # if exists:
                flash('Employee with this email already exists')
                return redirect(url_for('main.manage_emp'))

        new_employee = Employee(user_id=user_id, firstName=firstName, middleName=middleName,
                                lastName=lastName, email=email, phoneNumber=phoneNumber,
                                address=address, nationality=nationality, stateOfOrigin=stateOfOrigin,
                                employeeID=employeeID, level=level, salary=salary,
                                branch=branch, department=department, DateOfEmployment=DateOfEmployment,
                                dateOfBirth=dateOfBirth, gender=gender)
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('main.manage_emp'))
    return url_for('main.manage_emp')


@main.route('/get_employee_details', methods=['GET', 'POST'])
@login_required
def get_employee_details():
    if request.method == 'POST':
        # Retrieve the employee ID from the form
        employeeID = request.form.get("employeeID")

        # Query the database for the employee with the employeeID for the current user
        # employee_list = current_user.employees
        # for employee in employee_list:
        #     if employee.employeeID == employeeID:
        #         return render_template('manage_employee.html', employee=employee)


        employee = Employee.query.filter_by(employeeID=employeeID, user_id=current_user.id).first()

        # Check if the employee exists and belongs to the currently logged-in user
        if not employee:
            flash('Employee does not exist')
            return redirect(url_for('main.manage_emp'))
        
        # Return the employee details to the page
    
    return render_template('manage_employee.html', employee=employee)
