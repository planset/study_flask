import os
from functools import wraps

from flask import current_app, request, redirect, url_for, \
        session, g, send_from_directory
from flaskr.models import User
from flaskr import factory

def login_required(f):
    @wraps(f)
    def decorated_view(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.path))
        return f(*args, **kwargs)
    return decorated_view

def load_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(session['user_id'])

def send_favicon():
    return send_from_directory(os.path.join(current_app.root_path, 'static'),
                'favicon.ico', mimetype='image/vnd.microsoft.icon')

def index():
    return redirect(url_for('entries.show_entries'))


def init_app(app):
    app.before_request(load_user)
    app.add_url_rule('/favicon.ico', 'send_favicon', send_favicon)
    app.add_url_rule('/', 'index', index)

    from flaskr.frontend import entries, users
    app.register_blueprint(users.bp)
    app.register_blueprint(entries.bp)


def create_app(settings_override=None):
    app = factory.create_app(__name__, settings_override)
    init_app(app)
    return app



