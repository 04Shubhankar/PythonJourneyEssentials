#Implimentation of pack() method

from tkinter import *  # Import the tkinter module for creating GUIs

# Create the main window (parent)
parent = Tk()

# Create a red button and place it on the left side
redbutton = Button(parent, text="Red", fg="red")  # Create a red button with text "Red"
redbutton.pack(side=LEFT)  # Place the button on the left side

# Create a green button and place it on the right side, filling the available horizontal space
greenbutton = Button(parent, text="green", fg="green")
greenbutton.pack(side=RIGHT, fill=X)  # Fill the available horizontal space

# Create a blue button and place it at the top
bluebutton = Button(parent, text="Blue", fg="blue")
bluebutton.pack(side=TOP)

# Create a black button and place it at the bottom
blackbutton = Button(parent, text="Black", fg="black")
blackbutton.pack(side=BOTTOM)

# Start the main loop to display the GUI
parent.mainloop()
