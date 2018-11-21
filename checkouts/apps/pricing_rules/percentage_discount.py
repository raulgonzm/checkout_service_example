# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps.pricing_rules.base_rules import PricingRule


class PercentageDiscount(PricingRule):

    def is_applicable_by_target_type(self, target):
        pass

    def is_applicable_by_quantity(self, quantity):
        pass

    def is_applicable_to(self, checkout):
        pass

    def apply_to_price_checkout(self, checkout):
        pass