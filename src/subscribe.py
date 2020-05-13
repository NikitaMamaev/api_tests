"""
Subsciption creating and deleting methods
"""

from tests.data.subscription import Subscription
from utils.api_requests import send_request


def create_subscription(subcription: Subscription) -> dict:
    """
    Create subscription
    :param subcription: subscription data
    """

    payload = {
        'email': subcription.email,
        'name': subcription.name,
        'time': subcription.time
    }

    response = send_request(
        method='post',
        data=payload
    )

    return response


def delete_subscriptions() -> dict:
    """
    Delete all subscriptions
    """

    response = send_request(
        method='delete'
    )

    return response
