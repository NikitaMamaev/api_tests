"""
Subscribe creating tests
"""

import hamcrest as hc
import pytest

from src.api_requests import send_request


@pytest.mark.api
def test_subscribe_creating():
    payload = {
        'email': 'a123@aaaa.aaa',
        'name': 'a a',
        'time': '5d'
    }

    response = send_request(
        method='post',
        data=payload
    )

    hc.assert_that(
        response,
        hc.not_(hc.empty())
    )
