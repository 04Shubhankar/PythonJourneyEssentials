# This code checks if a given number is an Armstrong number.

# Get the number from the user
num = int(input("Enter any number: "))

# Store the original number for comparison later
s = num

# Initialize the sum to 0
sum = 0

# Loop until the number becomes 0
while num != 0:
    # Extract the last digit
    rem = num % 10

    # Add the cube of the last digit to the sum
    sum += (rem * rem * rem)

    # Remove the last digit from the number
    num //= 10

# Check if the sum of cubes of digits is equal to the original number
if s == sum:
    print("Given number is an Armstrong number")
else:
    print("Number is not an Armstrong number")
