import json  # Import the json module for working with JSON data

dictionary = {  # Create a Python dictionary to store data
    "name": "sathiyajith",  # Assign the name "sathiyajith" to the key "name"
    "rollno": 56,  # Assign the roll number 56 to the key "rollno"
    "cgpa": 8.6,  # Assign the CGPA 8.6 to the key "cgpa"
    "phonenumber": "9976770500"  # Assign the phone number to the key "phonenumber"
}

with open("sample.json", "w") as outfile:  # Open a file named "sample.json" in write mode
    json.dump(dictionary, outfile)  # Write the dictionary to the file as JSON
