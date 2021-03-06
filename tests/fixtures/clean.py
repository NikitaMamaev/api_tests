"""
Delete subscriptions before and after testing
"""

import pytest

from src.subscription import delete_subscriptions
from utils.api_requests import send_request


@pytest.fixture(scope='function')
def clean(request):
    """
    Delete subscriptions if the list is not empty
    """

    if send_request():
        delete_subscriptions()

    request.addfinalizer(delete_subscriptions)
