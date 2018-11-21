# Python imports
import unittest
from decimal import Decimal
# Flask imports
# Third-Party imports
# Project Imports
from apps.checkouts.tests.mocks import CheckoutFactory
from apps.pricing_rules.percentage_discount import PercentageDiscount
from apps.pricing_rules.tests import mocks
from apps.products.tests.mocks import ProductFactory
from apps.purchase_items.tests.mocks import PurchaseItemFactory


class PricingRuleTwoForOneTestCase(unittest.TestCase):

    def setUp(self):
        self.product = ProductFactory()
        self.checkout = CheckoutFactory()
        self.purchase_item = PurchaseItemFactory(
            product=self.product,
            checkout=self.checkout
        )
        self.product.purchases.append(self.purchase_item)
        self.checkout.purchases.append(self.purchase_item)

    def test_is_applicable_by_target_type_target_all(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_ALL)
        self.assertTrue(pricing_rule.is_applicable_by_target_type(target=self.purchase_item.product.code))

    def test_is_applicable_by_target_type_target_concrete_product(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_VOUCHER)
        self.product.code = "VOUCHER"
        self.assertTrue(pricing_rule.is_applicable_by_target_type(target=self.purchase_item.product.code))

    def test_is_not_applicable_by_target_type_target_concrete_product(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_VOUCHER)
        self.assertFalse(pricing_rule.is_applicable_by_target_type(target=self.purchase_item.product.code))

    def test_is_applicable_by_quantity_greater_than(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_ALL)
        self.purchase_item.quantity = 3
        self.assertTrue(pricing_rule.is_applicable_by_quantity(quantity=self.purchase_item.quantity))

    def test_is_applicable_by_quantity_less_than(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_ALL)
        self.purchase_item.quantity = 1
        self.assertFalse(pricing_rule.is_applicable_by_quantity(quantity=self.purchase_item.quantity))

    def test_is_applicable_to_purchase_all_targets_quantity_greater(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_ALL)
        self.purchase_item.quantity = 3
        self.assertTrue(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_is_applicable_to_purchase_all_targets_quantity_less(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_ALL)
        self.purchase_item.quantity = 1
        self.assertFalse(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_is_applicable_to_purchase_concrete_target_quantity_greater(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_VOUCHER)
        self.product.code = "VOUCHER"
        self.purchase_item.quantity = 3
        self.assertTrue(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_is_applicable_to_purchase_different_target_quantity_greater(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_VOUCHER)
        self.purchase_item.quantity = 3
        self.assertFalse(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_is_applicable_to_purchase_concrete_target_quantity_less(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_VOUCHER)
        self.product.code = "VOUCHER"
        self.purchase_item.quantity = 1
        self.assertFalse(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_is_applicable_to_purchase_different_target_quantity_less(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_VOUCHER)
        self.purchase_item.quantity = 1
        self.assertFalse(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_apply_to_price_purchase_all_targets_quantity_greater(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_ALL)
        self.purchase_item.quantity = 3
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price - (self.purchase_item.price * Decimal(pricing_rule.value / 100))
        )
        self.purchase_item.quantity = 5
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price - (self.purchase_item.price * Decimal(pricing_rule.value / 100))
        )
        self.purchase_item.quantity = 567
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price - (self.purchase_item.price * Decimal(pricing_rule.value / 100))
        )
        self.product.db_price = 20.00
        self.purchase_item.quantity = 3
        self.assertEqual(
            round(pricing_rule.apply_to_price_purchase(purchase=self.purchase_item), 2),
            Decimal(57.00)
        )

    def test_apply_to_price_purchase_all_targets_quantity_less(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_ALL)
        self.purchase_item.quantity = 2
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price
        )

    def test_apply_to_price_purchase_concrete_target_quantity_greater(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_VOUCHER)
        self.product.code = "VOUCHER"
        self.purchase_item.quantity = 3
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price - (self.purchase_item.price * Decimal(pricing_rule.value / 100))
        )
        self.purchase_item.quantity = 5
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price - (self.purchase_item.price * Decimal(pricing_rule.value / 100))
        )
        self.purchase_item.quantity = 567
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price - (self.purchase_item.price * Decimal(pricing_rule.value / 100))
        )
        self.product.db_price = 20.00
        self.purchase_item.quantity = 3
        self.assertEqual(
            round(pricing_rule.apply_to_price_purchase(purchase=self.purchase_item), 2),
            Decimal(57.00)
        )

    def test_apply_to_price_purchase_concrete_target_quantity_less(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_VOUCHER)
        self.product.code = "VOUCHER"
        self.purchase_item.quantity = 1
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price
        )

    def test_apply_to_price_purchase_different_target_quantity_greater(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_VOUCHER)
        self.purchase_item.quantity = 3
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price
        )

    def test_apply_to_price_purchase_different_target_quantity_less(self):
        pricing_rule = PercentageDiscount(config=mocks.PRICING_RULE_BULK_PURCHASE_VOUCHER)
        self.purchase_item.quantity = 1
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price
        )
