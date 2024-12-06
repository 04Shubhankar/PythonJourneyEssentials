from datetime import time

# Create a time object
time_obj = time(hour=12, minute=30, second=45, microsecond=123456)

# Access individual components
print("Hour:", time_obj.hour)  # Access the hour component
print("Minute:", time_obj.minute)  # Access the minute component
print("Second:", time_obj.second)  # Access the second component
print("Microsecond:", time_obj.microsecond)  # Access the microsecond component

# Create a new time object with modified components
new_time_obj = time_obj.replace(minute=45, second=0)  # Create a new time object with minute set to 45 and second to 0

# Print the new time object
print("New time:", new_time_obj)
