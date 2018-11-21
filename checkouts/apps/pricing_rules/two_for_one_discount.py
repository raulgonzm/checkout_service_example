# Python imports
import math
# Flask imports
# Third-Party imports
# Project Imports
from apps.pricing_rules.base_rules import PricingRule


class TwoForOneDiscount(PricingRule):

    def apply_to_price_purchase(self, purchase):
        if self.is_applicable_to_purchase(purchase=purchase):
            return math.ceil(purchase.quantity / self.prerequisite_quantity) * purchase.product.price
        return purchase.price
