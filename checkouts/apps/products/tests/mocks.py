# Python imports
# Flask imports
# Third-Party imports
import factory
# Project Imports
from apps.products.models import Product
from apps import db


class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: n)
    code = factory.Faker("pystr", max_chars=10)
    name = factory.Faker("name")

    class Meta:
        model = Product
        sqlalchemy_session = db.session
