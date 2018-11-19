# Python imports
# Flask imports
# Third-Party imports
import factory
# Project Imports
from apps import db
from apps.purchase_items.models import PurchaseItem


class PurchaseItemFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: n)
    quantity = factory.Faker("pyint")

    class Meta:
        model = PurchaseItem
        exclude = ('product', 'checkout')
        sqlalchemy_session = db.session
