"""
Positive tests of subscriptions creating
"""

import hamcrest as hc
import pytest

import settings
from src.subscribe import create_subscription
from tests.data.subscribe import positive
from utils.api_requests import send_request


@pytest.mark.api
@pytest.mark.creating
@pytest.mark.positive
def test_creating_with_correct_data(create_positive_subscription):
    """
    Test of creating subscription with correct data
    """

    hc.assert_that(
        actual=send_request(),
        matcher=hc.has_item(hc.has_entries({
            'email': positive.email,
            'name': positive.name
        })),
        reason="New subscription not added at list"
    )


@pytest.mark.api
@pytest.mark.creating
@pytest.mark.positive
def test_sixth_subscription_creating(fill_subscriptions_list):
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
        reason="Incorrect length of the list"
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
