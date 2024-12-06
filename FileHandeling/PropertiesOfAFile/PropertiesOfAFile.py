file = open("myfile.txt", "r")

print(file.name)  # Output: full path to the file
print(file.mode)  # Output: 'r'
print(file.closed)  # Output: False
print(file.readable())  # Output: True
print(file.writable())  # Output: False

file.close()
print(file.closed)  # Output: True
