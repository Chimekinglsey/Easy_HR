from flask import Blueprint, render_template, redirect, url_for
from flask import request
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from .model_user import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('landing_page.html')

@auth.route('/signup')
def signup():
    return render_template('sign_up_page.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    ###
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    DOB = request.form.get('DOB')
    company_name = request.form.get('company_name')
    official_email = request.form.get('official_email')
    company_size = request.form.get('company_size')
    password = request.form.get('password')

    # DOB = datetime.strptime(DOB, '%Y-%m-%d').date()

    user = User.query.filter_by(official_email=official_email).first() # if this returns a user, then the email already exists in database
    
    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.signup'))
        # return 'Email address already exists'
    
    # create a new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(first_name=first_name, last_name=last_name, DOB=DOB,
                    company_name=company_name, official_email=official_email,
                    company_size=company_size, password=generate_password_hash(password, method='sha256'))
    
    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout'