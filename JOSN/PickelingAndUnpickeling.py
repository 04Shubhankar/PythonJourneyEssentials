import pickle  # Import the pickle module for object serialization

class Student:
    def __init__(self, name, roll, address):
        self.name = name
        self.roll = roll
        self.address = address

    def disp(self):
        print(f"Name: {self.name} Roll: {self.roll} Address: {self.address}")

with open('student.dat', 'wb') as f:  # Open a file in write binary mode
    stu1 = Student("ram", 101, "pune")  # Create a Student object
    pickle.dump(stu1, f)  # Pickle the object and save it to the file
    print("Pickling Done!")

with open('student.dat', 'rb') as f:  # Open the file in read binary mode
    obj = pickle.load(f)  # Unpickle the object from the file
    print("Unpickling Done!")
    obj.disp()  # Call the disp method of the unpickled object



"""
Explanation:

Import the pickle module: This module provides functions for object serialization and deserialization.
Define the Student class: This class represents a student with attributes name, roll, and address.
Open a file in write binary mode: Create a file named student.dat in write binary mode (wb) for storing the pickled object.
Create a Student object: Create a Student object named stu1 with the specified details.
Pickle the object: Use pickle.dump() to serialize the stu1 object and save it to the file.
Print a message: Indicate that pickling is done.
Open the file in read binary mode: Open the student.dat file in read binary mode (rb) to retrieve the pickled object.
Unpickle the object: Use pickle.load() to deserialize the object from the file and store it in the obj variable.
Print a message: Indicate that unpickling is done.
Call the disp() method: Call the disp() method of the unpickled object to display its details.

"""
