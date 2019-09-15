from flask import Flask, render_template, request, redirect, url_for, abort, flash
from . import main
from .forms import PitchForm, UpdateProfile
from ..models import User, Pitch
from flask_login import login_required, current_user
from .. import db
import markdown2
import datetime


@main.route('/')
@login_required
def index():
    title = 'Welcome to Pitch'
    
    return render_template('index.html', title = title)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches = Pitch
    
    if user is None:
        abort(404)
        
    return render_template('profile/profile.html', user = user)


@main.route('/writing-pitch', methods = ['GET', 'POST'])
@login_required
def write_pitch():
    form = PitchForm()
    
    title = 'New Pitch'
    
    render_template('new_pitch.html', pitch = form, title = title)