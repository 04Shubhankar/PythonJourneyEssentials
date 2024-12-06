def get_days_in_month(year, month):
    """Calculates the number of days in a given month and year.

    Args:
        year: The year.
        month: The month (1-12).

    Returns:
        The number of days in the specified month.
    """

    # A list to store the number of days in each month
    days_in_month = [31, 28 + (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #days_in_month = [31, 28 + (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] creates a list to store the number of days in each month. The second element calculates the number of days in February, considering leap years.
    # Return the number of days for the specified month
    return days_in_month[month - 1]

# Example usage:
year = 2022
month = 2

# Calculate the number of days in the specified month
days_in_month = get_days_in_month(year, month)

# Print the result
print("There are", days_in_month, "days in", month, "/", year)
