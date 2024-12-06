import json  # Import the json module for working with JSON data

x = {  # Create a Python dictionary to store data

    "name": "raj",  # Name of the person
    "age": 32,  # Age of the person
    "married": True,  # Marital status (True for married)
    "divorced": False,  # Marital status (False for not divorced)
    "children": ("ram", "sham"),  # Children's names (as a tuple)
    "pets": None,  # No pets (represented by None)
    "cars": [  # List of cars
        {"model": "BMW 230", "mpg": 27.5},  # First car with model and mpg
        {"model": "Ford Edge", "mpg": 24.1}  # Second car with model and mpg
    ]
}

print(json.dumps(x))  # Convert the Python dictionary to a JSON string and print it


"""

Explanation:

The code imports the json module, which is used for working with JSON data.
A Python dictionary x is created to store various types of data.
The dictionary contains key-value pairs representing different attributes like name, age, marital status, children, pets, and cars.
The cars key holds a list of dictionaries, each representing a car with its model and mpg.
Finally, the json.dumps() function is used to convert the Python dictionary x into a JSON string, which is then printed to the console.
"""
