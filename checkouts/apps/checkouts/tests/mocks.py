# Python imports
# Flask imports
# Third-Party imports
import factory
# Project Imports
from apps.checkouts.models import Checkout
from apps import CheckoutApp

db = CheckoutApp.db


class CheckoutFactory(factory.alchemy.SQLAlchemyModelFactory):
    checkout_number = factory.Faker("pystr", max_chars=10)

    class Meta:
        model = Checkout
        sqlalchemy_session = db.session
