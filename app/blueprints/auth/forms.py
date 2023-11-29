from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import EqualTo, DataRequired

class LoginForm(FlaskForm):
    email = EmailField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit_btn = SubmitField('Login')

class SignupForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = EmailField('Email ', validators=[DataRequired()])
    password = PasswordField('Password ', validators=[DataRequired()])
    Comfirm_Password = PasswordField('Comfirm Password ', validators=[DataRequired(), EqualTo('password')])
    submit_btn = SubmitField('Sign Up')