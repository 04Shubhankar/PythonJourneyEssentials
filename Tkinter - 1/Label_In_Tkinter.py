import tkinter as tk
from tkinter import StringVar

# Create the main window (parent container)
root = tk.Tk()
root.title("Label Widget Example")

# Create a StringVar to be used with the textvariable option
label_text = StringVar()
label_text.set("Hello, Tkinter!")

# Create a label with various options
label = tk.Label(
    root,
    anchor="nw",              # Align text to the northwest
    bg="lightblue",            # Background color
    fg="darkblue",             # Foreground (text) color
    font=("Helvetica", 16),    # Font used for the text
    height=4,                  # Height of the label
    width=30,                  # Width of the label
    justify="left",            # Left justify the text
    padx=10,                   # Padding on the left and right sides
    pady=10,                   # Padding on the top and bottom sides
    relief="groove",           # Border style
    textvariable=label_text,   # Link the text to StringVar
    wraplength=200             # Wrap text after 200 pixels
)

# Bitmap and image can be added as follows (commented since no image is provided)
# label.config(bitmap="info")   # To show a bitmap image, remove this line if not needed
# label.config(image=my_image)  # To display an image, replace 'my_image' with a valid image

# Set the underline option
label.config(underline=1)  # Underline the 2nd character ('H' in 'Hello')

# Place the label in the window using grid (can also use pack() or place())
label.grid(row=0, column=0, padx=20, pady=20)

# Button to demonstrate text change using configure() method
def change_text():
    label_text.set("Label text updated!")

button = tk.Button(root, text="Change Text", command=change_text)
button.grid(row=1, column=0, pady=10)

# Set mouse cursor style when hovering over the label
label.config(cursor="hand2")  # Changes cursor to hand when hovered over

# Start the Tkinter event loop
root.mainloop()
