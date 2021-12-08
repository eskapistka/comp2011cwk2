from flask_login import login_user, login_required, logout_user
from flask import Blueprint, flash, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, models

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # login code for the authentication on the server side
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = models.User.query.filter_by(email=email).first()

    # check if the user exists
    # then we check the hashed password entered in the form against
    # the one that is hashed and stored in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    # if the above checks passed we can authenticate the user
    # we log in the user and save the state of "remember me" check
    login_user(user, remember=remember)
    return redirect(url_for('app.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    # here will be the code for data validation
    # and for adding the entry to the database

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # check if the email is not already in the database
    # if this check returns a user then it's already been taken
    user = models.User.query.filter_by(email=email).first()

    # if the email has not been used then we can create a new user
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    new_user = models.User(email=email,
                           name=name,
                           password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('app.index'))
