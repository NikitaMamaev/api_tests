"""
Create subscription with positive data
"""

import hamcrest as hc
import pytest

from src.subscribe import create_subscription, delete_subscriptions
from tests.data.subscribe import empty_name


@pytest.fixture(scope='function')
def create_subscription_with_empty_name(request):
    """
    Create subscription before test
    """

    response = create_subscription(empty_name)

    hc.assert_that(
        actual=response,
        matcher=hc.has_key('id'),
        reason=f'There is no key "id" in response: {response}'
    )

    request.addfinalizer(delete_subscriptions)
