import tkinter as tk

# Import the Tkinter library for creating graphical interfaces

def scroll_command(x, y):
    """
    Function called when the scrollbar is moved.
    Updates the canvas's scroll region to match the bounding box of all content.
    """
    canvas.configure(scrollregion=canvas.bbox("all"))  # Set scroll region based on all canvas content

root = tk.Tk()

# Create the main window

# Create a canvas with various attributes
canvas = tk.Canvas(root, width=400, height=300,
                   bd=2,  # Border width (2 pixels)
                   bg="lightblue",  # Background color
                   confine=True,  # Confine contents to visible area
                   cursor="hand1",  # Mouse cursor style (hand)
                   highlightcolor="yellow",  # Border color when focused
                   relief="raised")  # Border style (raised)

canvas.pack(fill=tk.BOTH, expand=True)

# Pack the canvas into the main window (fill=BOTH expands to fill space, expand=True allows resizing)

# Draw shapes on the canvas
canvas.create_rectangle(50, 50, 150, 150, fill="green")
canvas.create_oval(200, 50, 300, 150, fill="blue")
canvas.create_line(100, 200, 300, 200, fill="black")

# Draw shapes (rectangle, oval, line) with specified positions and colors

# Configure scrolling
scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a scrollbar and configure it to scroll the canvas vertically
# Pack the scrollbar on the right side and fill its height

# Bind scroll commands
canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * event.delta / 120), "units"))
canvas.bind("<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))
canvas.bind("<Button-5>", lambda event: canvas.yview_scroll(1, "units"))

# Bind events to scroll the canvas:
# - Mouse wheel: scroll up/down based on wheel movement
# - Button-4: scroll one unit up (usually back mouse button)
# - Button-5: scroll one unit down (usually forward mouse button)

root.mainloop()

# Start the main event loop to display the GUI and handle user interactions
