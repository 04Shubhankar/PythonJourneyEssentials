print("Statements 1")  # Prints the string "Statements 1" to the console

try:
    print(20/0)  # This line will cause a ZeroDivisionError because division by zero is not allowed
except:
    print("Statements 2")  # This line will not be executed because an error occurred in the try block

# The code will output:
# Statements 1
# ZeroDivisionError: division by zero
