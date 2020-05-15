"""
Subscriptions deleting test
"""

import hamcrest as hc
import pytest

from src.subscription import delete_subscriptions
from utils.api_requests import send_request


@pytest.mark.deleting
def test_subscribe_deleting(create_correct_subscription):
    """
    Test for deleting all subscriptions
    """

    response = delete_subscriptions()

    hc.assert_that(
        actual=response,
        matcher=hc.has_entries({"removed": hc.greater_than(0)}),
        reason="There was no subscriptions!"
    )

    subscription_list = send_request()

    hc.assert_that(
        actual=subscription_list,
        matcher=hc.empty(),
        reason="List has not cleared!"
    )
