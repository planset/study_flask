from flask import Flask
from .core import db, login_manager
from .models import User
from .log import setup_log

def create_app(package_name, override_config=None):

    app = Flask(package_name)
    app.config.from_object('flaskr.config')
    app.config.from_object(override_config)

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)

    setup_log(app)

    from flaskr.views import bp as views
    app.register_blueprint(views)

    return app


