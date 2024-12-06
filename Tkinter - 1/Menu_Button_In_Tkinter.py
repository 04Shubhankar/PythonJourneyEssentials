import tkinter as tk

root = tk.Tk()

# Create a menubutton with a menu
menubutton = tk.Menubutton(
    root,
    text="Options",
    anchor="center",  # Center align text within the button
    bg="lightblue",
    disabledforeground="gray",  # Set color for disabled state
    font=("Arial", 12, "bold"),
    fg="green",
    height=2,
    image=None,  # You can set an image here
    justify="left",
    menu=None,  # You can associate a menu here
    padx=10,
    pady=5,
    relief="groove",
    textvariable=None,  # You can associate a variable
    underline=0,
    width=20,
)

# Create a menu associated with the menubutton
menu = tk.Menu(menubutton, tearoff=0)
menu.add_command(label="Option 1", command=lambda: print("Option 1 clicked"))
menu.add_command(label="Option 2", command=lambda: print("Option 2 clicked"))
menu.add_separator()
menu.add_checkbutton(label="Check me")

# Configure the menubutton to use the created menu
menubutton.config(menu=menu)

# Pack the menubutton into the root window
menubutton.pack()

root.mainloop()
