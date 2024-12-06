from collections import ChainMap

# Create multiple dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}

# Combine the dictionaries into a ChainMap
chain_map = ChainMap(dict3, dict2, dict1)

# Access values from the ChainMap
print(chain_map['a'])  # Output: 1
print(chain_map['b'])  # Output: 3
print(chain_map['c'])  # Output: 5
print(chain_map['d'])  # Output: 6

# Create a new ChainMap with a new child dictionary
new_chain_map = chain_map.new_child({'e': 7})

# Access values from the new ChainMap
print(new_chain_map['a'])  # Output: 1
print(new_chain_map['b'])  # Output: 3
print(new_chain_map['c'])  # Output: 5
print(new_chain_map['d'])  # Output: 6
print(new_chain_map['e'])  # Output: 7

# Update a value in the child dictionary
new_chain_map['e'] = 8

# The change is reflected in the new ChainMap
print(new_chain_map['e'])  # Output: 8

# Access values from the original ChainMap
print(chain_map['e'])  # Output: 7


"""
This code demonstrates the use of the new_child function to create a new ChainMap with a new child dictionary:

Create multiple dictionaries: Create multiple dictionaries that you want to combine.
Combine dictionaries: Use the ChainMap constructor to combine the dictionaries into a single ChainMap object.
Create a new ChainMap with a child dictionary: Use the new_child function to create a new ChainMap with a new child dictionary. The child dictionary will be the first dictionary in the new ChainMap.
Access values: Use the indexing operator to access values from the new ChainMap. The ChainMap will search the dictionaries in the order they were passed to the constructor.
Update values: You can update values in any of the underlying dictionaries. The changes will be reflected in the appropriate ChainMap.
"""
