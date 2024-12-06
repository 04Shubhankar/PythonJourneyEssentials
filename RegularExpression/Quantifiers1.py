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

# Match exactly two 'a' characters
pattern4 = 'a{2}'
result4 = re.findall(pattern4, word)

# Match one or more 'a' characters (equivalent to 'a+')
pattern5 = 'a{1,}'
result5 = re.findall(pattern5, word)

# Match between one and three 'a' characters
pattern6 = 'a{1,3}'
result6 = re.findall(pattern6, word)

# Print the results of each pattern
print("One or more a:", result1)
print("Zero or more a:", result2)
print("Zero or one a:", result3)
print("Exactly two a:", result4)
print("One or more a (equivalent to a+):", result5)
print("One to three a:", result6)
