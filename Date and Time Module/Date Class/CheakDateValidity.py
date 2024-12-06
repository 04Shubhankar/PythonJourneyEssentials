from datetime import date  # Import the 'date' class from the 'datetime' module

def is_valid_date(year, month, day):  # Define a function to check if a date is valid
    """Checks if a given year, month, and day form a valid date.

    Args:
        year: The year.
        month: The month (1-12).
        day: The day of the month.

    Returns:
        True if the date is valid, False otherwise.
    """

    try:
        date(year, month, day)  # Attempt to create a date object
        return True  # If successful, the date is valid
    except ValueError:  # If an error occurs, the date is invalid
        return False

year = 2022  # Set the year
month = 2  # Set the month
day = 31  # Set the day

is_valid = is_valid_date(year, month, day)  # Check if the date is valid

if is_valid:  # If the date is valid
    print("The date", date(year, month, day), "is valid.")  # Print a success message
else:  # If the date is invalid
    print("The date", date(year, month, day), "is invalid.")  # Print an error message
