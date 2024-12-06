# Open a file named "example3.txt" in write mode ('w')
f1 = open("example3.txt", "w")

# Create a list of strings to be written to the file
list1 = ["wednesday", "thursday", "Monday"]

# Write the list of strings to the file
f1.writelines(list1)

# Close the file
f1.close()

# Open the same file in read mode ('r')
f2 = open("example3.txt", "r")

# Read all lines from the file into a list
data = f2.readlines()

# Print each line without a newline character
for i in data:
    print(i, end="")


"""

f1 = open("example3.txt", "w"): Opens a file named "example3.txt" in write mode. If the file doesn't exist, it creates a new one. If it exists, it overwrites the contents.
list1 = ["wednesday", "thursday", "Monday"]: Creates a list of strings to be written to the file.
f1.writelines(list1): Writes the contents of the list list1 to the file.
f1.close(): Closes the file after writing.
f2 = open("example3.txt", "r"): Opens the same file in read mode to read its contents.
data = f2.readlines(): Reads all lines from the file and stores them in the data list.
for i in data:: Iterates through each line in the data list.
print(i, end=""): Prints the current line without adding a newline character at the end. This ensures that the output is displayed on a single line.
"""
