from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import filters

app = Flask(__name__)
app.config.from_object('flaskr.config')

db = SQLAlchemy(app)

filters.init_app(app)

import flaskr.views
