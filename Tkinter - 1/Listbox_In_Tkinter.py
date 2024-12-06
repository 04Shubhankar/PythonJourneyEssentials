import tkinter as tk

root = tk.Tk()

# Create a listbox with various options
listbox = tk.Listbox(
    root,
    bg="lightblue",
    bd=5,
    cursor="hand2",
    font=("Arial", 12, "bold"),
    fg="green",
    height=5,
    highlightcolor="red",
    highlightthickness=2,
    relief="groove",
    selectbackground="purple",
    selectmode="single",
    width=20
)

# Insert items into the listbox
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.insert(tk.END, "Item 3")

# Bind a function to the <<ListboxSelect>> event
def on_listbox_select(event):
    selected_index = listbox.curselection()
    selected_item = listbox.get(selected_index)
    print("Selected item:", selected_item)

listbox.bind("<<ListboxSelect>>", on_listbox_select)

# Pack the listbox into the root window
listbox.pack()

root.mainloop()
