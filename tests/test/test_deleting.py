"""
Subscribe deleting test
"""

import hamcrest as hc
import pytest

from src.subscribe import delete_subscriptions
from utils.api_requests import send_request


@pytest.mark.api
@pytest.mark.deleting
def test_subscribe_deleting(create_positive_subscription):
    """
    Test for deleting all subscriptions
    """

    response = delete_subscriptions()

    hc.assert_that(
        actual=response,
        matcher=hc.has_entries({"removed": hc.greater_than(0)}),
        reason="There was no subscriptions"
    )

    subscription_list = send_request()

    hc.assert_that(
        actual=subscription_list,
        matcher=hc.empty(),
        reason=f"There are subscriptions after deleting: {subscription_list}"
    )
