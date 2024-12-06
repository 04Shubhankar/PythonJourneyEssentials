import time  # Import the 'time' module for working with time-related functions

current_time = time.localtime()  # Get the current local time as a struct_time object

time_string = time.strftime("%Y-%m-%d %H:%M:%S", current_time)  # Format the current time as a string using strftime()

print("The current date and time is:", time_string)  # Print the formatted time string
