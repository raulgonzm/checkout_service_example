# Python imports
from decimal import Decimal
# Flask imports
# Third-Party imports
from sqlalchemy.sql import func
# Project Imports
from apps import db
from apps.pricing_rules.services import get_current_discounts
from apps.purchase_items.models import PurchaseItem


class Checkout(db.Model):
    __tablename__ = 'checkouts'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    checkout_number = db.Column(db.String, nullable=False, unique=True)
    purchases = db.relationship(PurchaseItem, backref='checkout', lazy=True)

    def __repr__(self):
        return f"<Checkout-{self.id}>"

    def _calc_price_with_discounts(self, item):
        return [discount.apply_to_price_purchase(purchase=item) for discount in get_current_discounts()]

    def calc_price(self):
        total_price = Decimal(0.0)
        for item in self.purchases:
            discounted = [item.price] + self._calc_price_with_discounts(item=item)
            total_price += min(discounted)
        return total_price

    @property
    def total(self):
        return self.calc_price()

    def scan(self, purchase_item):
        self.purchases.append(purchase_item)
