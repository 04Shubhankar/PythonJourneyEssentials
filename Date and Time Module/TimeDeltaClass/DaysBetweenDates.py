from datetime import date, timedelta  # Import necessary modules

# Create two date objects
date1 = date(2023, 3, 1)  # Create a date object for March 1, 2023
date2 = date(2022, 3, 10)  # Create a date object for March 10, 2022

# Calculate the difference between the dates
difference = date1 - date2  # Calculate the difference between the two dates as a timedelta object

# Extract the number of days from the difference
days_between = difference.days  # Extract the number of days from the timedelta object

# Print the dates and the number of days between them
print(f"Date1: {date1}")  # Print the first date
print(f"Date2: {date2}")  # Print the second date
print(f"Number of days between date1 and date2: {days_between}")  # Print the number of days between the dates
