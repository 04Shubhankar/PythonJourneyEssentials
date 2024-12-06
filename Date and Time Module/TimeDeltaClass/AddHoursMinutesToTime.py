from datetime import *

# Create a time object
t = time(12, 30)  # Create a time object representing 12:30

# Create a timedelta object representing 2 hours and 15 minutes
delta = timedelta(hours=2, minutes=15)  # Create a timedelta object for 2 hours and 15 minutes

# Combine the time object with a dummy date and add the timedelta
new_t = (datetime.combine(datetime.min, t) + delta).time()  # Combine time with a dummy date, add timedelta, and extract time

# Print the original time and the new time after adding the timedelta
print(f"Original time: {t}")
print(f"New time after adding {delta}: {new_t}")
