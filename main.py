from flask import Blueprint, render_template
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def landing_page():
    return render_template('landing_page.html')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@main.route('/dashboard/manage_emp')
def manage_emp():
    return render_template('manage_employee.html')