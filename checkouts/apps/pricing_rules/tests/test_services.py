# Python imports
import unittest
# Flask imports
# Third-Party imports
# Project Imports
from apps.pricing_rules import services
from apps.pricing_rules.percentage_discount import PercentageDiscount
from apps.pricing_rules.two_for_one_discount import TwoForOneDiscount


class PricingRuleServicesTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_current_discounts(self):
        current_discount = services.get_current_discounts()
        self.assertEqual(len(current_discount), 2)
        self.assertIsInstance(current_discount[0], TwoForOneDiscount)
        self.assertIsInstance(current_discount[1], PercentageDiscount)
