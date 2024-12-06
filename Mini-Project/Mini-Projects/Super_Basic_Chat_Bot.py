import time
import random

# This line imports the time and random modules, which are used for various purposes.

name = input("Hello, what is your name?")

# This line prompts the user to enter their name and stores it in the variable 'name'.

time.sleep(2)

# This line adds a delay of 2 seconds before the next line is executed.

print("Hello " + name)

# This line prints a greeting message with the user's name.

feeling = input("How are you today?")

# This line prompts the user to enter how they are feeling and stores it in the variable 'feeling'.

time.sleep(2)

if "good" in feeling:
    print("I am feeling good too!")

# This block checks if the string "good" is present in the 'feeling' variable. If it is, it prints a positive response.

else:
    print("I am sorry to hear that!")

# This block is the else part of the if statement. If the "good" condition is not met, it prints a sympathetic message.

time.sleep(2)

favcolour = input("What is your favourite colour?")

# This line prompts the user to enter their favorite color and stores it in the variable 'favcolour'.

colours = ["Red", "Green", "Blue"]

# This line creates a list of colors.

time.sleep(2)

print("My favorite color is " + random.choice(colours))

# This line randomly selects a color from the 'colours' list and prints it as the program's favorite color.
