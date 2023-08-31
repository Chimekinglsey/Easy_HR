from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .model_user import User
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