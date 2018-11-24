.. image:: https://img.shields.io/badge/build-passed-green.svg
   :target: https://img.shields.io/
   :alt: Build Status
.. image:: https://img.shields.io/badge/coverage-100%25-green.svg
   :target: https://img.shields.io/
   :alt: Build Status
.. image:: https://img.shields.io/badge/python-3.4%20%7C%203.5%20%7C%203.6%20%7C%203.7-blue.svg
   :target: https://img.shields.io/
   :alt: Build Status

=========================================================
Code Challenge. Checkout Service
=========================================================

Building the development infrastructure
==========================================

- Replace the env variable within your local code path in *infrastructure/build_env.sh* file.

.. code-block::
::

    export BACKEND_SERVICE_CODE=<your-local-path>

- Building Checkout Services. Run Docker build for each service

.. code-block::
::

    chmod 774 ./infrastructure/build_docker.sh
    ./infrastructure/build_docker.sh


- Start Docker containers for each service

.. code-block::
::

    chmod 774 ./infrastructure/docker_up.sh
    ./infrastructure/docker_up.sh


- SSH connect with the container

.. code-block::
::

    chmod 774 ./infrastructure/docker_ssh.sh
    ./infrastructure/docker_ssh.sh


- Loading Product fixture (Execute one at a time)

.. code-block::
::

    root@5f77ebc363c8:/checkouts# python manage.py load_fixtures


- Right now you got the checkout service running in your machine


Checkout Service API
==========================================

You have a Postman collection and a Postman environment inside the project. This collection has a complete
aggregation of Checkout service API endpoints.

Principally you have three endpoints:

- Product List
.. code-block::
::

    GET /api/rest/v1_0/products/


    An example of response would be:

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


- Checkout creation

.. code-block::
::

    POST /api/rest/v1_0/checkouts/


The request body should be something like:

.. code-block::
::

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


An example of response would be:

.. code-block::
::

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


- Checkout detail

.. code-block::
::

    GET /api/rest/v1_0/checkouts/<checkout_number>/


Pricing Rules
==========================================

There are two pricing rules configured by default right now. You can check this inside of
*/apps/pricing_rules/settings.py* file.

.. code-block::
::

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


We have two discounts applied: a *"two for one"* discount and a percentage discount. Both have their own configuration
inside PRICING_RULE_TWO_FOR_ONE_ALL and PRICING_RULE_BULK_PURCHASE_ALL configuration vars.

We can check one of them these configurations:

.. code-block::
::

    PRICING_RULE_TWO_FOR_ONE_ALL = DiscountRuleConfig(
        title="Two For One",
        target_type=ALL_TARGET_TYPE,
        value_type="percentage",
        value=-100,
        prerequisite_quantity=2,
        entitled_quantity=1
    )


This show us that the discount is a DiscountRuleConfig for all products (ALL_TARGET_TYPE), "percentage" is his
type and we have a quantity prerequisite with two units.

You can change this configuration customizing the target (setting up a product code inside. i.e. "VOUCHE") or
customizing the quantity prerequisite.

Also you can configure the current discounts customizing the CURRENT_DISCOUNTS_RULES list:

.. code-block::
::

    CURRENT_DISCOUNTS_RULES = [
        {
            "module": "apps.pricing_rules.two_for_one_discount",
            "class": "TwoForOneDiscount",
            "configuration": PRICING_RULE_TWO_FOR_ONE_ALL
        },
    ]


Now we have only a single discount applied to checkouts.


Also, you can create new Discount Rules overriding PricingRule abstract class and implementing the
*apply_to_price_purchase* method.

.. code-block::
::

    # Python imports
    # Flask imports
    # Third-Party imports
    # Project Imports
    from apps.pricing_rules.base_rules import PricingRule


    NewDiscountRule(PricingRule):

        def apply_to_price_purchase(self, purchase):
            ...


Running testing
==========================================

- To run tests you can type
.. code-block::
::

    root@5f77ebc363c8:/checkouts# python manage.py test


- If you want to run tests with coverage
.. code-block::
::

    root@5f77ebc363c8:/checkouts# coverage run manage.py test
    root@5f77ebc363c8:/checkouts# coverage report




