import tkinter as tk

def greet():
    print("Hello, world!")

root = tk.Tk()

# Create a button with various attributes and add comments
button = tk.Button(root,
                   text="Click me",
                   command=greet,
                   activebackground="yellow",  # Background color when pressed
                   activeforeground="blue",  # Text color when pressed
                   bd=5,  # Border width
                   bg="green",  # Background color
                   cursor="hand1",  # Mouse cursor style
                   fg="red",  # Text color
                   font=("Helvetica", 12, "bold"),  # Font style, size, and weight
                   height=2,  # Height in lines
                   highlightbackground="orange",  # Background color when focused
                   highlightcolor="purple",  # Border color when focused
                   image=None,  # Replace with an image path if needed
                   justify="center",  # Text alignment
                   padx=10,  # Horizontal padding
                   pady=5,  # Vertical padding
                   relief="raised",  # Border style
                   state="normal",  # Button state
                   takefocus=True,  # Whether it can receive keyboard focus
                   underline=0,  # Index of underlined character
                   width=20,  # Width in characters
                   wraplength=100,  # Maximum text width before wrapping
                   bitmap=None,  # Replace with a bitmap path if needed
                   compound="left",  # Combine text and image
                   overrelief="sunken")  # Relief style when the mouse hovers

button.pack()

root.mainloop()
