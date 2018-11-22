# Python imports
import importlib
# Flask imports
# Third-Party imports
# Project Imports
from apps.pricing_rules.settings import CURRENT_DISCOUNTS_RULES


def instance_discount_from_module(module, class_name, configuration):
    module = importlib.import_module(module)
    class_ = getattr(module, class_name)
    return class_(config=configuration)


def get_current_discounts(discount_rules=CURRENT_DISCOUNTS_RULES):
    current_discounts = []
    for discount_config_rule in discount_rules:
        instance = instance_discount_from_module(
            module=discount_config_rule['module'],
            class_name=discount_config_rule['class'],
            configuration=discount_config_rule['configuration']
        )
        current_discounts.append(instance)
    return current_discounts
