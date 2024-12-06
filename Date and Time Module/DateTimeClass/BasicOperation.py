import datetime

# Get the current datetime
now = datetime.datetime.now()

# Extract and print components
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Microsecond:", now.microsecond)
print("Time zone info:", now.tzinfo)
