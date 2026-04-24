from datetime import datetime, timedelta


def format_date(timestamp: int, datetime_format: str) -> str:
    """Formats a timestamp into a human-readable date string.

    Args:
        timestamp (int): The timestamp to format.
        datetime_format (str): The format string to use for formatting the date.

    Returns:
        str: The formatted date string.

    Example:
        >>> format_date(1514665153, "%d-%m-%Y")
        '30-12-2017'
    """
    return datetime.fromtimestamp(timestamp).strftime(datetime_format)


def calculate_landing_time(rocket_launch_dt: datetime, travel_duration: int) -> str:
    """Calculates the landing time of a rocket based on its launch date and travel duration.

    Args:
        rocket_launch_dt (datetime): The launch date and time of the rocket.
        travel_duration (int): The duration of the rocket's travel in days.

    Returns:
        str: The landing date in the format "dd-mm-yyyy".

    Example:
        >>> calculate_landing_time(datetime(2023, 2, 15), 20)
        '07-03-2023'
    """
    days: timedelta = timedelta(days=travel_duration)
    arrival: datetime = rocket_launch_dt + days
    return arrival.strftime("%d-%m-%Y")


def days_until_delivery(expected_delivery_dt: datetime, current_dt: datetime):
    """Calculates the number of days until the expected delivery date.

    Args:
        expected_delivery_dt (datetime): The expected delivery date.
        current_dt (datetime): The current date.

    Returns:
        int: The number of days until delivery. If the expected delivery date has already passed,
            this function will return a negative number.

    Example:
        >>> days_until_delivery(datetime(2023, 2, 15), datetime(2023, 2, 5))
        10
    """
    time_remaining: timedelta = expected_delivery_dt - current_dt
    return time_remaining.days
