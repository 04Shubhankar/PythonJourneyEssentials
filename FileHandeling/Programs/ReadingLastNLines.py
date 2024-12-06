def read_last_n_lines(file_path, n):
  """
  Reads the last n lines of a file.

  Args:
    file_path: The path to the file.
    n: The number of lines to read.

  Returns:
    A list of the last n lines of the file.
  """

  with open(file_path, 'r') as f:  # Open the file in read mode
    lines = f.readlines()  # Read all lines into a list
    return lines[-n:]  # Return the last n lines

# Example usage:
file_path = 'myfile.txt'  # Specify the file path
n = 2  # Specify the number of lines to read
last_n_lines = read_last_n_lines(file_path, n)  # Call the function to get the last n lines
print(last_n_lines)  # Print the last n lines
