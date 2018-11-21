# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps.pricing_rules.base_rules import PricingRule


class PercentageDiscount(PricingRule):

    def apply_to_price_purchase(self, purchase):
        pass