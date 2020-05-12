"""
Subscribe data for tests
"""

from dataclasses import dataclass


@dataclass
class Subscribe:
    """
    Supscribe parameters
    """
    email: str
    name: str
    time: str


positive = Subscribe(
    email="subscribe@example.com",
    name="Name Lastname",
    time="-1d"
)
