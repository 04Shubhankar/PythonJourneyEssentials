import tkinter as tk

root = tk.Tk()
root.title("Scrollbar Example")

# Create a Text widget with a vertical Scrollbar
text = tk.Text(root, height=10, width=30)
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Link the Text widget and Scrollbar
text.config(yscrollcommand=scrollbar.set)

root.mainloop()
