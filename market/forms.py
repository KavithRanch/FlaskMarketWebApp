from flask_wtf import FlaskForm  # Importing forms
from wtforms import StringField, PasswordField, SubmitField  # Import specific types of fields

class RegisterForm(FlaskForm):
    username = StringField(label='Username:')
    email_address = StringField(label='Email Address:')
    password = PasswordField(label='Password:')
    confirm_password = PasswordField(label='Confirm password:')
    submit = SubmitField(label='Create Account')
