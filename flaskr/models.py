from flaskr import db, login_manager
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin


from datetime import datetime, timedelta
from uuid import uuid4

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(
        db.String(128),
        default = generate_password_hash('snsflaskapp')
        )
    picture_path = db.Column(db.Text)
    is_active = db.Column(db.Boolean, unique=False, default=False)
    created_at = db.Column(db.DataTime, default=datetime.now)
    update_at = db.Column(db.DataTime, default=datetime.now)
    
    @classmethod
    def select_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
class PasswordResetToken(db.Model):
    __tablename__ = "password_reset_tokens"
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(
        db.String(64),
        unique=True,
        index=True,
        server_default=str(uuid4)
    )
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', nullable=False))
    expire_at = db.Column(db.DataTime, default=datetime.now)
    created_at = db.Column(db.DataTime, default=datetime.now)
    update_at = db.Column(db.DataTime, default=datetime.now)
    
    