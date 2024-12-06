# Implimentation of grid() method

from tkinter import *  # Import the tkinter module for creating GUIs

# Create the main window (parent)
parent = Tk()

# Create a label for the name and place it in the first row and first column
name = Label(parent, text="Name").grid(row=0, column=0)

# Create an entry field for the name and place it in the first row and second column
e1 = Entry(parent).grid(row=0, column=1)

# Create a label for the password and place it in the second row and first column
password = Label(parent, text="Password").grid(row=1, column=0)

# Create an entry field for the password and place it in the second row and second column
e2 = Entry(parent).grid(row=1, column=1)

# Create a submit button and place it in the fourth row and first column
submit = Button(parent, text="Submit").grid(row=4, column=0)

# Start the main loop to display the GUI
parent.mainloop()
