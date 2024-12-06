with open("xyz.txt", "w") as file:  # Opens a file named "xyz.txt" in write mode ('w') and assigns it to the variable 'file'
    file.write('Hello, World! This Is Python')  # Writes the text "Hello, World!" to the file

with open("xyz.txt", "r") as file:  # Opens the same file "xyz.txt" in read mode ('r') and assigns it to the variable 'file'
    contents = file.read()  # Reads the entire contents of the file and stores it in the 'contents' variable
    num_chars = len(contents)  # Calculates the number of characters in the 'contents' string and stores it in 'num_chars'

print(f'The file xyz.txt contains {num_chars} characters.')  # Prints a formatted string showing the number of characters in the file
