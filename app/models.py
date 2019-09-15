from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager
# from flask_sqlalchemy import SQLAlchemy


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Pitch:
  def __init__(self, id, title, author, posted_at, body, upvotes, downvotes):
    self.id = id
    self.title = title
    self.overview = overview
    self.author = author
    self.posted_at = posted_at
    self.body = body
    self.upvotes = upvotes
    self.downvotes = downvotes


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    pass_secure = db.Column(db.String(255))
    
    
    @property
    def password(self):
        raise AttributeError('You do not have permission to view password attribute')
    
    
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)


    def save_user(self):
        db.session.add(self)
        db.session.commit()


    def __repr__(self):
        return f'User {self.username}'
    
    
    
class Role(db.Model):
  __tablename__ = 'roles'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255))
  users = db.relationship('User', backref='role', lazy='dynamic')


  def __repr__(self):
    return f'User {self.name}'



class Comments(db.Model):
  __tablename__ = 'comments'

  id = db.Column(db.Integer, primary_key = True)
  pitch_id = db.Column(db.Integer)
  title = db.Column(db.String)
  image_path = db.Column(db.String)
  comment = db.Column(db.String)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def save_comment(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comments(cls, id):
    comments = Comments.query.filter_by(pitch_id=id).all()
    return comments