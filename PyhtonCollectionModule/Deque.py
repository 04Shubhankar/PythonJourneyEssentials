from collections import deque

# Create a deque
my_deque = deque(['apple', 'banana', 'orange'])

# Add elements to the right end
my_deque.append('pear')
print(my_deque)  # Output: deque(['apple', 'banana', 'orange', 'pear'])

# Add elements to the left end
my_deque.appendleft('grape')
print(my_deque)  # Output: deque(['grape', 'apple', 'banana', 'orange', 'pear'])

# Remove elements from the right end
removed_element = my_deque.pop()
print(removed_element)  # Output: pear
print(my_deque)  # Output: deque(['grape', 'apple', 'banana', 'orange'])

# Remove elements from the left end
removed_element = my_deque.popleft()
print(removed_element)  # Output: grape
print(my_deque)  # Output: deque(['apple', 'banana', 'orange'])

# Rotate the deque to the right
my_deque.rotate(2)
print(my_deque)  # Output: deque(['orange', 'pear', 'apple', 'banana'])

# Rotate the deque to the left
my_deque.rotate(-1)
print(my_deque)  # Output: deque(['pear', 'apple', 'banana', 'orange'])

# Check if the deque is empty
print(my_deque.empty())  # Output: False

# Get the length of the deque
print(len(my_deque))  # Output: 4

"""

This code demonstrates the basic usage of the deque class in Python:

Create a deque: A deque is created from an iterable.
Add elements: Elements can be added to the right end using append or to the left end using appendleft.
Remove elements: Elements can be removed from the right end using pop or from the left end using popleft.
Rotate elements: The rotate method can be used to rotate the deque to the right or left.
"""
