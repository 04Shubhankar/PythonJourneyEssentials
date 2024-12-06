from collections import Counter

# Sample list
my_list = ['apple', 'banana', 'orange', 'apple', 'banana', 'banana']

# Create a Counter object
word_counts = Counter(my_list)

# Print the word counts
print(word_counts)

# Find the most common word
most_common_word = word_counts.most_common(1)
print("Most common word:", most_common_word)

# Update the count of a specific word
word_counts['apple'] += 2
print(word_counts)

# Perform mathematical operations on counts
word_counts.update(['pear', 'pear'])
print(word_counts)

# Check if a word exists in the Counter
if 'orange' in word_counts:
    print("Orange count:", word_counts['orange'])
else:
    print("Orange is not in the Counter")
"""
This code demonstrates the basic usage of the Counter class in Python:

Create a Counter object: A Counter object is created from a list of elements.
Count occurrences: The Counter automatically counts the occurrences of each element in the list.
Find most common: The most_common method returns a list of tuples, where each tuple contains an element and its count.
Update counts: The update method can be used to update the counts of existing elements or add new elements.
Check existence: The in operator can be used to check if an element exists in the Counter.
"""
