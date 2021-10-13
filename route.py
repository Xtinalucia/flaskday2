
from app import app
from flask import render_template
from app.forms import UserInfoForm, PostForm
from app.models import User, Post
from app import db


@app.route('/PB')
def phonenumber():
    title = 'PhoneBook'
    return render_template('PB.html', title=title)


@app.route('/register1')
def register_phone_number():
    title = 'Register'
    return render_template('register1.html', title=title)



