try:
    print("Outer try block")  # Start of the outer try block
    print(10 / 0)  # This line will raise a ZeroDivisionError

    try:
        print("Inner try block")  # Start of the inner try block
    except ZeroDivisionError:
        print("Inner except block")  # Handles ZeroDivisionError if raised in the inner try block
    finally:
        print("Inner finally block")  # Always executed after the inner try or except block

except:  # Handles any exception that is not caught by the inner try block
    print("Outer except block")

finally:
    print("Outer finally block")  # Always executed after the outer try or except block


"""
Explanation:

The code demonstrates nested try-except-finally blocks.
The outer try block contains code that might raise a ZeroDivisionError.
An inner try block is placed within the outer try block for more specific exception handling.
The except block within the inner try block catches a ZeroDivisionError if it occurs in the inner block.
The finally block within the inner try block is always executed, regardless of whether an exception occurs or not.
The outer except block catches any exception that is not handled by the inner try block.
The outer finally block is always executed, regardless of whether an exception occurs in the outer try block.
Note: In this example, the ZeroDivisionError is raised in the outer try block, so the inner try and except blocks are not executed. The outer except block will handle the exception.

"""
