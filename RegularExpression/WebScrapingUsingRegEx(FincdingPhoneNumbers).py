import re
import urllib.request

# Open a URL connection to the specified website
u = urllib.request.urlopen("https://gopgms.com/contactus.html")

# Read the content of the webpage
text = u.read()

# Extract phone numbers using regular expression
numbers = re.findall("[0-9-]{7}[0-9-]+", str(text), re.I)

# Print the extracted phone numbers
for n in numbers:
    print(n)


"""
import re: Imports the re module for regular expression operations.
import urllib.request: Imports the urllib.request module for handling URL requests.
u = urllib.request.urlopen("https://gopgms.com/contactus.html"): Opens a URL connection to the specified website and stores it in the u variable.
text = u.read(): Reads the content of the webpage and stores it in the text variable.
numbers = re.findall("[0-9-]{7}[0-9-]+", str(text), re.I):
Uses re.findall() to find all occurrences of the specified pattern in the text.
The pattern "[0-9-]{7}[0-9-]+" matches sequences of 7 digits or hyphens followed by one or more digits or hyphens.
str(text) converts the text content (which might be in bytes format) to a string for regular expression matching.
re.I makes the search case-insensitive.
for n in numbers:: Iterates over each extracted phone number in the numbers list.
print(n): Prints the extracted phone number.

"""
