import json  # Import the json module for working with JSON data

dictionary = {  # Create a Python dictionary to store data
    "id": "04",  # Assign the value "04" to the key "id"
    "name": "Sunil",  # Assign the value "Sunil" to the key "name"
    "department": "HR"  # Assign the value "HR" to the key "department"
}

json_object = json.dumps(dictionary, indent=4)  # Convert the dictionary to a formatted JSON string
print(json_object)  # Print the formatted JSON string
