# This code implements a simple calculator that performs addition, subtraction, multiplication, and division.

def add(S, R):
    """Adds two numbers.

    Args:
        S: The first number.
        R: The second number.

    Returns:
        The sum of the two numbers.
    """
    return S + R

def subtract(S, R):
    """Subtracts the second number from the first.

    Args:
        S: The first number.
        R: The second number.

    Returns:
        The difference of the two numbers.
    """
    return S - R

def multiply(S, R):
    """Multiplies two numbers.

    Args:
        S: The first number.
        R: The second number.

    Returns:
        The product of the two numbers.
    """
    return S * R

def division(S, R):
    """Divides the first number by the second.

    Args:
        S: The first number (dividend).
        R: The second number (divisor).

    Returns:
        The quotient of the division.
    """
    return S / R

# Print the available operations
print("Please select the operation:")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

# Get the user's choice
choice = input("Please enter the choice (a/b/c/d): ")

# Get the numbers from the user
num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

# Perform the selected operation and print the result
if choice == 'a':
    result = add(num_1, num_2)
    print("The sum is:", result)
elif choice == 'b':
    result = subtract(num_1, num_2)
    print("The difference is:", result)
elif choice == 'c':
    result = multiply(num_1, num_2)
    print("The product is:", result)
elif choice == 'd':
    result = division(num_1, num_2)
    print("The quotient is:", result)
else:
    print("Invalid choice. Please enter a valid choice (a/b/c/d).")
