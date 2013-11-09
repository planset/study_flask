from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import Required, Length

class LoginForm(Form):
    email = TextField('email', validators=[
        Required(message='Required'),
        Length(min=1, max=100, message='1-100')
        ])
    password = PasswordField('password', validators=[
        Required(message='Required'),
        Length(min=1, max=100, message='1-100')
        ])
    submit = SubmitField('login')


