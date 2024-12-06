def divide(x, y):  # Defines a function named 'divide' that takes two arguments, x and y
    try:  # Starts a try block to handle potential exceptions
        result = x / y  # Divides x by y and stores the result in the 'result' variable
        print("Your result is:", result)  # Prints the calculated result
    except:  # Handles any exception that might occur in the try block
        print("Don't divide by zero")  # Prints an error message if the exception is a division by zero

x = int(input("Enter number 1: "))  # Takes the first number as input and converts it to an integer
y = int(input("Enter number 2: "))  # Takes the second number as input and converts it to an integer

divide(x, y)  # Calls the 'divide' function with the input values x and y
