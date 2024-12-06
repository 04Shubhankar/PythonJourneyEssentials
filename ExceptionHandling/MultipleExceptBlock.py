try:  # Start a try block to handle potential exceptions
    x = int(input("Enter number 1: "))  # Take the first number as input and convert it to an integer
    y = int(input("Enter number 2: "))  # Take the second number as input and convert it to an integer
    print(x / y)  # Divide x by y and print the result
except ZeroDivisionError:  # Handle the specific case of division by zero
    print("Can't Divide by zero")
except ValueError:  # Handle the case where the input is not a valid integer
    print("Provide valid int value")
except:  # Handle any other unexpected errors
    print("Unknown error occurred")


"""

Explanation:

try:: This line starts a try block, which is used to enclose code that might raise an exception.
x = int(input("Enter number 1: ")): This line takes the first number as input from the user and converts it to an integer using the int() function.
y = int(input("Enter number 2: ")): This line takes the second number as input from the user and converts it to an integer using the int() function.
print(x / y): This line divides the value of x by the value of y and prints the result.
except ZeroDivisionError:: This line starts an except block that handles the specific exception ZeroDivisionError, which occurs when dividing by zero. If this exception is raised, the code inside this block will be executed.
print("Can't Divide by zero"): This line prints an error message indicating that division by zero is not allowed.
except ValueError:: This line starts another except block that handles the specific exception ValueError, which occurs when the input cannot be converted to an integer. If this exception is raised, the code inside this block will be executed.
print("Provide valid int value"): This line prints an error message indicating that the user should provide a valid integer value.
except:: This line starts a general except block that handles any other exceptions that might occur. It's generally recommended to avoid using a bare except like this, as it can hide unexpected errors.
print("Unknown error occurred"): This line prints a generic error message indicating that an unknown error has occurred.
"""
