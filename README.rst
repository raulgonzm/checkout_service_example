=========================================================
Code Challenge. Checkout Service
=========================================================

Building the development infrastructure
==========================================

- Replace the env variable with your local code path within *infrastructure/build_env.sh* file.

``export BACKEND_SERVICE_CODE=<your-local-path>``

- Building Checkout Services. Run Docker build for each service

``
chmod 774 ./infrastructure/build_docker.sh
./infrastructure/build_docker.sh
``

- Start Docker containers for each service

``
chmod 774 ./infrastructure/docker_up.sh
./infrastructure/docker_up.sh
``

- SSH connect with the container

``
chmod 774 ./infrastructure/docker_ssh.sh
./infrastructure/docker_ssh.sh
``

- Loading Product fixture (Execute one at a time)

``
root@5f77ebc363c8:/checkouts# python manage.py load_fixtures
``

- Right now you got the checkout service running in your machine


Checkout Service API
==========================================

You have a Postman collection and a Postman environment inside the project. This collection has a complete
aggregation of Checkout service API endpoints.

Principally you have three endpoints:

- Product List
``
GET /api/rest/v1_0/products/
``

An example of response would be:

``
[
    {
        "name": "Cabify Mug",
        "price": "7.50",
        "code": "MUG"
    },
    {
        "name": "Cabify T-Shirt",
        "price": "20.00",
        "code": "TSHIRT"
    },
    {
        "name": "Cabify Voucher",
        "price": "5.00",
        "code": "VOUCHER"
    }
]
``

- Checkout creation
``
POST /api/rest/v1_0/checkouts/
``

The request body should be something like:
``
[
	{
		"product": 1,
		"quantity": 2
	},
	{
		"product": 2,
		"quantity": 4
	}
]
``

An example of response would be:
``
{
    "checkout_number": "067d6009-cfc1-4048-ba8d-07954577faa2",
    "discount": "45.00",
    "price": "90.00",
    "id": 1,
    "purchases": [
        {
            "price": "10.00",
            "product": {
                "name": "Cabify Voucher",
                "price": "5.00",
                "code": "VOUCHER"
            },
            "quantity": 2
        },
        {
            "price": "80.00",
            "product": {
                "name": "Cabify T-Shirt",
                "price": "20.00",
                "code": "TSHIRT"
            },
            "quantity": 4
        }
    ],
    "total": "45.00"
}
``

- Checkout detail
``
GET /api/rest/v1_0/checkouts/<checkout_id>/
``

Pricing Rules
==========================================

There are two pricing rules configured by default right now. You can check this inside of
*/apps/pricing_rules/settings.py* file.

``
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
``

We have two discounts applied: a *"two for one"* discount and a percentage discount. Both have their own configuration
inside PRICING_RULE_TWO_FOR_ONE_ALL and PRICING_RULE_BULK_PURCHASE_ALL configuration vars.

We can check one of them these configurations:

``
PRICING_RULE_TWO_FOR_ONE_ALL = DiscountRuleConfig(
    title="Two For One",
    target_type=ALL_TARGET_TYPE,
    value_type="percentage",
    value=-100,
    prerequisite_quantity=2,
    entitled_quantity=1
)
``

This show us that the discount is a DiscountRuleConfig for all products (ALL_TARGET_TYPE), "percentage" is his
type and we have a quantity prerequisite with two units.

You can change this configuration customizing the target (setting up a product code inside. i.e. "VOUCHE") or
customizing the quantity prerequisite.

Also you can configure the current discounts customizing the CURRENT_DISCOUNTS_RULES list:

``
CURRENT_DISCOUNTS_RULES = [
    {
        "module": "apps.pricing_rules.two_for_one_discount",
        "class": "TwoForOneDiscount",
        "configuration": PRICING_RULE_TWO_FOR_ONE_ALL
    },
]
``

Now we have only a single discount applied to checkouts.


Running testing
==========================================

- To run tests you can type
``
root@5f77ebc363c8:/checkouts# python manage.py test
``

- If you want to run tests with coverage
``
root@5f77ebc363c8:/checkouts# coverage run manage.py test
root@5f77ebc363c8:/checkouts# coverage report
``



