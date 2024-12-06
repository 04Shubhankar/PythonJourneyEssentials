# This code takes a phrase as input and creates an acronym by combining the first letters of each word.

# Get user input for a phrase
user_input = str(input("Enter a Phrase:"))

# Split the input phrase into a list of words
text = user_input.split()

# Initialize an empty string to store the acronym
a = ""

# Iterate through each word in the list
for i in text:
    # Append the uppercase first letter of the current word to the acronym
    a += str(i[0]).upper()

# Print the final acronym
print(a)
