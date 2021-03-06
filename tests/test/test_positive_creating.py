"""
Positive tests of subscriptions creating
"""

import dateutil.parser
import hamcrest as hc
import pytest

import settings
from src.subscription import create_subscription
from tests.data.subscription import positive
from utils.api_requests import send_request


@pytest.mark.creating
@pytest.mark.positive
def test_creating_with_correct_data(create_correct_subscription):
    """
    Test of creating subscription with correct data
    """

    subscription_list = send_request()

    hc.assert_that(
        actual=subscription_list,
        matcher=hc.has_item(hc.has_entries({
            'email': positive.email,
            'name': positive.name
        })),
        reason="New subscription not added at list"
    )

    expiration_date = dateutil.parser.parse(subscription_list[0]['expired_at'])
    creation_date = dateutil.parser.parse(subscription_list[0]['created_at'])

    hc.assert_that(
        actual=f"{(expiration_date-creation_date).days}d",
        matcher=hc.equal_to(positive.time.replace(" ", "")),
        reason="Invalid subscription time"
    )


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
