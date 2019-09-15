from flask import Flask, render_template, request, redirect, url_for, abort
from . import main
from .forms import PitchForm, UpdateProfile
from ..models import User
from flask_login import login_required, current_user
from .. import db
import markdown2


@main.route('/')
@login_required
def index():
    pitches = pitch.save_pitch(pitch)
    
    return render_template('index.html', pitches=pitches)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches = Pitch
    
    if user is None:
        abort(404)
        
    return render_template('profile/profile.html', user = user)