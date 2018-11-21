# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps.pricing_rules.datastructures import DiscountRuleConfig
from apps.pricing_rules import settings

PRICING_RULE_TWO_FOR_ONE_ALL = DiscountRuleConfig(
    title="Two For One",
    target_type=settings.ALL_TARGET_TYPE,
    value_type="percentage",
    value=-100,
    prerequisite_quantity=2,
    entitled_quantity=1
)

PRICING_RULE_TWO_FOR_ONE_VOUCHER = DiscountRuleConfig(
    title="Two For One",
    target_type="VOUCHER",
    value_type=settings.PERCENTAGE_TYPE,
    value=-100,
    prerequisite_quantity=2,
    entitled_quantity=1
)

PRICING_RULE_FIXED_AMOUNT_ALL = DiscountRuleConfig(
    title="Fixed Amount",
    target_type=settings.ALL_TARGET_TYPE,
    value_type=settings.FIXED_AMOUNT_TYPE,
    value=5,
    prerequisite_quantity=0,
    entitled_quantity=1
)

PRICING_RULE_FIXED_AMOUNT_VOUCHER = DiscountRuleConfig(
    title="Fixed Amount",
    target_type="VOUCHER",
    value_type=settings.FIXED_AMOUNT_TYPE,
    value=5,
    prerequisite_quantity=0,
    entitled_quantity=1
)

PRICING_RULE_BULK_PURCHASE_ALL = DiscountRuleConfig(
    title="Bulk Purchase",
    target_type=settings.ALL_TARGET_TYPE,
    value_type=settings.PERCENTAGE_TYPE,
    value=5,
    prerequisite_quantity=3,
    entitled_quantity=1
)

PRICING_RULE_BULK_PURCHASE_VOUCHER = DiscountRuleConfig(
    title="Bulk Purchase",
    target_type="VOUCHER",
    value_type=settings.PERCENTAGE_TYPE,
    value=5,
    prerequisite_quantity=3,
    entitled_quantity=1
)
