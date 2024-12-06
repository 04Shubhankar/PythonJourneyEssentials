with open('myfile.txt', 'r+b') as f:
  # Move to the 10th byte
  f.seek(10)
  print("Current position:", f.tell())  # Output: 10

  # Read 5 bytes from the current position
  data = f.read(5)
  print(data)

  # Move back to the beginning
  f.seek(0)
  print("Current position:", f.tell())  # Output: 0
