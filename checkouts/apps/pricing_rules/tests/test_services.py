# Python imports
import unittest
# Flask imports
# Third-Party imports
# Project Imports
from apps.pricing_rules import services
from apps.pricing_rules.percentage_discount import PercentageDiscount
from apps.pricing_rules.settings import PRICING_RULE_BULK_PURCHASE_ALL, PRICING_RULE_TWO_FOR_ONE_ALL
from apps.pricing_rules.two_for_one_discount import TwoForOneDiscount


class PricingRuleServicesTestCase(unittest.TestCase):

    def test_instance_discount_from_module(self):
        self.assertIsInstance(
            services.instance_discount_from_module(
                module="apps.pricing_rules.percentage_discount",
                class_name="PercentageDiscount",
                configuration=PRICING_RULE_BULK_PURCHASE_ALL,
            ),
            PercentageDiscount
        )
        self.assertIsInstance(
            services.instance_discount_from_module(
                module="apps.pricing_rules.two_for_one_discount",
                class_name="TwoForOneDiscount",
                configuration=PRICING_RULE_TWO_FOR_ONE_ALL,
            ),
            TwoForOneDiscount
        )

    def test_get_current_discounts(self):
        current_discount = services.get_current_discounts()
        self.assertEqual(len(current_discount), 2)
        self.assertIsInstance(current_discount[0], TwoForOneDiscount)
        self.assertIsInstance(current_discount[1], PercentageDiscount)
