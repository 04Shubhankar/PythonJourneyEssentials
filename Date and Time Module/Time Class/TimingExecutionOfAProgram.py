import time  # Import the 'time' module for accessing time-related functions

start_time = time.time()  # Record the starting time using the time.time() function, which returns the current time in seconds since the epoch

end_time = time.time()  # Record the ending time using the same time.time() function

elapsed_time = end_time - start_time  # Calculate the elapsed time by subtracting the start time from the end time

print("Elapsed time:", elapsed_time, "seconds")  # Print the calculated elapsed time in seconds
