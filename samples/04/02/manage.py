from __future__ import print_function
from flask.ext.script import Manager, prompt, prompt_pass
from flaskr import app
from flaskr.models import User, db

manager = Manager(app)

@manager.command
def create_user(username, password):
    username = username or prompt('Username')
    password = password or prompt_pass('Password')
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    print('User created successfully')

@manager.command
def delete_user(username):
    username = username or prompt('Username')
    user = User.query.filter(User.username==username).first()
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

