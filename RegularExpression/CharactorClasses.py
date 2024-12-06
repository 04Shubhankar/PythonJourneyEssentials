import re

word = "How are you Brother12?"

# Match one or more digits
pattern1 = r'\d+'
result1 = re.findall(pattern1, word)

# Match lowercase letters
pattern2 = r'[a-z]+'
result2 = re.findall(pattern2, word)

# Match uppercase letters
pattern3 = r'[A-Z]+'
result3 = re.findall(pattern3, word)

# Match any word character (letters, numbers, underscore)
pattern4 = r'\w+'
result4 = re.findall(pattern4, word)

# Match any non-word character
pattern5 = r'\W+'
result5 = re.findall(pattern5, word)

# Match whitespace characters
pattern6 = r'\s+'
result6 = re.findall(pattern6, word)

print("Digits:", result1)
print("Lowercase letters:", result2)
print("Uppercase letters:", result3)
print("Word characters:", result4)
print("Non-word characters:", result5)
print("Whitespace characters:", result6)
