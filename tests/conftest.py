"""
Fixtures list
"""

pytest_plugins = [
    "fixtures.api.create_positive_subscription",
    "fixtures.api.create_subscription_with_zero_time",
    "fixtures.api.fill_subscriptions_list",
    "fixtures.clean"
]
