from flask import Flask, render_template, request, redirect, url_for, abort, flash
from . import main
from .forms import PitchForm, CommentForm
from ..models import User, Pitch, Comments
from ..pitches import get_pitch
from flask_login import login_required, current_user
from .. import db
import markdown2
import datetime


@main.route('/')
@login_required
def index():
    pitches=Pitch.query.all()
    
    title = 'Welcome to Pitch'
    
    return render_template('index.html', title = title, pitches=pitches)



@main.route('/profile/<uname>/<id>')
def profile(id, uname):
  user = User.query.filter_by(username = uname)
  pitches = Pitch.query.filter_by(id=id)
  message="You don't have any pitches."
  if pitches is not 0:
    message="You have pitches"
    
  if user is None:
    abort(404)
    
  return render_template('profile/profile.html', user=user, pitches=pitches, message=message)


@main.route('/writing-pitch', methods=['GET', 'POST'])
@login_required
def write_pitch():
  form = PitchForm()
  if form.validate_on_submit():
    pitch = Pitch(title=form.title.data, body=form.body.data, category=form.category.data)

    db.session.add(pitch)
    db.session.commit()
    return redirect(url_for('main.index'))

  title = 'New Pitch'
  return render_template('new_pitch.html', pitch=form, title=title)


@main.route('/comment', methods=['GET', 'POST'])
@login_required
def write_comment():
  form = CommentForm()
  if form.validate_on_submit():
    comment = Comments(comment=form.comment.data)
    comment.save_comment()

    return redirect(url_for('main.index'))

  return render_template('comment.html', comment=form)


@main.route('/interview')
def get_interview():
  pitches = Pitch.query.filter_by(category='int')
  title='Interview Pitches'
  message='There are no pitches in the interview section. Go back to home to continue viewing.'
  if pitches is not 0:
    message='Interview pitches'
  return render_template('index.html', pitches=pitches, title=title, message=message)

@main.route('/pickup')
def get_pickup():
  pitches = Pitch.query.filter_by(category='pick')
  title='Pickup Pitches'
  message='There are no pitches in the pickup section. Go back to home to continue viewing.'
  if pitches is not 0:
    message='Pickup Pitches'
  return render_template('index.html', pitches=pitches, title=title, message=message)

@main.route('/product')
def get_product():
  pitches = Pitch.query.filter_by(category='prod')
  title='Product Pitches'
  message='There are no pitches in the product section. Go back home to continue viewing.'
  if pitches is not 0:
    message='Product Pitches'
  return render_template('index.html', pitches=pitches, title=title, message=message)

@main.route('/promotion')
def get_promotion():
  pitches = Pitch.query.filter_by(category='prom')
  title='Promotion Pitches'
  message='There are no pitches in the promotion section. Go back to home to continue viewing'
  if pitches is not 0:
    message='Promotion Pitches'
  return render_template('index.html', pitches=pitches, title=title, message=message)

@main.route('/view-comments/<id>')
def view_comments(id):
  pitch = Pitch.query.filter_by(id=id)
  comments = Comments.query.filter_by(id=id)
  message='This pitch has no comments'
  if comments is not 0:
    message=f"You're now viewing the comments. Click home to continue browsing pitches"
  return render_template('comments.html', message=message, comments=comments, pitch=pitch)

@main.route('/delete/<id>')
def pitch_delete(id):
  pitch = Pitch.query.filter_by(id=id)
  return pitch.delete_pitch()