from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Required, Email, EqualTo
from ..models import User 

class RegistrationForm(FlaskForm):
  email = StringField('Your email address', validators=[Required(), Email()])
  first_name = StringField('Your first name', validators=[Required()])
  last_name = StringField('Your last name', validators=[Required()])
  username = StringField('Enter a username', validators=[Required()])
  password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message='Passwords must match')])
  password_confirm = PasswordField('Confirm password', validators=[Required()])
  submit = SubmitField('Sign Up')

  def validate_email(self, data_field):
    if User.query.filter_by(email = data_field.data).first():
      raise ValidationError('An account with that email already exists')
    
  def validate_username(self, data_field):
    if User.query.filter_by(username = data_field.data).first():
      raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
  username = StringField('Your Username', validators=[Required()])
  password = PasswordField('Password', validators=[Required()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')