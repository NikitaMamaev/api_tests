"""
Fixtures list
"""

pytest_plugins = [
    "fixtures.clean",
    "fixtures.create_positive_subscription",
    "fixtures.create_subscription_with_zero_time",
    "fixtures.fill_subscriptions_list"
]
