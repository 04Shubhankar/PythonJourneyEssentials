import tkinter as tk

def insert_text():
    text.insert("end", "This text is inserted.\n")

def delete_text():
    text.delete("1.0", "end")

def get_text():
    text_content = text.get("1.0", "end")
    print(text_content)

def see_line():
    text.see("3.0")  # Scroll to the third line

def mark_example():
    text.mark_set("my_mark", "1.0")
    text.mark_gravity("my_mark", "left")
    text.insert("my_mark", "Marked text\n")

def tag_example():
    text.tag_add("highlight", "1.0", "1.end")
    text.tag_config("highlight", background="yellow", foreground="blue")

root = tk.Tk()
root.title("Text Widget Example")

text = tk.Text(root, height=10, width=30)
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text.config(yscrollcommand=scrollbar.set)

# Insert button
insert_button = tk.Button(root, text="Insert Text", command=insert_text)
insert_button.pack()

# Delete button
delete_button = tk.Button(root, text="Delete Text", command=delete_text)
delete_button.pack()

# Get Text button
get_button = tk.Button(root, text="Get Text", command=get_text)
get_button.pack()

# See Line button
see_button = tk.Button(root, text="See Line 3", command=see_line)
see_button.pack()

# Mark Example button
mark_button = tk.Button(root, text="Mark Example", command=mark_example)
mark_button.pack()

# Tag Example button
tag_button = tk.Button(root, text="Tag Example", command=tag_example)
tag_button.pack()

root.mainloop()
