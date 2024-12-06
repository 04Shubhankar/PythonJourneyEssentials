from collections import UserList

class MyList(UserList):
    def __setitem__(self, index, value):
        if value % 2 != 0:
            raise ValueError("Value must be even")
        super().__setitem__(index, value)

my_list = MyList([2, 4, 6])
print(my_list)  # Output: [2, 4, 6]

my_list[1] = 8
print(my_list)  # Output: [2, 8, 6]

try:
    my_list[2] = 5
except ValueError as e:
    print(e)  # Output: Value must be even


"""
here's a comprehensive explanation of how the UserList class and the __setitem__ method work together:

UserList Class:

A built-in Python class that provides a base class for creating custom list-like classes.
Inheriting from UserList gives your custom class all the attributes and methods of regular lists, such as append, pop, extend, etc.
You can override specific methods in your custom class to customize their behavior.
__setitem__ Method:

A special method that is called when you use the indexing operator [] to set an element in a list.
Takes two arguments:
index: The index of the element you want to set.
value: The new value for the element.
By default, __setitem__ simply sets the value at the specified index.
You can override this method in your custom class to add custom logic or validation.
Combining UserList and __setitem__:

Create a custom class: Inherit from UserList to create your custom list class.
Override __setitem__: Define a new __setitem__ method in your custom class.
Add custom logic: Inside the overridden __setitem__ method, you can implement your desired behavior. For example, you could:
Validate the value being assigned.
Modify the value before setting it.
Perform additional actions based on the index or value.
Example (without code):

Imagine you want to create a custom list that only allows even numbers. You could override __setitem__ to check if the value is even before setting it. If the value is odd, you could raise an error.

Key points:

UserList provides a foundation for creating custom lists.
__setitem__ controls how elements are set in a list.
By overriding __setitem__, you can customize the behavior of your custom list class.

"""
