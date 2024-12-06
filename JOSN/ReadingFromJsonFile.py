import json  # Import the json module for working with JSON data

f = open("sample.json")  # Open the file "emp.txt" in read mode (default)

data = json.load(f)  # Load the JSON data from the file into a Python dictionary

for i in data['emp_details']:  # Iterate through the list of employee details

    print(i)  # Print each employee detail

f.close()  # Close the file
