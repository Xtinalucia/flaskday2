from app import db
import os
from werkzeug.security import generate_password_hash, check_password_hash



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    phonenumber = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    

    def __init__(self, username, phonenumber, password):
        self.username=username
        self.phonenumber = phonenumber
        self.password = generate_password_hash(password)
        
