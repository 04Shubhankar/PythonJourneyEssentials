class MyCustomException(Exception):
    """A custom exception class."""

    def __init__(self, message):
        """
        Constructor for the custom exception.

        Args:
            message: The error message to be displayed.
        """
        self.message = message

def my_custom_function():
    """Raises a custom exception."""
    print("Something went wrong.")
    raise MyCustomException("This is my custom exception message")

try:
    my_custom_function()
except MyCustomException as e:
    print("Caught a custom exception:", e)
