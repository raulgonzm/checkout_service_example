# Python imports
from typing import NamedTuple
# Flask imports
# Third-Party imports
# Project Imports


class DiscountRuleConfig(NamedTuple):
    title: str
    target_type: str
    value_type: str
    value: int
    prerequisite_quantity: int
    entitled_quantity: int
