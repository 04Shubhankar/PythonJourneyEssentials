import csv

# Create CSV file with header
filename = "students.csv"
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['Roll_no', 'Name', 'Grade', 'City']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# Add students
num_students = int(input("Enter number of students: "))
for i in range(num_students):
    roll_no = input("Enter Roll number: ")
    name = input("Enter students name: ")
    grade = input("Enter students grade: ")
    city = input("Enter students city: ")
    
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['Roll_no', 'Name', 'Grade', 'City']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Roll_no': roll_no, 'Name': name, 'Grade': grade, 'City': city})

# Read CSV file
with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

# Search for student
roll_no_search = input("Enter roll number to search: ")
found = False
with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Roll_no'] == roll_no_search:
            print("Student found:", row)
            found = True
            break
if not found:
    print("Student not found")

# Update student
roll_no_update = input("Enter roll number to update: ")
found = False
temp_rows = []
with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Roll_no'] == roll_no_update:
            found = True
            new_name = input("Enter new name: ")
            new_grade = input("Enter new grade: ")
            new_city = input("Enter new city: ")
            row['Name'] = new_name
            row['Grade'] = new_grade
            row['City'] = new_city
        temp_rows.append(row)

if not found:
    print("Student not found")
else:
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(temp_rows)

# Delete student
roll_no_delete = input("Enter roll number to delete: ")
found = False
temp_rows = []
with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Roll_no'] != roll_no_delete:
            temp_rows.append(row)
        else:
            found = True

if not found:
    print("Student not found")
else:
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(temp_rows)



"""
Enter number of students: 5
Enter Roll number: 1
Enter students name: Abhishek
Enter students grade: 10
Enter students city: Mumbai
Enter Roll number: 2
Enter students name: Mehek
Enter students grade: 9
Enter students city: Vashi
Enter Roll number: 3
Enter students name: Sujal
Enter students grade: 8
Enter students city: Airoli
Enter Roll number: 4
Enter students name: Prem
Enter students grade: 10
Enter students city: Ghansoli
Enter Roll number: 5
Enter students name: Akshad
Enter students grade: 7.7
Enter students city: Ghansoli
{'Roll_no': '1', 'Name': 'Abhishek', 'Grade': '10', 'City': 'Mumbai'}
{'Roll_no': '2', 'Name': 'Mehek', 'Grade': '9', 'City': 'Vashi'}
{'Roll_no': '3', 'Name': 'Sujal', 'Grade': '8', 'City': 'Airoli'}
{'Roll_no': '4', 'Name': 'Prem', 'Grade': '10', 'City': 'Ghansoli'}
{'Roll_no': '5', 'Name': 'Akshad', 'Grade': '7.7', 'City': 'Ghansoli'}
Enter roll number to search: 3
Student found: {'Roll_no': '3', 'Name': 'Sujal', 'Grade': '8', 'City': 'Airoli'}
Enter roll number to update: 1
Enter new name: AbhishekM
Enter new grade: 10
Enter new city: Mumbai
Enter roll number to delete: 5

"""
