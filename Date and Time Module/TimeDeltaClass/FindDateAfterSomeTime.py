from datetime import datetime, timedelta  # Import necessary modules

# Create a timedelta object representing a duration
duration = timedelta(days=10, hours=2, minutes=30)  # Create a timedelta object with specified duration

# Create a datetime object representing the start time
start_time = datetime(2022, 3, 8, 10, 30)  # Create a datetime object for the start time

# Calculate the end time by adding the duration to the start time
end_time = start_time + duration  # Add the duration to the start time to get the end time

# Print the start and end times in a formatted way
print(f"Start time: {start_time}")  # Print the start time
print(f"End time after {duration}: {end_time}")  # Print the end time and the duration
