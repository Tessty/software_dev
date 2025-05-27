from flask import Blueprint, render_template, request, redirect, flash, url_for
from .models import User
from .extension import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            return redirect(url_for('views.home'))
        else:
            flash('Incorrect email or password')
    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('auth.signup'))

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered')
            return redirect(url_for('auth.signup'))
        
        new_user = User(
            name=name,
            email=email,
            password=generate_password_hash(password, method='sha256')
        )
        flash('Account created! continue to order.')

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    
    return render_template("signup.html")

