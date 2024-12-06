import datetime  # Import the datetime module for working with dates and times

date = datetime.date(2022, 10, 1)  # Create a date object for October 1, 2022

print("The date is:", date.strftime("%A, %B %d, %Y"))  # Format and print the date as "Weekday, Month Day, Year"


"""
%A %b %d %Y is a format specifier used in Python's strftime() method to format a date object as a string. Here's what each component represents:

%A: Full weekday name (e.g., Monday, Tuesday, Wednesday)
%b: Abbreviated month name (e.g., Jan, Feb, Mar)
%d: Day of the month with leading zero (e.g., 01, 02, 31)
%Y: Four-digit year (e.g., 2023, 2024)
"""
