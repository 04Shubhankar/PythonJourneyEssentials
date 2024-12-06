import tkinter as tk

def on_entry_change(event):
  print("Entry content changed:", event.widget.get())

def move_cursor_to_end():
  entry.icursor("end")  # Move cursor to the end

def select_all_text():
  entry.select_range(0, tk.END)  # Select all text (0 to END)

def clear_selection():
  entry.select_clear()  # Clear current selection

def scroll_right(amount):
  entry.xview_scroll(amount, "characters")  # Scroll right by specified characters

root = tk.Tk()

# Create an entry widget with various options
entry = tk.Entry(
    root,
    bg="lightblue",
    bd=5,
    cursor="hand2",
    font=("Arial", 12, "bold"),
    exportselection=True,
    fg="green",
    highlightbackground="yellow",
    highlightcolor="red",
    highlightthickness=2,
    insertbackground="blue",
    insertborderwidth=2,
    insertontime=500,
    insertwidth=3,
    justify="left",
    relief="groove",
    selectbackground="purple",
    selectborderwidth=2,
    selectforeground="yellow",
    show="*",
    textvariable=None,
    width=30,
)

# Bind a function to the <<EntryModified>> event (corrected)
entry.bind("<<EntryModified>>", on_entry_change)

# Create buttons for cursor and selection manipulation
move_cursor_end_button = tk.Button(root, text="Move Cursor to End", command=move_cursor_to_end)
select_all_button = tk.Button(root, text="Select All", command=select_all_text)
clear_selection_button = tk.Button(root, text="Clear Selection", command=clear_selection)

# Create a button and slider for scrolling
scroll_right_button = tk.Button(root, text="Scroll Right", command=lambda: scroll_right(5))  # Scroll 5 characters
scroll_amount_slider = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=lambda value: scroll_right(int(value)))  # Scroll based on slider value

# Pack the widgets
entry.pack()
move_cursor_end_button.pack()
select_all_button.pack()
clear_selection_button.pack()
scroll_right_button.pack()
scroll_amount_slider.pack()

root.mainloop()
