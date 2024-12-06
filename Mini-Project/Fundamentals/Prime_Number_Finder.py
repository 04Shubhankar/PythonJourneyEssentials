# This code finds prime numbers within a specified range.

# Get the starting and ending ranges from the user
start_range = int(input("Enter starting range: "))
end_range = int(input("Enter ending range: "))

# Print a message indicating the range
print("All prime numbers between given range are:")

# Iterate through the numbers in the specified range
for num in range(start_range, end_range):
    # Check if the number is greater than 1
    if num > 1:
        # Iterate through potential divisors from 2 to num-1
        for i in range(2, num):
            # If the number is divisible by any divisor, it's not prime
            if (num % i == 0):
                break
        else:
            # If the loop completes without breaking, the number is prime
            print(num)
