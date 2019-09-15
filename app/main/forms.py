from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import Required, Email
from ..models import User


class CommentForm(FlaskForm):
    
    title = StringField('Comment title',validators=[Required()])
    
    comment = TextAreaField('Pitch post comment')
    
    submit = SubmitField('Submit')
    
    
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators= [Required()])
    submit = SubmitField('Submit')