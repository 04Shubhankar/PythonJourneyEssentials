import tkinter as tk

root = tk.Tk()

paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL)

left_pane = tk.Label(paned_window, text="Left Pane", bg="lightblue")
right_pane = tk.Label(paned_window, text="Right Pane", bg="lightgreen")

paned_window.add(left_pane)
paned_window.add(right_pane)

paned_window.pack(fill=tk.BOTH, expand=True)

root.mainloop()
