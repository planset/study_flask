from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import filters
import logs

app = Flask(__name__)
app.config.from_object('flaskr.config')

db = SQLAlchemy(app)

filters.init_app(app)
logs.init_app(app)

import flaskr.views
