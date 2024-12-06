with open('input.txt', 'r') as input_file:  # Opens the file 'input.txt' in read mode ('r') and assigns it to the variable 'input_file'
    contents = input_file.read()  # Reads the entire contents of the 'input.txt' file and stores it in the 'contents' variable

contents_upper = contents.upper()  # Converts the contents of the 'contents' variable to uppercase and stores it in 'contents_upper'

with open('output.txt', 'w') as output_file:  # Opens the file 'output.txt' in write mode ('w') and assigns it to the variable 'output_file'
    output_file.write(contents_upper)  # Writes the contents of the 'contents_upper' variable (uppercase text) to the 'output.txt' file

with open('output.txt', 'r') as output_file:  # Opens the file 'output.txt' in read mode ('r') and assigns it to the variable 'output_file'
    print(output_file.read())  # Reads the contents of the 'output.txt' file and prints it to the console



"""
with open('input.txt', 'r') as input_file:  # Opens the file 'input.txt' in read mode ('r') and assigns it to the variable 'input_file'
    contents = input_file.read()  # Reads the entire contents of the 'input.txt' file and stores it in the 'contents' variable

contents_upper = contents.upper()  # Converts the contents of the 'contents' variable to uppercase and stores it in 'contents_upper'

with open('output.txt', 'w') as output_file:  # Opens the file 'output.txt' in write mode ('w') and assigns it to the variable 'output_file'
    output_file.write(contents_upper)  # Writes the contents of the 'contents_upper' variable (uppercase text) to the 'output.txt' file

with open('output.txt', 'r') as output_file:  # Opens the file 'output.txt' in read mode ('r') and assigns it to the variable 'output_file'
    print(output_file.read())  # Reads the contents of the 'output.txt' file and prints it to the console


"""
