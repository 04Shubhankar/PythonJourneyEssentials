import re

text = "apple"

# Check for 'es' at the beginning
match_start = re.match('es', text)

# Check for 'es' at the end
match_end = re.search('es$', text)

if match_start:
    print("Found 'es' at the beginning")
elif match_end:
    print("Found 'es' at the end")
else:
    print("No match found")
