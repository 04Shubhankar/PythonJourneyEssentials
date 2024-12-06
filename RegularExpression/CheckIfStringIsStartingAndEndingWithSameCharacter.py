import re

def check_start_end_same(string):
  """Checks if a string starts and ends with the same character."""
  pattern = r"^(.)(.*)\1$"
  match = re.match(pattern, string)
  return bool(match)

# Test cases
strings = ["hello", "level", "radar", "world", "12321"]

for string in strings:
  if check_start_end_same(string):
    print(f"{string} starts and ends with the same character.")
  else:
    print(f"{string} does not start and end with the same character.")



"""
Explanation:
Import the re module: This line imports the re module for regular expressions.
Define the check_start_end_same function: This function takes a string as input and checks if it starts and ends with the same character.
Create a regular expression pattern: The pattern r"^(.)(.*)\1$" breaks down as follows:
^: Matches the beginning of the string.
(.): Matches any single character and captures it in group 1.
(.*): Matches any number of characters (non-greedy).
\1: Matches the same text as most recently captured group (i.e., the first character).
$: Matches the end of the string.
Match the pattern: The re.match function is used to check if the entire string matches the pattern.
Return the result: The function returns True if the match is successful, indicating that the string starts and ends with the same character, otherwise False.
Test cases: A list of strings is created to test the function.
Iterate and print results: The for loop iterates over each string, calls the check_start_end_same function, and prints the corresponding message.

"""
