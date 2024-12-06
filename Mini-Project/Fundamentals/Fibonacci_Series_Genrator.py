# This code defines a recursive function to calculate Fibonacci numbers and then prints the sequence up to a specified range.

def fibonacci(num):
    """Calculates the nth Fibonacci number recursively.

    Args:
        num: The index of the Fibonacci number to be calculated.

    Returns:
        The nth Fibonacci number.
    """

    if num == 0:
        # Base case: The 0th Fibonacci number is 0
        return 0
    elif num == 1:
        # Base case: The 1st Fibonacci number is 1
        return 1
    else:
        # Recursive case: The nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers
        return fibonacci(num - 2) + fibonacci(num - 1)

# Get the range from the user
num = int(input("Enter range: "))

# Print the Fibonacci sequence up to the specified range
for i in range(0, num):
    print(fibonacci(i))
