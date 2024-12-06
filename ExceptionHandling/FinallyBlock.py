try:  # Begin a try block to handle potential exceptions
    print(10/0)  # This line will cause a ZeroDivisionError
except:  # Handles any exception that might occur in the try block
    print("Except")  # Prints "Except" if an exception occurs
finally:  # This block always executes, regardless of whether an exception occurs or not
    print("Finally")  # Prints "Finally"
