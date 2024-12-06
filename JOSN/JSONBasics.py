import json  # Import the json module for working with JSON data

print(json.dumps({"name": "John", "age": 30}))  # Convert a dictionary to JSON string
print(json.dumps(["apple", "bananas"]))  # Convert a list to JSON string
print(json.dumps(("apple", "bananas")))  # Convert a tuple to JSON string
print(json.dumps("hello"))  # Convert a string to JSON string
print(json.dumps(42))  # Convert an integer to JSON string
print(json.dumps(31.76))  # Convert a float to JSON string
print(json.dumps(True))  # Convert a boolean (True) to JSON string
print(json.dumps(False))  # Convert a boolean (False) to JSON string
print(json.dumps(None))  # Convert None to JSON string (becomes "null")
