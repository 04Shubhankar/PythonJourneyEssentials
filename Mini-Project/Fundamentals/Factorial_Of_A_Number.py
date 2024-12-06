# This code calculates the factorial of a given number.

num = int(input("Enter a number to get its factorial: "))

# Initialize the factorial variable to 1
fact = 1

# Check if the number is 0
if num == 0:
    print("Factorial of 0 is 1")

# Check if the number is negative
elif num < 0:
    print("Factorial does not exist for negative numbers")

# Calculate the factorial for positive numbers
else:
    for i in range(1, num + 1):
        fact *= i
    print("Factorial of", num, "is", fact)
