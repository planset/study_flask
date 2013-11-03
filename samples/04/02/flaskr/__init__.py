from flask import Flask

from .core import db, login_manager
from .models import User

app = Flask(__name__)
app.config.from_object('flaskr.config')

db.init_app(app)

login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

import flaskr.views
