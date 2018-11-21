# Python imports
from logging.handlers import RotatingFileHandler
from logging import DEBUG
# Flask imports
from flask import Flask
# Third-Party imports
from flask_sqlalchemy import SQLAlchemy
# Project imports
from .settings import config_by_name


db = SQLAlchemy()


def create_app(env):
    app = Flask(__name__)
    config = config_by_name[env]
    app.config.from_object(config)
    db.init_app(app)
    if 'local' in env:
        handler = RotatingFileHandler('/tmp/app.log', maxBytes=10000, backupCount=3)
        handler.setLevel(DEBUG)
        app.logger.addHandler(handler)
    return app
