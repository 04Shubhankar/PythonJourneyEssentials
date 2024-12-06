from datetime import date, timedelta

# Create a start date
start_date = date(2022, 1, 1)  # Create a date object for January 1, 2022

# Specify the number of days to add
days_to_add = 30

# Calculate the end date by adding days to the start date
end_date = start_date + timedelta(days=days_to_add)

# Print the end date
print("The end date is:", end_date)

# Specify the number of days to subtract
days_to_subtract = 15

# Calculate a new date by subtracting days from the end date
new_date = end_date - timedelta(days=days_to_subtract)

# Print the new date
print("The new date is:", new_date)
