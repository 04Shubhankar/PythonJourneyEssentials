n = "This is a Python language"

# Split the string into words
s = n.split(" ")

# Iterate through each word
for i in s:
    # Check if the length of the word is even
    if len(i) % 2 == 0:
        # Print the word if it has an even length
        print(i)
