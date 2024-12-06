try:  # Begin a try block to handle potential exceptions
    x = int(input("Enter number 1: "))  # Take the first number as input and convert it to an integer
    y = int(input("Enter number 2: "))  # Take the second number as input and convert it to an integer
    print(x / y)  # Divide x by y and print the result
except (ZeroDivisionError, ValueError) as msg:  # Handle ZeroDivisionError and ValueError exceptions, capturing the exception object as 'msg'
    print("Provide valid input only and Error is:", msg)  # Print an error message indicating invalid input and the specific error
except:  # Handle any other unexpected exceptions (not recommended for general use)
    print("Unknown error occurred")  # Print a generic error message for unknown exceptions
