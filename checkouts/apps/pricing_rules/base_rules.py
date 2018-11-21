# Python imports
from abc import ABCMeta, abstractmethod
# Flask imports
# Third-Party imports
# Project Imports
from apps.pricing_rules.datastructures import DiscountRuleConfig
from apps.pricing_rules.settings import ALL_TARGET_TYPE


class PricingRule(metaclass=ABCMeta):

    def __init__(self, config: DiscountRuleConfig):
        (self.title, self.target_type, self.value_type, self.value,
         self.prerequisite_quantity, self.entitled_quantity) = config

    def is_applicable_by_target_type(self, target):
        return any([
            ALL_TARGET_TYPE in self.target_type,
            target in self.target_type
        ])

    def is_applicable_by_quantity(self, quantity):
        return quantity >= self.prerequisite_quantity

    def is_applicable_to_purchase(self, purchase):
        return all([
            self.is_applicable_by_target_type(target=purchase.product.code),
            self.is_applicable_by_quantity(quantity=purchase.quantity)
        ])

    @abstractmethod
    def apply_to_price_purchase(self, purchase):
        pass
