# Cabify Code Challenge

This code challenge has been completed by Raúl González.

## Solution's guide

The pricing rule is a simple abstract class called *PricingRule*.

This abstract call implements some methods to validate if each discount is applicable to a checkout. In resume, 
it checks if a discount is applicable by target, the kind of the product, and by the quantity prerequisite.

Currently We have three kind of discount rules:

- Two for One discount (TwoForOneDiscount). The marketing department believes in 2-for-1 promotions 
(buy two of the same product, get one free), and would like for there to be a 2-for-1 special on VOUCHER items.
    
    
    DiscountRuleConfig(
        title="Two For One",
        target_type=ALL_TARGET_TYPE,
        value_type="percentage",
        value=-100,
        prerequisite_quantity=2,
        entitled_quantity=1
    )
    
- Percentage discount (PercentageDiscount). The CFO insists that the best way to increase sales is with 
discounts on bulk purchases (buying x or more of a product, the price of that product is reduced), and demands that 
if you buy 3 or more TSHIRT items, the price per unit should be 19.00€.
    
    
    PRICING_RULE_BULK_PURCHASE_ALL = DiscountRuleConfig(
        title="Bulk Purchase",
        target_type=ALL_TARGET_TYPE,
        value_type=PERCENTAGE_TYPE,
        value=5,
        prerequisite_quantity=3,
        entitled_quantity=1
    )

- Fixed amount discount (FixedAmountDiscount). This discount substract to the checkout price the value of the discount.

To set up each discount we have a data structure called *DiscountRuleConfig*. This structure has the fields needed 
to configure a dicount:

    - title: str
    - target_type: str
    - value_type: str
    - value: int
    - prerequisite_quantity: int
    - entitled_quantity: int
    
New discount rules can be implemented in easy way. You can create new Discount Rules overriding the PricingRule 
abstract class and implementing the *apply_to_price_purchase* method.

    # Python imports
    # Flask imports
    # Third-Party imports
    # Project Imports
    from apps.pricing_rules.base_rules import PricingRule


    NewDiscountRule(PricingRule):

        def apply_to_price_purchase(self, purchase):
            ...

Finally, you can set up your discounts implemented using the *CURRENT_DISCOUNTS_RULES* variable in the settings 
of the application:

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

## Decision made

- To add items to the cart you need to pass the code of the product and a quantity. We use the following JSON Schema
to achieve this:


    [
        {
            "product": "VOUCHER",
            "quantity": 2
        },
        {
            "product": "TSHIRT",
            "quantity": 4
        }
    ]
    
- For simplicity we have not added persistence to discount rules. With this feature we could obtain an admin interface
to configure and maintain our discounts. This could be a feature implemented in the feature. We could have fields like
active, start date and end date which could be interesting to add to our discounts if we have this admin interface. In
this way, we will have a manner to change any discount on the fly.

## Future outlines

- Pricing rules persistence and an admin interface to manage our discount rules.
- Pricing rules in a cache service. 
- New discounts rules.
- Split current checkout class in Carts and Checkouts.
- API Authentication.
- Microservices adoption.
- Event data architecture:
    - checkout_created 
    - discount_used
    - etc.
- Event data and statistics of usage.
- Put product API inside Elasticsearch cluster.
- Improve and complete acceptance tests suite.