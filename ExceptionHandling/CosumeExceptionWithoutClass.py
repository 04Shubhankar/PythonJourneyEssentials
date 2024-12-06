def my_custom_exception():
    # Defines a function named 'my_custom_exception'
    print("Something went wrong.")  # Prints a message indicating an error

    # Raises a generic Exception with a custom message
    raise Exception("This is my custom exception message.")

try:
    # Starts a try block to handle potential exceptions
    my_custom_exception()  # Calls the custom exception function

except Exception as e:
    # Handles any exception that might occur within the try block
    # The exception object is assigned to the variable 'e'
    print("Exception caught:", e)  # Prints an error message along with the exception object
