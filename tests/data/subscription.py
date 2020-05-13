"""
Subscription data for tests
"""

from dataclasses import dataclass


@dataclass
class Subscription:
    """
    Subscription parameters
    """

    email: str = ""
    name: str = ""
    time: str = "1d"


empty_email = Subscription(
    email="",
    name="Empty Email"
)

empty_name = Subscription(
    email="empty_name@example.com",
    name=""
)

empty_time = Subscription(
    email="empty_time@example.com",
    name="Empty Time",
    time=""
)

negative_email = Subscription(
    email="incorrect_email",
    name="Incorrect Email"
)

negative_name = Subscription(
    email="incorrect_name@example.com",
    name="./*#@!%|^&*(),'`~;:+-}_=[]?\"<>{",
    time="incorrect name"
)

negative_time = Subscription(
    email="incorrect_time@example.com",
    name="Incorrect Time",
    time="incorrect time"
)

positive = Subscription(
    email="positive@example.com",
    name="Positive Name"
)

zero_time = Subscription(
    email="zero_time@example.com",
    name="Zero Time",
    time="0d"
)
