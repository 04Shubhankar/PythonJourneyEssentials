with open("my_file.txt", "w") as file:  # Open a file named "my_file.txt" in write mode
    file.write("This is the first line.\n")  # Write the first line to the file
    file.write("This is the second line.")  # Write the second line to the file

with open("my_file.txt", "a") as file:  # Open the same file in append mode
    file.write("\nThis is appended content.")  # Append a new line to the file

lines = ["Line 1\n", "Line 2\n"]  # Create a list of lines
with open("my_file.txt", "w") as file:  # Open the file in write mode again, overwriting existing content
    file.writelines(lines)  # Write the list of lines to the file
