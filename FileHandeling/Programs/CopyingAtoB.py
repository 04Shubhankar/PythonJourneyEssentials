with open('a.txt', 'r') as file_a:  # Opens the file 'a.txt' in read mode ('r') and assigns it to the variable 'file_a'
    with open('b.txt', 'w') as file_b:  # Opens the file 'b.txt' in write mode ('w') and assigns it to the variable 'file_b'
        file_b.write(file_a.read())  # Reads the contents of 'file_a' and writes them to 'file_b'
