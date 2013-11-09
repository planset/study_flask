from __future__ import print_function
from flask.ext.script import Manager
from flaskr import app, db

manager = Manager(app)

@manager.command
def init_db():
    db.create_all()

if __name__ == '__main__':
    manager.run()
