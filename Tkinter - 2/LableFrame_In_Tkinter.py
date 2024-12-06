import tkinter as tk

root = tk.Tk()

# Create a LabelFrame with various options
labelframe = tk.LabelFrame(
    root,
    text="Personal Information",
    bg="lightblue",
    bd=5,
    relief=tk.RAISED,
    font=("Arial", 14, "bold"),
    fg="darkblue",
    cursor="hand2",
    highlightbackground="gray",
    highlightcolor="black",
    highlightthickness=2,
    padx=10,
    pady=10
)

# Add widgets to the LabelFrame
name_label = tk.Label(labelframe, text="Name:")
name_entry = tk.Entry(labelframe)
age_label = tk.Label(labelframe, text="Age:")
age_entry = tk.Spinbox(labelframe, from_=0, to=120)

name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry.grid(row=0, column=1, padx=5, pady=5)
age_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
age_entry.grid(row=1, column=1, padx=5, pady=5)

labelframe.pack(fill=tk.BOTH, expand=True)

root.mainloop()
