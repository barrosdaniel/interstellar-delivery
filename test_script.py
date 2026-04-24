from script import format_date


def test_format_date():
    timestamp = 1514665153
    datetime_format = "%d-%m-%Y"
    # Depending on the timezone, the output may vary
    expected_output = '31-12-2017'
    assert format_date(timestamp, datetime_format) == expected_output
