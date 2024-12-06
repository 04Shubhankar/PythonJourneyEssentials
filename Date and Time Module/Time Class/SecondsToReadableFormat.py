import time  # Import the 'time' module for working with time-related functions

seconds = 7200  # Define the total number of seconds as 7200

hours = seconds // 3600  # Calculate the number of hours by dividing seconds by 3600 and using integer division (//)

minutes = (seconds % 3600) // 60  # Calculate the number of minutes by taking the remainder of seconds divided by 3600, then dividing by 60

seconds = seconds % 60  # Calculate the remaining seconds by taking the remainder of seconds divided by 60

print(f"{hours} hours, {minutes} minutes, {seconds} seconds")  # Print the formatted output with hours, minutes, and seconds
