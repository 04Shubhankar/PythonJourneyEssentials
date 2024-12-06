print("Statement 1")  # Prints the string "Statement 1" to the console

try:
    print(10/0)  # This line will cause a ZeroDivisionError because division by zero is not allowed
except ZeroDivisionError:
    print("Dont divide by Zero")  # This line will be executed if a ZeroDivisionError occurs
"""
Explanation:

The first line prints the string "Statement 1" to the console.
The try block starts a block of code where potential errors can be handled.
Inside the try block, print(10/0) attempts to print the result of dividing 10 by 0, which will always raise a ZeroDivisionError.
Since an error occurred, the code jumps to the except ZeroDivisionError: block.
The except ZeroDivisionError: block specifically catches a ZeroDivisionError and prints the string "Dont divide by Zero" to the console.
The code will output:
Statement 1
Dont divide by Zero
"""
