from unittest import mock
from unittest.mock import MagicMock

import pytest

from datetime import date

from app.main import outdated_products


@pytest.fixture()
def products_template() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.fixture()
def mocked_datetime() -> None:
    with mock.patch("app.main.datetime.date") as mock_today_date:
        yield mock_today_date.today


def test_should_return_empty_list(
        mocked_datetime: MagicMock,
        products_template: MagicMock
) -> None:
    mocked_datetime.return_value = date(2022, 2, 1)
    assert outdated_products(products_template) == []


def test_should_return_all_products(
        mocked_datetime: MagicMock,
        products_template: MagicMock
) -> None:
    mocked_datetime.return_value = date(2022, 2, 11)
    assert (outdated_products(products_template)
            == ["salmon", "chicken", "duck"])


def test_should_return_only_duck(
        mocked_datetime: MagicMock,
        products_template: MagicMock
) -> None:
    mocked_datetime.return_value = date(2022, 2, 2)
    assert outdated_products(products_template) == ["duck"]
