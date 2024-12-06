import datetime  # Import the 'datetime' module for date and time manipulation

# Get the current date and time as a datetime object
now = datetime.datetime.now()

# Extract the year from the datetime object
year = now.year

# Extract the month from the datetime object
month = now.month

# Extract the day from the datetime object
day = now.day

# Extract the hour from the datetime object
hour = now.hour

# Extract the minute from the datetime object
minute = now.minute

# Extract the second from the datetime object
second = now.second

# Get the weekday (0-6, Monday is 0)
weekday = now.weekday()

# Format the datetime object as a string in YYYY-MM-DD HH:MM:SS format
str_now = now.strftime("%Y-%m-%d %H:%M:%S")

# Print the formatted datetime string with a descriptive label
print("Current Date and Time:", str_now)

# Print the extracted year with a label
print("Year:", year)

# Print the extracted month with a label
print("Month:", month)

# Print the extracted day with a label
print("Day:", day)

# Print the extracted hour with a label
print("Hour:", hour)

# Print the extracted minute with a label
print("Minute:", minute)

# Print the extracted second with a label
print("Second:", second)

# Print the weekday (0-6, Monday is 0) with a label and clarification
print("Weekday (0-6, Monday is 0):", weekday)
