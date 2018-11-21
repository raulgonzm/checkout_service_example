# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps.pricing_rules.base_rules import PricingRule


class FixedAmountDiscount(PricingRule):

    def apply_to_price_purchase(self, purchase):
        if self.is_applicable_to_purchase(purchase=purchase):
            discounted = purchase.price - self.value
            return discounted if discounted >= 0 else 0
        return purchase.price
