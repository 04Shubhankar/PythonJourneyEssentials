import tkinter as tk

root = tk.Tk()

# Create a menu bar
menubar = tk.Menu(root)

# Create a file menu with various options
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=lambda: print("Open clicked"))
filemenu.add_command(label="Save", command=lambda: print("Save clicked"), accelerator="Ctrl+S")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit, accelerator="Ctrl+Q")

# Create an edit menu with radio buttons
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_radiobutton(label="Cut", command=lambda: print("Cut clicked"))
editmenu.add_radiobutton(label="Copy", command=lambda: print("Copy clicked"))
editmenu.add_radiobutton(label="Paste", command=lambda: print("Paste clicked"))

# Create a view menu with checkbuttons
viewmenu = tk.Menu(menubar, tearoff=0)
show_grid_var = tk.BooleanVar()
viewmenu.add_checkbutton(label="Show Grid", variable=show_grid_var, command=lambda: print("Show Grid:", show_grid_var.get()))
show_ruler_var = tk.BooleanVar()
viewmenu.add_checkbutton(label="Show Ruler", variable=show_ruler_var, command=lambda: print("Show Ruler:", show_ruler_var.get()))

# Create a help menu with a cascade submenu
helpmenu = tk.Menu(menubar, tearoff=0)
aboutmenu = tk.Menu(helpmenu, tearoff=0)
aboutmenu.add_command(label="About", command=lambda: print("About clicked"))
aboutmenu.add_command(label="Help", command=lambda: print("Help clicked"))
helpmenu.add_cascade(label="About", menu=aboutmenu)

# Add the menus to the menubar
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="View", menu=viewmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

# Add the menubar to the root window
root.config(menu=menubar)

# Bind accelerators to menu items
root.bind("<Control-s>", lambda event: menu_command(filemenu, "Save"))
root.bind("<Control-q>", lambda event: menu_command(filemenu, "Exit"))

def menu_command(menu, label):
    """
    Disables the clicked menu item for a short time and then re-enables it.
    """
    menu.entryconfig(menu.index(tk.ACTIVE), state="disabled")
    root.after(1000, lambda: menu.entryconfig(menu.index(tk.ACTIVE), state="normal"))
    print(f"{label} clicked")

root.mainloop()
