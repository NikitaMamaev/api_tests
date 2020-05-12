"""
Subscribe creating tests
"""

import hamcrest as hc
import pytest

from src.api_requests import send_request
from tests.data.subscribe import positive


@pytest.mark.api
def test_subscribe_creating():
    """
    Positive subscribe test
    """

    payload = {
        'email': positive.email,
        'name': positive.name,
        'time': positive.time
    }

    response = send_request(
        method='post',
        data=payload
    )

    hc.assert_that(
        response,
        hc.not_(hc.empty())
    )
