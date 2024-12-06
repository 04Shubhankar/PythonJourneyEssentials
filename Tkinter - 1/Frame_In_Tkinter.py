import tkinter as tk

root = tk.Tk()

# Create a frame with various options
frame = tk.Frame(
    root,
    bd=5,
    bg="lightblue",
    cursor="hand2",
    height=200,
    highlightbackground="yellow",
    highlightcolor="red",
    highlightthickness=2,
    width=300
)

# Place the frame using the grid layout
frame.grid(row=0, column=0, padx=10, pady=10)

# Create a label and a button within the frame
label = tk.Label(frame, text="This is a label within a frame")
label.pack(padx=10, pady=10)

button = tk.Button(frame, text="Click me")
button.pack(padx=10, pady=10)

root.mainloop()
