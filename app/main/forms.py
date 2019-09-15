from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import Required, Email
from ..models import User


class PitchForm(FlaskForm):
    
    title = StringField('Pitch title',validators=[Required()])
    
    info = TextAreaField('Pitch post')
    
    submit = SubmitField('Submit')
    
    
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators= [Required()])
    submit = SubmitField('Submit')