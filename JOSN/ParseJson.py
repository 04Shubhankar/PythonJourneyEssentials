import json  # Import the 'json' module for working with JSON data

x = '{"name": "John", "age": 30, "city": "New york"}'  # Create a JSON string representing a person's information

y = json.loads(x)  # Parse the JSON string into a Python dictionary

print(y["age"])  # Access and print the 'age' value from the dictionary
