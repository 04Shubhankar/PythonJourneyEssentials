import datetime
from datetime import timezone

# Get the current datetime in UTC
now = datetime.datetime.now(timezone.utc)  # Get current datetime in UTC timezone

# Convert to local time
local_time = now.astimezone()  # Convert the UTC datetime to local time

# Format the datetime as a string
formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S")  # Format datetime as a string for better readability

# Print the formatted datetime
print("Formatted datetime:", formatted_time)

# Extract and print year, month, and day
print("Year:", local_time.year)  # Extract and print the year
print("Month:", local_time.month)  # Extract and print the month
print("Day:", local_time.day)  # Extract and print the day

# Extract and print time components
print("Hour:", local_time.hour)  # Extract and print the hour
print("Minute:", local_time.minute)  # Extract and print the minute
print("Second:", local_time.second)  # Extract and print the second
print("Microsecond:", local_time.microsecond)  # Extract and print the microsecond

# Create a new datetime by combining date and time
combined_datetime = datetime.datetime.combine(local_time.date(), local_time.time())  # Combine date and time into a new datetime object

# Print the combined datetime
print("Combined datetime:", combined_datetime)

# Convert datetime to timestamp
timestamp = combined_datetime.timestamp()  # Convert datetime to a timestamp (seconds since epoch)
print("Timestamp:", timestamp)

# Create datetime from timestamp
from_timestamp = datetime.datetime.fromtimestamp(timestamp)  # Create a datetime object from a timestamp
print("From timestamp:", from_timestamp)

# Get the day of the week (0-6, Monday is 0)
weekday = local_time.weekday()  # Get the day of the week as an integer
print("Weekday:", weekday)

# Get ISO calendar information (year, week number, weekday)
iso_calendar = local_time.isocalendar()  # Get ISO calendar information as a tuple
print("ISO calendar:", iso_calendar)

# Get the ordinal representation of the date (number of days since January 1, 1)
ordinal = local_time.toordinal()  # Get the ordinal representation of the date
print("Ordinal:", ordinal)

# Get time zone information
tzname = local_time.tzname()  # Get the time zone name
print("Time zone name:", tzname)
utc_offset = local_time.utcoffset()  # Get the UTC offset as a timedelta object
print("UTC offset:", utc_offset)
