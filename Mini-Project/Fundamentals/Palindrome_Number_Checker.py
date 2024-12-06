# This code checks if a given number is a palindrome.

# Get the number from the user
n = int(input("Enter number: "))

# Store the original number for comparison later
temp = n

# Initialize the reversed number to 0
rev = 0

# Reverse the number
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n //= 10

# Check if the reversed number is equal to the original number
if temp == rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
