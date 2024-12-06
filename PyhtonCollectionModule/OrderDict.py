from collections import OrderedDict

# Create an OrderedDict
my_dict = OrderedDict([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])

# Print the OrderedDict
print(my_dict)

# Add a new key-value pair
my_dict['key4'] = 'value4'
print(my_dict)

# Move a key-value pair to the end
my_dict.move_to_end('key2', last=False)
print(my_dict)

# Check if the OrderedDict is empty
if not my_dict:
    print("OrderedDict is empty")
else:
    print("OrderedDict is not empty")



"""
This code demonstrates the basic usage of the OrderedDict class in Python:

Create an OrderedDict: An OrderedDict is created from a list of tuples, where each tuple contains a key and its corresponding value.
Add a new key-value pair: New key-value pairs can be added using the indexing operator.
Move a key-value pair: The move_to_end method can be used to move a key-value pair to the beginning or end of the OrderedDict.
Check emptiness: The bool operator can be used to check if the OrderedDict is empty.
"""
