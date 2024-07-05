from flask import Blueprint, render_template 

auth = Blueprint("auth", __name__)  

@auth.route('/signup')
def signup():
    return "This page will sign up users"


@auth.route('/login')
def login():
    return "This page logs in users"


@auth.route('/logout')
def logout():
    return "This page logs out users"