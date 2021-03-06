"""
Fill the subscriptions list
"""

import hamcrest as hc
import pytest

import settings
from src.subscription import create_subscription
from tests.data.subscription import Subscription
from utils.api_requests import send_request


@pytest.fixture(scope='function')
def fill_subscriptions_list(request, clean):
    """
    Create five subscriptions before testing
    """

    for index in range(settings.LIST_LENGTH):
        create_subscription(
            subcription=Subscription(
                email=f"email{index+1}@example.com",
                name=f"name{index+1} lastname{index+1}"
            )
        )

    hc.assert_that(
        actual=send_request(),
        matcher=hc.has_length(settings.LIST_LENGTH),
        reason="The list is not full"
    )
