import datetime


def demonstrate_date_class():
    """Demonstrates the use of various attributes and methods of the date class."""

    # Create a date object for today
    today = datetime.date.today()

    # Print various attributes
    print("Year:", today.year)
    print("Month:", today.month)
    print("Day:", today.day)

    # Use methods
    print("ctime:", today.ctime())
    print("ISO format:", today.isoformat())
    print("Weekday (0-6):", today.weekday())

    # Get ISO calendar data using isocalendar() function
    iso_year, iso_week, iso_weekday = datetime.date.isocalendar(today)
    print("ISO calendar:", iso_year, iso_week, iso_weekday)

    # ... (rest of your code demonstrating other methods)


if __name__ == "__main__":
    demonstrate_date_class()
