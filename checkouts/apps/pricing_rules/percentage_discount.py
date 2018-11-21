# Python imports
from decimal import Decimal
# Flask imports
# Third-Party imports
# Project Imports
from apps.pricing_rules.base_rules import PricingRule


class PercentageDiscount(PricingRule):

    def apply_to_price_purchase(self, purchase):
        if self.is_applicable_to_purchase(purchase=purchase):
            purchase_price = purchase.price
            discounted = purchase_price - (purchase_price * Decimal(self.value / 100))
            return discounted if discounted >= 0 else 0
        return purchase.price
