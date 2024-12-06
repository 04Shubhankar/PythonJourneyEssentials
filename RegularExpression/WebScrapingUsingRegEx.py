import re, urllib  # Import necessary modules for regular expressions and URL handling
import urllib.request  # Import the 'request' submodule from urllib

sites = "moneycontrol google".split()  # Create a list of websites to process
print(sites)  # Print the list of websites

for s in sites:  # Iterate over each website in the list
    print("searching...", s)  # Print a message indicating the website being searched

    u = urllib.request.urlopen("http://" + s + ".com")  # Open a URL connection to the website
    text = u.read()  # Read the content of the webpage

    title = re.findall("<title>.*</title>", str(text), re.I)  # Extract the title using regular expression
    print(title[0])  # Print the extracted title


"""
import re, urllib: Imports the re module for regular expressions and the urllib module for handling URLs.
import urllib.request: Imports the request submodule from the urllib module for opening URLs.
sites="moneycontrol google".split(): Creates a list of websites to process by splitting the string at whitespace.
print(sites): Prints the list of websites for reference.
for s in sites:: Starts a loop to iterate over each website in the list.
print("searching...", s): Prints a message indicating the website being searched.
u = urllib.request.urlopen("http://" + s + ".com"): Opens a URL connection to the specified website using urllib.request.urlopen().
text = u.read(): Reads the content of the webpage and stores it in the text variable.
title = re.findall("<title>.*</title>", str(text), re.I): Uses re.findall() to extract the title from the HTML content. The regular expression "<title>.*</title>" matches the entire <title> tag, including its content. The re.I flag makes the search case-insensitive.
print(title[0]): Prints the first element of the title list, which contains the extracted title.

"""
