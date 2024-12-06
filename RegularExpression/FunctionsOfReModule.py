import re  # Import the regular expression module

text = "The phone number is 415-555-1212. Email: john.doe@example.com"  # Define the text to be processed

# Operation: match()
print("Operation: match()")
match_result = re.match(r'The', text)  # Attempt to match the beginning of the text with 'The'
if match_result:  # Check if a match was found
    print(match_result.group())  # Print the matched substring
else:
    print("Not found")  # Print a message if no match

# Operation: fullmatch()
print("Operation: fullmatch()")
full_match_result = re.fullmatch(r'The phone number is 415-555-1212. Email: john.doe@example.com', text)  # Attempt to match the entire text with the given pattern
if full_match_result:  # Check if the entire text matched
    print(full_match_result.group())  # Print the matched text
else:
    print("Not found")  # Print a message if no full match

# Operation: search()
print("Operation: search()")
search_result = re.search(r'\d{3}-\d{3}-\d{4}', text)  # Search for the phone number pattern in the text
if search_result:  # Check if a phone number was found
    print(search_result.group())  # Print the matched phone number
else:
    print("Not found")  # Print a message if no phone number found

# Operation: findall()
print("Operation: findall()")
findall_result = re.findall(r'\w+', text)  # Find all words in the text
print(findall_result)  # Print the list of words

# Operation: finditer()
print("Operation: finditer()")
finditer_result = re.finditer(r'\w+', text)  # Find all words in the text as iterators
for match in finditer_result:  # Iterate over the match objects
    print(match.group())  # Print each matched word

# Operation: sub()
print("Operation: sub()")
sub_result = re.sub(r'\d', '*', text)  # Replace all digits with '*'
print(sub_result)  # Print the modified text

# Operation: subn()
print("Operation: subn()")
subn_result = re.subn(r'\d', '*', text)  # Replace all digits with '*' and count replacements
print(subn_result)  # Print the modified text and the number of replacements

# Operation: split()
print("Operation: split()")
split_result = re.split(r'\s+', text)  # Split the text into words based on whitespace
print(split_result)  # Print the list of words

# Operation: compile()
print("Operation: compile()")
phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')  # Compile the phone number pattern for efficiency
compiled_search_result = phone_pattern.search(text)  # Search for the phone number using the compiled pattern
if compiled_search_result:
    print(compiled_search_result.group())  # Print the matched phone number
