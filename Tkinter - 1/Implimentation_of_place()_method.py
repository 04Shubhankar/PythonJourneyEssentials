#Implimentation of .place() method
from tkinter import *  # Import the tkinter module for creating GUIs


# Create the main window
root = Tk()

# Set the size of the window
root.geometry("400x300")

# Create a label and place it at a specific position
label = Label(root, text="Hello, world!")
label.place(x=100, y=100)  # Place the label at coordinates (100, 100)

# Start the main loop
root.mainloop()
