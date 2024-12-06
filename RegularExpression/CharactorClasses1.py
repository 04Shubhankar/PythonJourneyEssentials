import re

word = "Study 7 hours to get job@Google"  # Define a string to be searched

pattern = r'\S'  # Create a regular expression pattern using a raw string

result = re.finditer(pattern, word)  # Find all non-overlapping occurrences

for i in result:
    print(i.start(), "=>", i.group())  # Print the start index and the matched character
"""
Explanation:

import re: Imports the re module, which provides functions for working with regular expressions in Python.
word = "Study 7 hours to get job@Google": Defines a string named word containing the text to be searched.
pattern = r'\S': Creates a regular expression pattern to match any non-whitespace character. The \S is a special character class representing non-whitespace characters.
result = re.finditer(pattern, word): Uses the re.finditer() function to find all non-overlapping occurrences of the pattern within the word string and returns an iterator of match objects.
for i in result:: Iterates over each match object in the result iterator.
print(i.start(), "=>", i.group()): Prints the start index of the match within the original string using i.start() and the matched character using i.group().

"""
