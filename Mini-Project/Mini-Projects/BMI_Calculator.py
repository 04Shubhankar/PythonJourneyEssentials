# This code calculates the Body Mass Index (BMI) based on user-provided height and weight.

# Get height and weight from the user
Height = float(input("Enter your height in centimeters: "))
Weight = float(input("Enter your Weight in kg: "))

# Convert height from centimeters to meters
Height = Height / 100

# Calculate BMI using the formula: BMI = Weight / (Height * Height)
BMI = Weight / (Height * Height)

# Print the calculated BMI
print("Your Body mass index is:", BMI)

# Check if the BMI is valid (greater than 0)
if BMI > 0:
    # Use nested if-elif-else statements to determine weight category based on BMI
    if BMI <= 16:
        print("You are severely underweight")
    elif BMI <= 18.5:
        print("You are Underweight")
    elif BMI <= 25:
        print("You are Healthy")
    elif BMI <= 30:
        print("You are Overweight")
    else:
        print("You are Severely Overweight")
else:
    # If BMI is not greater than 0, print an error message
    print("Enter Valid Details")
