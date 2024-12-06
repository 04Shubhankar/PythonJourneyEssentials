import re  # Import the regular expression module

word = "aabbccABcaDe"  # Define the string to be searched

# Match one or more 'a' characters
pattern1 = 'a+'
result1 = re.findall(pattern1, word)

# Match zero or more 'a' characters (including empty strings)
pattern2 = 'a*'
result2 = re.findall(pattern2, word)

# Match zero or one 'a' character
pattern3 = 'a?'
result3 = re.findall(pattern3, word)

# Print the results of each pattern
print(result1)
print(result2)
print(result3)
