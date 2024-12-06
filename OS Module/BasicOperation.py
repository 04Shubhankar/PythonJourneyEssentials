import os

file_path = "myfile.txt"  # Specify the file path
directory_path = "my_directory"  # Specify the directory path

# Check if the file exists
if os.path.exists(file_path):  # Check if the file path exists
    # Check if it's a file
    if os.path.isfile(file_path):  # Check if the path is a regular file
        print("The file exists and is a regular file.")
    else:
        print("The file exists but is not a regular file.")
else:
    print("The file does not exist.")

# Check if the directory exists
if os.path.exists(directory_path):  # Check if the directory path exists
    # Check if it's a directory
    if os.path.isdir(directory_path):  # Check if the path is a directory
        print("The directory exists.")
    else:
        print("The path exists but is not a directory.")
else:
    print("The directory does not exist.")
