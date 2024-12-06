class Student:
    """Represents a student with a name and marks."""

    def __init__(self, name):
        """Initializes a new Student object with the given name.

        Args:
            name (str): The name of the student.
        """
        self.name = name
        self.marks = []  # Initialize an empty list to store the student's marks

    def add_marks(self, mark):
        """Adds a mark to the student's list of marks.

        Args:
            mark (int): The mark to add.
        """
        self.marks.append(mark)

    def calculate_average_marks(self):
        """Calculates the average of the student's marks.

        Returns:
            float: The average marks.
        """
        total = sum(self.marks)
        return total / len(self.marks)

    def display_report(self):
        """Displays the student's name, marks, and average marks."""
        average_marks = self.calculate_average_marks()
        print("Student name:", self.name)
        print("Student subject-wise marks:", self.marks)
        print("Average Marks:", average_marks)
        print("\n")

# Create an empty list to store student objects
students = []

while True:
    print("Enter student name (or 'exit' to stop):")
    name = input()

    if name == 'exit':
        break

    # Create a new Student object with the entered name and add it to the list
    student = Student(name)
    students.append(student)

    # Get marks for the current student
    while True:
        print("Enter mark (or 'done' to stop):")
        mark = input()

        if mark == 'done':
            break

        # Add the entered mark to the student's marks
        student.add_marks(int(mark))

# Display reports for all students
for student in students:
    student.display_report()
