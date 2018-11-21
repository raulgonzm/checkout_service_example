# Python imports
import unittest
# Flask imports
# Third-Party imports
# Project Imports
from apps.checkouts.tests.mocks import CheckoutFactory
from apps.pricing_rules.fixed_amount_discount import FixedAmountDiscount
from apps.pricing_rules.tests import mocks
from apps.products.tests.mocks import ProductFactory
from apps.purchase_items.tests.mocks import PurchaseItemFactory


class PricingRuleFixedAmountTestCase(unittest.TestCase):

    def setUp(self):
        self.product = ProductFactory()
        self.product.db_price = self.product.db_price + mocks.PRICING_RULE_FIXED_AMOUNT_ALL.value
        self.checkout = CheckoutFactory()
        self.purchase_item = PurchaseItemFactory(
            product=self.product,
            checkout=self.checkout
        )
        self.product.purchases.append(self.purchase_item)
        self.checkout.purchases.append(self.purchase_item)

    def test_is_applicable_by_target_type_target_all(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_ALL)
        self.assertTrue(pricing_rule.is_applicable_by_target_type(target=self.purchase_item.product.code))

    def test_is_applicable_by_target_type_target_concrete_product(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_VOUCHER)
        self.product.code = "VOUCHER"
        self.assertTrue(pricing_rule.is_applicable_by_target_type(target=self.purchase_item.product.code))

    def test_is_not_applicable_by_target_type_target_concrete_product(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_VOUCHER)
        self.assertFalse(pricing_rule.is_applicable_by_target_type(target=self.purchase_item.product.code))

    def test_is_applicable_by_quantity_greater_than(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_ALL)
        self.purchase_item.quantity = 3
        self.assertTrue(pricing_rule.is_applicable_by_quantity(quantity=self.purchase_item.quantity))

    def test_is_applicable_by_quantity_less_than(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_ALL)
        self.purchase_item.quantity = 1
        self.assertTrue(pricing_rule.is_applicable_by_quantity(quantity=self.purchase_item.quantity))

    def test_is_applicable_to_purchase_all_targets_quantity_greater(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_ALL)
        self.purchase_item.quantity = 3
        self.assertTrue(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_is_applicable_to_purchase_all_targets_quantity_less(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_ALL)
        self.purchase_item.quantity = 1
        self.assertTrue(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_is_applicable_to_purchase_concrete_target_quantity_greater(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_VOUCHER)
        self.product.code = "VOUCHER"
        self.purchase_item.quantity = 3
        self.assertTrue(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_is_applicable_to_purchase_different_target_quantity_greater(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_VOUCHER)
        self.purchase_item.quantity = 3
        self.assertFalse(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_is_applicable_to_purchase_concrete_target_quantity_less(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_VOUCHER)
        self.product.code = "VOUCHER"
        self.purchase_item.quantity = 1
        self.assertTrue(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_is_applicable_to_purchase_different_target_quantity_less(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_VOUCHER)
        self.purchase_item.quantity = 1
        self.assertFalse(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_apply_to_price_purchase_all_targets_quantity_greater(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_ALL)
        self.purchase_item.quantity = 2
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price - pricing_rule.value
        )
        self.purchase_item.quantity = 3
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price - pricing_rule.value
        )
        self.purchase_item.quantity = 1586
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price - pricing_rule.value
        )

    def test_apply_to_price_purchase_all_targets_quantity_greater_total_price_less_than_zero(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_ALL)
        self.product.db_price = pricing_rule.value - 1
        self.purchase_item.quantity = 1
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            0
        )

    def test_apply_to_price_purchase_all_targets_quantity_less(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_ALL)
        self.purchase_item.quantity = 1
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price - pricing_rule.value
        )

    def test_apply_to_price_purchase_concrete_target_quantity_greater(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_VOUCHER)
        self.product.code = "VOUCHER"
        self.purchase_item.quantity = 2
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price - pricing_rule.value
        )
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_VOUCHER)
        self.purchase_item.quantity = 498
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price - pricing_rule.value
        )

    def test_apply_to_price_purchase_concrete_target_quantity_greater_total_price_less_than_zero(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_VOUCHER)
        self.product.code = "VOUCHER"
        self.product.db_price = pricing_rule.value - 1
        self.purchase_item.quantity = 1
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            0
        )

    def test_apply_to_price_purchase_concrete_target_quantity_less(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_VOUCHER)
        self.product.code = "VOUCHER"
        self.purchase_item.quantity = 1
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price - pricing_rule.value
        )

    def test_apply_to_price_purchase_different_target_quantity_greater(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_VOUCHER)
        self.purchase_item.quantity = 3
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price
        )

    def test_apply_to_price_purchase_different_target_quantity_less(self):
        pricing_rule = FixedAmountDiscount(config=mocks.PRICING_RULE_FIXED_AMOUNT_VOUCHER)
        self.purchase_item.quantity = 1
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price
        )

