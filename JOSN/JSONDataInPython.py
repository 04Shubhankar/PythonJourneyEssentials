import json

# Create a Python dictionary
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Convert dictionary to JSON string
json_string = json.dumps(data)

# Print the JSON string
print(json_string)

# Convert JSON string back to Python dictionary
python_object = json.loads(json_string)

# Print the Python object
print(python_object)

# Write JSON to a file
with open('data.json', 'w') as file:
    json.dump(data, file)

# Read JSON from a file
with open('data.json', 'r') as file:
    loaded_data = json.load(file)

# Print the loaded data
print(loaded_data)
