try:
    # Start of the try block: This block contains code that might raise an exception.
    print("Statement 1")  # Prints "Statement 1"

except ValueError:
    # Handles the ValueError exception if it occurs within the try block.
    print("except block")  # Prints "except block"

finally:
    # Always executed, regardless of whether an exception occurs or not.
    print("finally")  # Prints "finally"
    print("Statement 2")  # Prints "Statement 2"
