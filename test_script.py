from datetime import datetime
from script import (
    calculate_landing_time,
    days_until_delivery,
    format_date
)


def test_format_date():
    assert format_date(1514665153, "%d-%m-%Y") == '31-12-2017'


def test_calculate_landing_time():
    assert calculate_landing_time(datetime(2023, 2, 15), 20) == '07-03-2023'


def test_days_until_delivery():
    assert days_until_delivery(
        datetime(2023, 2, 15), datetime(2023, 2, 5)) == 10
