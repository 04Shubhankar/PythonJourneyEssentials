from collections import namedtuple

# Create a namedtuple class
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instances of the namedtuple
person1 = Person('Alice', 30, 'New York')
person2 = Person('Bob', 25, 'Los Angeles')

# Access values using attributes
print(person1.name)  # Output: Alice
print(person2.age)  # Output: 25

# Create a new namedtuple with modified values
person3 = person1._replace(age=31)
print(person3)  # Output: Person(name='Alice', age=31, city='New York')

# Convert a namedtuple to a dictionary
person_dict = person1._asdict()
print(person_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Create a namedtuple from a dictionary
person4 = Person(**person_dict)
print(person4)  # Output: Person(name='Alice', age=30, city='New York')

# Convert a namedtuple to a regular tuple
person_tuple = tuple(person1)
print(person_tuple)  # Output: ('Alice', 30, 'New York')

"""

This code demonstrates the basic usage of the namedtuple class in Python:

Create a namedtuple class: Use the namedtuple function to create a new namedtuple class with specified field names.
Create instances: Create instances of the namedtuple class by passing values for the fields.
Access values: Use attributes to access the values of the namedtuple fields.
Create new namedtuples: Use the _replace method to create a new namedtuple with modified values.
Convert to dictionaries: Use the _asdict method to convert a namedtuple to a dictionary.
Create namedtuples from dictionaries: Use the ** operator to create a namedtuple from a dictionary.
"""
