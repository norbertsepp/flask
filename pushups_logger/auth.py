from flask import Blueprint, render_template, url_for, request, redirect
from werkzeug.security import generate_password_hash
from .models import User
from . import db

auth = Blueprint("auth", __name__)  


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=["POST"])
def signup_post():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    
    #print(email, name, password)
    user = User.query.filter_by(email=email).first()
    
    if user:
        print("User already exists!")
    else:
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit() 
        
    return redirect(url_for('auth.login'))
    
    

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():

    email = request.form.get("email")
    password = request.form.get("password")
    
    print(email, password)
    
    return redirect(url_for('main.profile'))

@auth.route('/logout')
def logout():
    return "This page logs out users"