from flask import Flask, render_template, request, redirect, url_for, abort
from . import main
from ..models import User
from flask_login import login_required, current_user
from .. import db
import markdown2


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')



@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)