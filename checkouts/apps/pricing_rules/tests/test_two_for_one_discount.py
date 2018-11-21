# Python imports
import unittest
# Flask imports
# Third-Party imports
# Project Imports
from apps.checkouts.tests.mocks import CheckoutFactory
from apps.pricing_rules.datastructures import DiscountRuleConfig
from apps.pricing_rules.settings import ALL_TARGET_TYPE
from apps.pricing_rules.tests import mocks
from apps.pricing_rules.two_for_one_discount import TwoForOneDiscount
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
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_ALL)
        self.assertTrue(pricing_rule.is_applicable_by_target_type(target=self.purchase_item.product.code))

    def test_is_applicable_by_target_type_target_concrete_product(self):
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_VOUCHER)
        self.product.code = "VOUCHER"
        self.assertTrue(pricing_rule.is_applicable_by_target_type(target=self.purchase_item.product.code))

    def test_is_not_applicable_by_target_type_target_concrete_product(self):
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_VOUCHER)
        self.assertFalse(pricing_rule.is_applicable_by_target_type(target=self.purchase_item.product.code))

    def test_is_applicable_by_quantity_greater_than(self):
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_ALL)
        self.purchase_item.quantity = 4
        self.assertTrue(pricing_rule.is_applicable_by_quantity(quantity=self.purchase_item.quantity))

    def test_is_applicable_by_quantity_less_than(self):
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_ALL)
        self.purchase_item.quantity = 1
        self.assertFalse(pricing_rule.is_applicable_by_quantity(quantity=self.purchase_item.quantity))

    def test_is_applicable_to_purchase_all_targets_quantity_greater(self):
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_ALL)
        self.purchase_item.quantity = 3
        self.assertTrue(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_is_applicable_to_purchase_all_targets_quantity_less(self):
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_ALL)
        self.purchase_item.quantity = 1
        self.assertFalse(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_is_applicable_to_purchase_concrete_target_quantity_greater(self):
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_VOUCHER)
        self.product.code = "VOUCHER"
        self.purchase_item.quantity = 3
        self.assertTrue(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_is_applicable_to_purchase_different_target_quantity_greater(self):
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_VOUCHER)
        self.purchase_item.quantity = 3
        self.assertFalse(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_is_applicable_to_purchase_concrete_target_quantity_less(self):
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_VOUCHER)
        self.product.code = "VOUCHER"
        self.purchase_item.quantity = 1
        self.assertFalse(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_is_applicable_to_purchase_different_target_quantity_less(self):
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_VOUCHER)
        self.purchase_item.quantity = 1
        self.assertFalse(pricing_rule.is_applicable_to_purchase(purchase=self.purchase_item))

    def test_apply_to_price_purchase_all_targets_quantity_greater(self):
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_ALL)
        self.purchase_item.quantity = 2
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            1
            * self.product.price
        )
        self.purchase_item.quantity = 3
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            2 * self.product.price
        )
        self.purchase_item.quantity = 4
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            2 * self.product.price
        )
        self.purchase_item.quantity = 5
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            3 * self.product.price
        )
        self.purchase_item.quantity = 6
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            3 * self.product.price
        )
        self.purchase_item.quantity = 7
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            4 * self.product.price
        )
        self.purchase_item.quantity = 8
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            4 * self.product.price
        )
        self.purchase_item.quantity = 53
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            27 * self.product.price
        )
        self.purchase_item.quantity = 1594
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            797
            * self.product.price
        )

    def test_apply_to_price_purchase_all_targets_quantity_less(self):
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_ALL)
        self.purchase_item.quantity = 1
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price
        )

    def test_apply_to_price_purchase_concrete_target_quantity_greater(self):
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_VOUCHER)
        self.product.code = "VOUCHER"
        self.purchase_item.quantity = 3
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            2 * self.product.price
        )
        self.purchase_item.quantity = 4
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            2 * self.product.price
        )
        self.purchase_item.quantity = 5
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            3 * self.product.price
        )
        self.purchase_item.quantity = 6
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            3 * self.product.price
        )
        self.purchase_item.quantity = 7
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            4 * self.product.price
        )
        self.purchase_item.quantity = 8
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            4 * self.product.price
        )
        self.purchase_item.quantity = 53
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            27 * self.product.price
        )
        self.purchase_item.quantity = 1594
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            797
            * self.product.price
        )

    def test_apply_to_price_purchase_concrete_target_quantity_less(self):
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_VOUCHER)
        self.product.code = "VOUCHER"
        self.purchase_item.quantity = 1
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price
        )

    def test_apply_to_price_purchase_different_target_quantity_greater(self):
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_VOUCHER)
        self.purchase_item.quantity = 3
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price
        )

    def test_apply_to_price_purchase_different_target_quantity_less(self):
        pricing_rule = TwoForOneDiscount(config=mocks.PRICING_RULE_TWO_FOR_ONE_VOUCHER)
        self.purchase_item.quantity = 1
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            self.purchase_item.price
        )

    def test_three_for_one(self):
        mock_3_for_1 = DiscountRuleConfig(
            title="Two For One",
            target_type=ALL_TARGET_TYPE,
            value_type="percentage",
            value=-100,
            prerequisite_quantity=3,
            entitled_quantity=1
        )
        pricing_rule = TwoForOneDiscount(config=mock_3_for_1)
        self.purchase_item.quantity = 3
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            1 * self.product.price
        )
        self.purchase_item.quantity = 4
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            2 * self.product.price
        )
        self.purchase_item.quantity = 5
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            2 * self.product.price
        )
        self.purchase_item.quantity = 6
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            2 * self.product.price
        )
        self.purchase_item.quantity = 7
        self.assertEqual(
            pricing_rule.apply_to_price_purchase(purchase=self.purchase_item),
            3 * self.product.price
        )
