# Python imports
import os
from logging.handlers import RotatingFileHandler
from logging import DEBUG
# Flask imports
from flask import Flask
# Third-Party imports
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Project imports


env = os.environ.get('ENV', 'local')
config = f"apps.settings.{env.capitalize()}Config"
app = Flask(__name__)
app.config.from_object(config)

if 'local' in env:
    handler = RotatingFileHandler('/tmp/app.log', maxBytes=10000, backupCount=3)
    handler.setLevel(DEBUG)
    app.logger.addHandler(handler)


database_name = os.environ.get('DATABASE_NAME', 'checkouts.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{database_name}"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
