# Import the UserString class from the userstring module
from userstring import UserString

# Create an instance of UserString with an initial string
my_string = UserString("Hello, World!")

# Display the original string
print("Original string:", my_string)

# Convert the string to uppercase
upper_string = my_string.upper()
print("Uppercase string:", upper_string)

# Convert the string to lowercase
lower_string = my_string.lower()
print("Lowercase string:", lower_string)

# Capitalize the first letter of the string
capitalized_string = my_string.capitalize()
print("Capitalized string:", capitalized_string)

# Title case the string (capitalize the first letter of each word)
title_string = my_string.title()
print("Title case string:", title_string)

# Swap the case of each character in the string
swapcase_string = my_string.swapcase()
print("Swapcase string:", swapcase_string)

# Check if the string starts with 'Hello'
starts_with_hello = my_string.startswith("Hello")
print("Starts with 'Hello':", starts_with_hello)

# Check if the string ends with 'World!'
ends_with_world = my_string.endswith("World!")
print("Ends with 'World!':", ends_with_world)

# Find the index of the first occurrence of 'World'
index_of_world = my_string.find("World")
print("Index of 'World':", index_of_world)

# Replace 'World' with 'Universe'
replaced_string = my_string.replace("World", "Universe")
print("Replaced string:", replaced_string)

# Split the string by comma
split_string = my_string.split(", ")
print("Split string:", split_string)

# Join the split string with a hyphen
joined_string = "-".join(split_string)
print("Joined string:", joined_string)

# Strip whitespace from the beginning and end of the string
whitespace_string = UserString("   Leading and trailing spaces   ")
stripped_string = whitespace_string.strip()
print("Stripped string:", stripped_string)

# Check if the string is alphanumeric (contains only letters and numbers)
alphanumeric_check = my_string.isalnum()
print("Is alphanumeric:", alphanumeric_check)

# Check if the string is alphabetic (contains only letters)
alphabetic_check = my_string.isalpha()
print("Is alphabetic:", alphabetic_check)

# Check if the string is numeric (contains only numbers)
numeric_check = my_string.isdigit()
print("Is digit:", numeric_check)

# Check if the string is in title case
title_case_check = my_string.istitle()
print("Is title case:", title_case_check)

# Check if the string is in uppercase
uppercase_check = my_string.isupper()
print("Is uppercase:", uppercase_check)

# Check if the string is in lowercase
lowercase_check = my_string.islower()
print("Is lowercase:", lowercase_check)



#Explanation:
# UserString Creation: We create an instance of UserString with the initial string "Hello, World!".

# String Transformations:

# upper(): Converts all characters to uppercase.
# lower(): Converts all characters to lowercase.
# capitalize(): Capitalizes the first character of the string.
# title(): Capitalizes the first letter of each word.
# swapcase(): Swaps the case of each character.
# String Checks:

# startswith(): Checks if the string starts with a specified substring.
# endswith(): Checks if the string ends with a specified substring.
# String Manipulations:

# find(): Finds the index of the first occurrence of a specified substring.
# replace(): Replaces occurrences of a specified substring with another substring.
# split(): Splits the string into a list of substrings based on a delimiter.
# join(): Joins a list of substrings into a single string with a specified delimiter.
# Whitespace Management:

# strip(): Removes leading and trailing whitespace from the string.
# String Characteristics:

# isalnum(): Checks if all characters in the string are alphanumeric.
# isalpha(): Checks if all characters in the string are alphabetic.
# isdigit(): Checks if all characters in the string are digits.
# istitle(): Checks if the string is in title case.
# isupper(): Checks if the string is in uppercase.
# islower(): Checks if the string is in lowercase.