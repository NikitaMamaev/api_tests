"""
Subscribe data for tests
"""

from dataclasses import dataclass


@dataclass
class Subscribe:
    """
    Subscribe parameters
    """
    email: str = ""
    name: str = ""
    time: str = "1d"


positive = Subscribe(
    email="positive@example.com",
    name="Positive Name"
)

negative_email = Subscribe(
    email="incorrect_email",
    name="Incorrect Email"
)

negative_name = Subscribe(
    email="incorrect_name@example.com",
    name="./*#@!%|^&*(),'`~;:+-}_=[]?\"<>{",
    time="incorrect name"
)

negative_time = Subscribe(
    email="incorrect_time@example.com",
    name="Incorrect Time",
    time="incorrect time"
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

zero_time = Subscribe(
    email="zero_time@example.com",
    name="Zero Time",
    time="0d"
)
