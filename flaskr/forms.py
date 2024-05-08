from wtforms.form import Form
from wtforms.fields import(
    StringField, FileField, PasswordField, SubmitField, HiddenField
)
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

from flaskr.models import User


# ログイン用フォーム
class LoginForm(Form):
    email = StringField('メールアドレス: ', validators=[DataRequired(), Email()])
    password = PasswordField('パスワード:', validators=[DataRequired(), EqualTo('confirm_password', message='パスワードが一致しません')])
    confirm_password = PasswordField('パスワード再入力: ', validators=[DataRequired()])
    submit = SubmitField('ログイン')
#登録用フォーム
class RegisterForm(Form):
    email = StringField('メールアドレス: ', validators=[DataRequired(), Email('メールアドレスに誤りがあります。')])
    username = StringField('名前: ', validators=[DataRequired()])
    submit = SubmitField('登録')
    
    def validate_email(self, field):