from flask_wtf import FlaskForm  # Importing forms
from wtforms import StringField, PasswordField, SubmitField  # Import specific types of fields
from wtforms.validators import Length, EqualTo, Email, DataRequired # Import specific validation tools

class RegisterForm(FlaskForm):
    username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(label='Confirm password:', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Create Account')

