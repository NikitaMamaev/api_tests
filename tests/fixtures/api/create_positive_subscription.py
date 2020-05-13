"""
Create subscription with positive data
"""

import hamcrest as hc
import pytest

from src.subscribe import create_subscription
from tests.data.subscribe import positive


@pytest.fixture(scope='function')
def create_positive_subscription(request, clean):
    """
    Create subscription before test
    """

    response = create_subscription(positive)

    hc.assert_that(
        actual=response,
        matcher=hc.has_key('id'),
        reason=f'There is no key "id" in response: {response}'
    )
