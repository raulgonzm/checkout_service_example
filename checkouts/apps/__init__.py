# Python imports
from logging.handlers import RotatingFileHandler
from logging import DEBUG
# Flask imports
from flask import Flask
# Third-Party imports
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Project imports


class CheckoutApp:

    app = Flask(__name__)
    db = SQLAlchemy(app)
    env = "test"

    def __new__(cls, env):
        cls.env = env
        if not cls.app:
            cls.app = cls.start_app()
            cls.start_db()
        return cls.app, cls.db

    @classmethod
    def start_app(cls):
        config = f"apps.settings.{cls.env.capitalize()}Config"
        app = Flask(__name__)
        app.config.from_object(config)
        if 'local' in cls.env:
            handler = RotatingFileHandler('/tmp/app.log', maxBytes=10000, backupCount=3)
            handler.setLevel(DEBUG)
            app.logger.addHandler(handler)
        return app

    @classmethod
    def start_db(cls):
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{cls.app.config.get('DATABASE_NAME')}"
        cls.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        cls.db = SQLAlchemy(cls.app)
        Migrate(cls.app, cls.db)
        if 'test' in cls.env:
            cls.app.config['TESTING'] = True
