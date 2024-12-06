import re

text = "This is a test.\nMultiple lines."

# Match the beginning of the string
if re.match(r'^This', text):
    print("Starts with 'This'")

# Match the end of the string
if re.search(r'lines$', text):
    print("Ends with 'lines'")

# Match any character between 'T' and 's'
if re.search(r'T.s', text):
    print("Found 'T.s' pattern")
