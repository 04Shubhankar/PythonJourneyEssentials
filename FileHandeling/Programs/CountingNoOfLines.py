filename = input("Enter the file name: ")  # Prompts the user to enter the file name and stores it in the 'filename' variable

with open(filename, 'r') as file:  # Opens the file with the specified name in read mode ('r') using the 'with' statement for automatic resource management
    count = 0  # Initializes a counter to keep track of the number of lines

    for line in file:  # Iterates through each line in the file
        count += 1  # Increments the counter for each line

print("Number of lines in the file:", count)  # Prints the total number of lines in the file
