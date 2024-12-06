import os  # Import the os module for operating system interactions

file_name = input("Enter the file name:")  # Prompt the user to enter the file name

if os.path.exists(file_name):  # Check if the file exists

    file_size = os.path.getsize(file_name)  # Get the size of the file in bytes
    file_created = os.path.getctime(file_name)  # Get the creation time of the file
    file_modified = os.path.getmtime(file_name)  # Get the modification time of the file
    file_accessed = os.path.getatime(file_name)  # Get the access time of the file

    print(f"file name: {file_name}")  # Print the file name
    print(f'File size: {file_size} bytes')  # Print the file size in bytes
    print(f'File created: {file_created}')  # Print the file creation time
    print(f'File modified: {file_modified}')  # Print the file modification time
    print(f'File accessed: {file_accessed}')  # Print the file access time

else:
    print(f'File {file_name} does not exist.')  # Print a message if the file doesn't exist
