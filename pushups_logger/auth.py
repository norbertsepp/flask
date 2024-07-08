from flask import Blueprint, render_template, url_for, request, redirect
from werkzeug.security import generate_password_hash
from .models import User
from . import db
import sqlite3

auth = Blueprint("auth", __name__)  

def db_conn():
    try:
        conn_ = sqlite3.connect(".\\pushups_logger\\db.sqlite")
        print("Database connected successfully")
    except ConnectionError: 
        print("SQLite table connection error!")
    return conn_


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=["POST"])
def signup_post():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    
    password_hashed = generate_password_hash(password)
    
    conn = db_conn()
    print(conn)
    cursor = conn.cursor()
    print(cursor)
    cursor.execute(f'SELECT name, email from USER where email="{email}";')
    
    l = cursor.fetchall()
    print(l)
    if len(l) > 0:
        print(f"User with email {email} already exists!")
        print(l)
        
    else:
        statement = "INSERT INTO USER (email, password, name) VALUES(" 
        statement += f'"{email}", "{password_hashed}", "{name}");'
        print("SQL:-> ", statement)
        cursor.execute(statement)
        conn.commit()
        print(f"User successfully added: {name}, {email}, {password_hashed}")
    conn.close()
        
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