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
    db_price = factory.Faker("pyfloat", left_digits=3, right_digits=2, positive=True)

    class Meta:
        model = Product
        sqlalchemy_session = db.session
