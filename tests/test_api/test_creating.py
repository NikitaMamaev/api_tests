"""
Subscribe creating tests
"""

import hamcrest as hc
import pytest

import settings
from src.subscribe import create_subscription
from tests.data.subscribe import positive
from utils.api_requests import send_request


@pytest.mark.api
def test_positive_creating(create_positive_subscription):
    """
    Positive subscribe test
    """

    hc.assert_that(
        actual=send_request(),
        matcher=hc.has_length(1),
        reason="Wrong length of the list"
    )

    hc.assert_that(
        actual=send_request()[0],
        matcher=hc.has_entries({
            'email': positive.email,
            'name': positive.name
        }),
        reason="New subscription not added at list"
    )

@pytest.mark.api
def test_create_sixth_subscription(fill_subscriptions_list):
    """
    Sixth subscription creating test
    """

    create_subscription(positive)

    subscription_list = send_request()

    hc.assert_that(
        actual=subscription_list,
        matcher=hc.has_item(
            hc.has_entries({
                    'email': positive.email,
                    'name': positive.name
                })
        ),
        reason="New subscription not added at list"
    )

    hc.assert_that(
        actual=subscription_list,
        matcher=hc.has_length(settings.LIST_LENGTH),
        reason="Wrong length of the list"
    )

    hc.assert_that(
        actual=subscription_list,
        matcher=hc.not_(hc.has_item(
            hc.has_entries({
                'email': 'email1@example.com',
                'name': 'name1 lastname1',
            })
        )),
        reason="First subscription has not left the list"
    )
