import datetime

# Create two datetime objects
date1 = datetime.datetime(2023, 3, 7)
date2 = datetime.datetime(2023, 3, 14)

# Calculate the difference between the dates
delta = date2 - date1

# Print the number of days between the dates
print("Difference in days:", delta.days)

# Adding a timedelta to a date
new_date = date1 + datetime.timedelta(days=5)
print("New date:", new_date)

# Subtracting a timedelta from a date
previous_date = date2 - datetime.timedelta(weeks=1)
print("Previous date:", previous_date)

# Comparing dates
if date1 < date2:
    print("date1 is earlier than date2")
else:
    print("date1 is later than or equal to date2")
