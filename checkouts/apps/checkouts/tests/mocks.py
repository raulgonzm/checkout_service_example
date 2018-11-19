# Python imports
# Flask imports
# Third-Party imports
import factory
# Project Imports
from apps import db
from apps.checkouts.models import Checkout


class CheckoutFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: n)
    checkout_number = factory.Faker("pystr", max_chars=10)

    class Meta:
        model = Checkout
        sqlalchemy_session = db.session
