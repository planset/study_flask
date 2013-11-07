from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Length

class LoginForm(Form):
    username = TextField('username', validators=[
        Required(message='Required'),
        Length(min=1, max=100, message='1-100')
        ])
    password = PasswordField('password', validators=[
        Required(message='Required'),
        Length(min=1, max=100, message='1-100')
        ])

