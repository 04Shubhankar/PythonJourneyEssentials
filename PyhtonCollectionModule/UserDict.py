from collections import UserDict

class MyDict(UserDict):
    """
    A custom dictionary class that only allows even values.
    """

    def __setitem__(self, key, value):
        """
        Sets a key-value pair in the dictionary. Raises a ValueError if the value is not even.

        Args:
            key: The key to set.
            value: The value to associate with the key.
        """
        if value % 2 != 0:
            raise ValueError("Value must be even")
        super().__setitem__(key, value)

my_dict = MyDict({'a': 2, 'b': 4})
print(my_dict)  # Output: {'a': 2, 'b': 4}

my_dict['c'] = 6
print(my_dict)  # Output: {'a': 2, 'b': 4, 'c': 6}

try:
    my_dict['d'] = 5
except ValueError as e:
    print(e)  # Output: Value must be even


"""
Explanation:

Import the UserDict class: This line imports the UserDict class from the collections module, which provides a base class for creating custom dictionary-like classes.
Define the MyDict class: This line defines a new class named MyDict that inherits from UserDict. This means that MyDict will have all the attributes and methods of UserDict, but we can override or add our own methods as needed.
Define the __setitem__ method: This method is called when you try to set a value for a key in the dictionary. It checks if the value is even. If it's not, it raises a ValueError. Otherwise, it calls the __setitem__ method of the parent class (UserDict) to actually set the key-value pair.
Create an instance of MyDict: This line creates a new instance of the MyDict class and initializes it with a dictionary containing two key-value pairs.
Print the dictionary: This line prints the contents of the my_dict dictionary.
Add a new key-value pair: This line adds a new key-value pair to the my_dict dictionary. Since the value 6 is even, it's allowed.
Print the dictionary: This line prints the updated contents of the my_dict dictionary.
Try to add an invalid value: This line attempts to add a key-value pair where the value is 5, which is not even. This will raise a ValueError.
Handle the exception: This line catches the ValueError that is raised and prints its message.
In summary, this code creates a custom dictionary class that only allows even values. When a non-even value is assigned, it raises a ValueError.
"""
