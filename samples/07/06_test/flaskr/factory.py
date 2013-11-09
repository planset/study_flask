from flask import Flask
from flaskr.core import db
from flaskr import filters, logs

def create_app(package_name, settings_override=None):
    app = Flask(package_name)
    app.config.from_object('flaskr.config')

    app.config.from_object(settings_override)

    app.config['DEBUG'] = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    db.init_app(app)

    filters.init_app(app)
    logs.init_app(app)

    return app

