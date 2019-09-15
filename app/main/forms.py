from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError, IntegerField, SelectField
from wtforms.validators import Required, Email
from ..models import User


class PitchForm(FlaskForm):
    
    title = StringField('Pitch title',validators=[Required()])
    
    body = TextAreaField('Pitch post')
    
    author = TextAreaField('Your name the way you would like it displayed')
  
    category = SelectField('Category', choices=[('int', 'Interview'), ('pick', 'Pickup'), ('prod', 'Product'), ('prom', 'Promotion')])
    
    submit = SubmitField('Submit')
    
    
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators= [Required()])
    submit = SubmitField('Submit')