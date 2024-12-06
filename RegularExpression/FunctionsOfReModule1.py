import re  # Import the regular expression module

word = "Study Smart @25"  # Define the string to be searched

pattern = r'\w+'  # Create a regular expression pattern to match one or more word characters

result = re.finditer(pattern, word)  # Find all non-overlapping occurrences of the pattern in the string

print(result)  # Print the iterator of match objects

for i in result:  # Iterate over each match object
    print(i.start(), "-", i.end(), "-", i.group())  # Print the start index, end index, and matched substring
