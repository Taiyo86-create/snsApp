import os
from flask import flask
from flask_sqlalchemy import SQLalchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'app.view'
login_manager.login_massage = 'ログインが必要です'

basedir = os.path.abspath(os.path.dirname(__name__))
db = SQLalchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'SNS'