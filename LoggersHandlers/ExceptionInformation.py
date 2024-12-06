import logging  # Import the logging module

logging.basicConfig(level=logging.INFO)  # Configure basic logging setup with INFO level

logging.info("A new request came:")  # Log an info message indicating a new request

try:
    x = int(input("Enter First number:"))  # Prompt user for the first number and convert it to an integer
    y = int(input("Enter second number:"))  # Prompt user for the second number and convert it to an integer

    print(x / y)  # Perform division and print the result

except ZeroDivisionError as msg:  # Handle ZeroDivisionError exception
    print("Cannot divide with zero")  # Print an error message
    logging.exception(msg)  # Log the exception with traceback

except ValueError as msg:  # Handle ValueError exception (invalid input)
    print("Enter only int values")  # Print an error message
    logging.exception(msg)  # Log the exception with traceback

logging.info("Request processing completed")  # Log an info message indicating request completion
