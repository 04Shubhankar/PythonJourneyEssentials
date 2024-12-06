from tkinter import *

import calendar

# Generate the calendar for the year 2019
text = calendar.calendar(2019)

# Create the main window
root = Tk()

# Set the window size and title
root.geometry("500x600")
root.title("Calendar")

# Create a label for the title
label1 = Label(root, text="CALENDAR", bg="dark grey", font=("times", 28, "bold"))

# Place the label in the grid layout
label1.grid(row=1, column=1)

# Set the background color of the root window
root.config(background="white")

# Create a label to display the calendar text
label2 = Label(root, text=text, font="Consolas 10")

# Place the label in the grid layout
label2.grid(row=2, column=1, padx=20)

# Start the main event loop
root.mainloop()
