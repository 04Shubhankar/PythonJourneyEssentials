# This code defines a recursive function to calculate the factorial of a given number.

def factorial(num):
    """Calculates the factorial of a given number recursively.

    Args:
        num: The number for which the factorial is to be calculated.

    Returns:
        The factorial of the given number.
    """

    if num == 1:
        # Base case: The factorial of 1 is 1
        return 1
    else:
        # Recursive case: Factorial of n is n * factorial(n-1)
        return num * factorial(num - 1)

# Get the number from the user
num = int(input("Enter a number to get its factorial: "))

# Check if the number is 0 or negative
if num == 0:
    print("Factorial of 0 is 1")
elif num < 0:
    print("Factorial does not exist for negative numbers")

# Calculate and print the factorial using the recursive function
else:
    print("Factorial of", num, "is", factorial(num))
