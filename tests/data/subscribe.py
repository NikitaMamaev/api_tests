"""
Subscribe data for tests
"""

from dataclasses import dataclass


@dataclass
class Subscribe:
    """
    Supscribe parameters
    """
    email: str = ""
    name: str = ""
    time: str = "1d"


positive = Subscribe(
    email="subscribe@example.com",
    name="Name Lastname"
)

negative_email = Subscribe(
    email="incorrect_email",
    name="Incorrect Email"
)

negative_time = Subscribe(
    email="negative_time@example.com",
    name="Negative Time",
    time="negative time"
)

empty_email = Subscribe(
    email="",
    name="Empty Email"
)

empty_name = Subscribe(
    email="empty_name@example.com",
    name=""
)

empty_time = Subscribe(
    email="empty_time@example.com",
    name="Empty Time",
    time=""
)

long_time = Subscribe(
    email="long_time@example.com",
    name="Long Time",
    time="65536d"
)
