from __future__ import print_function
from flask_script import Manager, prompt, prompt_pass
from flaskr import app
from flaskr.core import db
from flaskr.models import User

manager = Manager(app)


@manager.command
def create_user(email, password):
    email = email or prompt('Email')
    password = password or prompt_pass('Password')
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    print('User created successfully')

@manager.command
def delete_user(email):
    email = email or prompt('Email')
    user = User.query.filter(User.email==email).first()
    db.session.delete(user)
    db.session.commit()
    print('User deleted successfully')

@manager.command
def list_users():
    for user in User.query.all():
        print(user)


@manager.command
def init_db():
    db.create_all()

if __name__ == '__main__':
    manager.run()
