import datetime  # Import the datetime module

# Create a date string in YYYY-MM-DD format
date_string = "2023-03-07"

# Convert the date string to a datetime object using strptime()
dt = datetime.datetime.strptime(date_string, "%Y-%m-%d")

# Convert the datetime object back to a string using strftime()
str_dt = dt.strftime("%Y-%m-%d")

# Print the resulting string
print(str_dt)
