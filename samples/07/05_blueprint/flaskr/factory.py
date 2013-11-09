from flask import Flask
from flaskr.core import db
from flaskr import filters, logs, frontend

def create_app(package_name):
    app = Flask(package_name)
    app.config.from_object('flaskr.config')

    app.config['DEBUG'] = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    db.init_app(app)

    filters.init_app(app)
    logs.init_app(app)
    frontend.init_app(app)

    return app

