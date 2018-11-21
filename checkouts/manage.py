# Python imports
import unittest
# Flask imports
# Third-Party imports
from flask_restful import Api
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
# Project imports
from apps import create_app, db
from apps.settings import get_env_variable
from apps.urls import Router
from apps.checkouts.models import Checkout
from apps.products.models import Product
from apps.purchase_items.models import PurchaseItem

app = create_app(env=get_env_variable("ENV"))
app.app_context().push()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
Router(Api(app))


@manager.command
def run():
    db.create_all()
    app.run(
        host=app.config.get("SERVER_BIND_ADDRESS"),
        port=app.config.get("SERVER_PORT"),
        debug=app.config.get("DEBUG")
    )


@manager.command
def test():
    tests = unittest.TestLoader().discover("apps/", pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
