from flask.ext.login import UserMixin
from flaskr.core import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column('password', db.String(100), nullable=False)

    def check_password(self, password):
        return self.password == password

    @classmethod
    def authenticate(cls, query, username, password):
        user = query(cls).filter(cls.username==username).first()
        if user is None:
            return None, False
        return user, user.check_password(password)

    def __repr__(self):
        return u'<User id={self.id} username={self.username!r}>'.format(
                self=self)


class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def __repr__(self):
        return '<Entry id={id} title={title!r}>'.format(
                id=self.id, title=self.title)

