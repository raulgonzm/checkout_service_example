# Python imports
# Flask imports
# Third-Party imports
import factory
# Project Imports
from apps.purchase_items.models import PurchaseItem

from apps import CheckoutApp

db = CheckoutApp.db


class PurchaseItemFactory(factory.alchemy.SQLAlchemyModelFactory):
    quantity = factory.Faker("pyint")

    class Meta:
        model = PurchaseItem
        exclude = ('product', 'checkout')
        sqlalchemy_session = db.session
