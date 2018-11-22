# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps.pricing_rules.datastructures import DiscountRuleConfig


ALL_TARGET_TYPE = "ALL"
PERCENTAGE_TYPE = "percentage"
FIXED_AMOUNT_TYPE = "fixed_amount"

PRICING_RULE_TWO_FOR_ONE_ALL = DiscountRuleConfig(
    title="Two For One",
    target_type=ALL_TARGET_TYPE,
    value_type="percentage",
    value=-100,
    prerequisite_quantity=2,
    entitled_quantity=1
)

PRICING_RULE_BULK_PURCHASE_ALL = DiscountRuleConfig(
    title="Bulk Purchase",
    target_type=ALL_TARGET_TYPE,
    value_type=PERCENTAGE_TYPE,
    value=5,
    prerequisite_quantity=3,
    entitled_quantity=1
)

CURRENT_DISCOUNTS_RULES = [
    {
        "module": "apps.pricing_rules.two_for_one_discount",
        "class": "TwoForOneDiscount",
        "configuration": PRICING_RULE_TWO_FOR_ONE_ALL
    },
    {
        "module": "apps.pricing_rules.percentage_discount",
        "class": "PercentageDiscount",
        "configuration": PRICING_RULE_BULK_PURCHASE_ALL
    }
]
