# Python imports
import importlib
# Flask imports
# Third-Party imports
# Project Imports
from apps.pricing_rules.settings import CURRENT_DISCOUNTS_RULES


def get_current_discounts():
    current_discounts = []
    for discount_config_rule in CURRENT_DISCOUNTS_RULES:
        module = importlib.import_module(discount_config_rule['module'])
        class_ = getattr(module, discount_config_rule['class'])
        instance = class_(config=discount_config_rule['configuration'])
        current_discounts.append(instance)
    return current_discounts
