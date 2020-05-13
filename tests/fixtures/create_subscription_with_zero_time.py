"""
Create subscription with positive data
"""

import hamcrest as hc
import pytest

from src.subscribe import create_subscription
from tests.data.subscription import zero_time


@pytest.fixture(scope='function')
def create_subscription_with_zero_time(request, clean):
    """
    Create subscription before test
    """

    response = create_subscription(zero_time)

    hc.assert_that(
        actual=response,
        matcher=hc.has_key('id'),
        reason=f'There is no key "id" in response: {response}'
    )
