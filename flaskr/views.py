from flask import(
    Blueprint, abort, request, render_template,
    redirect, url_for, flash
)

from flask_login import login_user, login_required, logout_user
from flaskr.models import(
    User, PasswordResetToken
)

from flaskr import db

from os import path

bp = Blueprint('app', __name__, url_prefix='')

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/logout')
def logout_user():
    logout_user()
    return redirect(url_for('app.home'))
