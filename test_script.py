from datetime import datetime
from script import calculate_landing_time, format_date


def test_format_date():
    assert format_date(1514665153, "%d-%m-%Y") == '31-12-2017'


def test_calculate_landing_time():
    assert calculate_landing_time(datetime(2023, 2, 15), 20) == '07-03-2023'
