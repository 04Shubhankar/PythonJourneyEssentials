with open("my_file.txt", "r") as file:
    # Read the entire file
    content = file.read()
    print("Entire File Contents:\n", content)

    # Read one line
    line = file.readline()
    print("First Line:", line)

    # Read all remaining lines (after the first line)
    lines = file.readlines()
    print("Remaining Lines:")
    for line in lines:
        print(line, end="")  # Print without extra newline after each line

# Note: This approach assumes the file is not extremely large.
# For very large files, consider reading in chunks or line by line using a loop.
