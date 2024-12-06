# Import the tkinter module for creating GUI applications
from tkinter import *

# Create the main window
root = Tk()
root.geometry("200x200")  # Set the window size to 200x200 pixels

# Define a function to open a new Toplevel window
def open():
    # Create a new Toplevel window
    top = Toplevel(root)
    top.mainloop()  # Start the event loop for the Toplevel window

# Create a button to trigger the open function
btn = Button(root, text="Open", command=open)
btn.place(x=75, y=50)  # Position the button at x=75, y=50

# Start the event loop for the main window
root.mainloop()
