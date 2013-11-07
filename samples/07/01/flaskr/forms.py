from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, PasswordField
from wtforms.validators import Required, Length


class EntryForm(Form):
    title = TextField('title', validators=[
        Required(message='Required'),
        Length(min=1, max=100, message='1-100')
        ])
    text = TextAreaField('text', validators=[
        Required('Required')
        ])

class LoginForm(Form):
    username = TextField('username', validators=[
        Required(message='Required'),
        Length(min=1, max=100, message='1-100')
        ])
    password = PasswordField('password', validators=[
        Required(message='Required'),
        Length(min=1, max=100, message='1-100')
        ])

