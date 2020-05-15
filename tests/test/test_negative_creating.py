"""
Tests of subscription creating with incorrect data
"""

import hamcrest as hc
import pytest

from src.subscription import create_subscription
from tests.data.subscription import \
    empty_email, empty_name, empty_time, positive,\
    incorrect_email, incorrect_name, incorrect_time, zero_time
from utils.api_requests import send_request


@pytest.mark.creating
@pytest.mark.negative
def test_creating_existing_subscription(create_correct_subscription):
    """
    Try to create subscription with existing email
    """

    create_subscription(positive)

    hc.assert_that(
        actual=send_request(),
        matcher=hc.has_length(1),
        reason="Subscription with existing email should not be created!"
    )


@pytest.mark.creating
@pytest.mark.negative
def test_creating_with_empty_email(clean):
    """
    Try to create subscription with empty email
    """

    response = create_subscription(empty_email)

    hc.assert_that(
        actual=response,
        matcher=hc.has_entries({
            "error": hc.all_of(
                hc.contains_string("ValidationError"),
                hc.matches_regexp(r"Invalid.*email")
            )
        }),
        reason="ValidationError was expected"
    )

    hc.assert_that(
        actual=send_request(),
        matcher=hc.not_(hc.has_item(
            hc.has_entries({
                'email': empty_email.email,
                'name': empty_email.name,
            })
        )),
        reason="There is subscription with empty email in the list"
    )


@pytest.mark.creating
@pytest.mark.negative
def test_creating_with_empty_name(clean):
    """
    Try to create subscription with empty name
    """

    response = create_subscription(empty_name)

    hc.assert_that(
        actual=response,
        matcher=hc.has_entries({
            "error": hc.all_of(
                hc.contains_string("ValidationError"),
                hc.matches_regexp(r"Invalid.*name")
            )
        }),
        reason="ValidationError was expected"
    )

    hc.assert_that(
        actual=send_request(),
        matcher=hc.not_(hc.has_item(
            hc.has_entries({
                'email': empty_name.email,
                'name': empty_name.name,
            })
        )),
        reason="There is subscription with empty name in the list"
    )


@pytest.mark.creating
@pytest.mark.negative
def test_creating_with_empty_time(clean):
    """
    Try to create subscription with empty time
    """

    response = create_subscription(empty_time)

    hc.assert_that(
        actual=response,
        matcher=hc.has_entries({
            "error": hc.all_of(
                hc.contains_string("ValidationError"),
                hc.matches_regexp(r"Invalid.*time")
            )
        }),
        reason="ValidationError was expected"
    )

    hc.assert_that(
        actual=send_request(),
        matcher=hc.not_(hc.has_item(
            hc.has_entries({
                'email': empty_time.email,
                'name': empty_time.name,
            })
        )),
        reason="There is subscription with empty time in the list"
    )


@pytest.mark.creating
@pytest.mark.negative
def test_creating_with_incorrect_email(clean):
    """
    Try to create subscription with incorrect email
    """

    response = create_subscription(incorrect_email)

    hc.assert_that(
        actual=response,
        matcher=hc.has_entries({
            "error": hc.all_of(
                hc.contains_string("ValidationError"),
                hc.matches_regexp(r"Invalid.*email")
            )
        }),
        reason="ValidationError was expected"
    )

    hc.assert_that(
        actual=send_request(),
        matcher=hc.not_(hc.has_item(
            hc.has_entries({
                'email': incorrect_email.email,
                'name': incorrect_email.name,
            })
        )),
        reason="There is subscription with incorrect email in the list"
    )


@pytest.mark.creating
@pytest.mark.negative
def test_creating_with_incorrect_name(clean):
    """
    Try to create subscription with incorrect name
    """

    response = create_subscription(incorrect_name)

    hc.assert_that(
        actual=response,
        matcher=hc.has_entries({
            "error": hc.all_of(
                hc.contains_string("ValidationError"),
                hc.matches_regexp(r"Invalid.*name")
            )
        }),
        reason="ValidationError was expected"
    )

    hc.assert_that(
        actual=send_request(),
        matcher=hc.not_(hc.has_item(
            hc.has_entries({
                'email': incorrect_name.email,
                'name': incorrect_name.name,
            })
        )),
        reason="There is subscription with incorrect name in the list"
    )


@pytest.mark.creating
@pytest.mark.negative
def test_creating_with_incorrect_time(clean):
    """
    Try to create subscription with incorrect time
    """

    response = create_subscription(incorrect_time)

    hc.assert_that(
        actual=response,
        matcher=hc.has_entries({
            "error": hc.all_of(
                hc.contains_string("ValidationError"),
                hc.matches_regexp(r"Invalid.*time")
            )
        }),
        reason="ValidationError was expected"
    )

    hc.assert_that(
        actual=send_request(),
        matcher=hc.not_(hc.has_item(
            hc.has_entries({
                'email': incorrect_time.email,
                'name': incorrect_time.name,
            })
        )),
        reason="There is subscription with incorrect time in the list"
    )


@pytest.mark.creating
@pytest.mark.negative
def test_creating_with_zero_time(clean):
    """
    Creating with zero time
    """

    response = create_subscription(zero_time)

    hc.assert_that(
        actual=response,
        matcher=hc.has_entries({
            "error": hc.all_of(
                hc.contains_string("ValidationError"),
                hc.matches_regexp(r"Invalid.*time")
            )
        }),
        reason="ValidationError was expected"
    )

    hc.assert_that(
        actual=send_request(),
        matcher=hc.not_(hc.has_item(
            hc.has_entries({
                'email': zero_time.email,
                'name': zero_time.name,
            })
        )),
        reason="There is subscription with zero time in the list"
    )
