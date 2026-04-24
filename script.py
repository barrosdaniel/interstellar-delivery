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


def main() -> None:
    if __name__ == "__main__":
        timestamp = 1514665153
        datetime_format = "%d-%m-%Y"
        print('Testing start')
        print(format_date(timestamp, datetime_format))
        print('Testing end')


main()
