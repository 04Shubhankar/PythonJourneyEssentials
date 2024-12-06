with open('number.txt', 'r') as input_file:  # Open the file 'numbers.txt' in read mode
    numbers = input_file.read().split()  # Read the file contents, split into a list of strings
    numbers = [int(num) for num in numbers]  # Convert each string to an integer

odd_numbers = [num for num in numbers if num % 2 != 0]  # Create a list of odd numbers using list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]  # Create a list of even numbers using list comprehension

with open('odd.txt', 'w') as odd_file:  # Open 'odd.txt' in write mode
    odd_file.write('\n'.join(str(num) for num in odd_numbers))  # Write odd numbers to a file, separated by newlines

with open('even.txt', 'w') as even_file:  # Open 'even.txt' in write mode
    even_file.write('\n'.join(str(num) for num in even_numbers))  # Write even numbers to a file, separated by newlines



"""

The provided code assumes that each number in the input file numbers.txt is on a separate line. The line numbers = input_file.read().split() splits the file content into a list of strings based on whitespace, which includes newlines. This implicitly assumes that numbers are separated by newlines.
"""
