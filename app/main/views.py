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
    return render_template('index.html')