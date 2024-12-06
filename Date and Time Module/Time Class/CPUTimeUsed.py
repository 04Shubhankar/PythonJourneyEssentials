import time  # Import the 'time' module for accessing time-related functions

start_time = time.process_time()  # Record the start time of the process
end_time = time.process_time()  # Record the end time of the process

cpu_time = end_time - start_time  # Calculate the elapsed CPU time

print("CPU time used:", cpu_time, "seconds")  # Print the calculated CPU time in seconds
