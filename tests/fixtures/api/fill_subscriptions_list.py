"""
Fill the subscriptions list
"""

import hamcrest as hc
import pytest

from src.subscribe import create_subscription, delete_subscriptions
from tests.data.subscribe import Subscribe
from utils.api_requests import send_request


@pytest.fixture(scope='function')
def fill_subscriptions_list(request):
    """
    Create five subscriptions before test
    """

    for index in range(5):
        create_subscription(
            subcription=Subscribe(
                email=f"email{index+1}@example.com",
                name=f"name{index+1} lastname{index+1}",
                time="1d"
            )
        )

    hc.assert_that(
        actual=send_request(),
        matcher=hc.has_length(5)
    )

    request.addfinalizer(delete_subscriptions)
