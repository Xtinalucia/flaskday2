from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class UserInfoForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    phonenumber = StringField('Phonenumber', validators=[DataRequired(), phonenumber()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()
    
