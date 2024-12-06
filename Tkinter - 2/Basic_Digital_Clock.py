import sys
from tkinter import *
import time

def times():
    # Get the current time in the format "HH:MM:SS"
    current_time = time.strftime("%H:%M:%S")

    # Update the clock label with the current time
    clock.config(text=current_time)

    # Schedule the `times` function to be called again after 200 milliseconds
    clock.after(200, times)

root = Tk()
root.geometry("500x250")  # Set the window size

clock = Label(root, font=("Times", 50, "bold"), bg="white")
clock.grid(row=2, column=2, pady=25, padx=100)  # Position and style the clock label

times()  # Start the clock update process

digi = Label(root, text="Digital Clock", font=("Times", 24, "bold"))
digi.grid(row=0, column=2)  # Position the title label

root.mainloop()  # Start the main event loop
