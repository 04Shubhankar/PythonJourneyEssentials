import tkinter as tk

def on_value_change(new_value):
    print("New value:", new_value)

root = tk.Tk()

spinbox = tk.Spinbox(
    root,
    from_=0,
    to=100,
    increment=10,
    width=10,
    justify='center',
    font=('Arial', 12),
    fg='blue',
    bg='lightgray',
    bd=2,
    relief='sunken',
    cursor='hand2',
    state='normal',
    textvariable=tk.StringVar(),
    validate='all',
    validatecommand=(root.register(lambda P: True), '%P'),
    values=('0', '25', '50', '75', '100'),
    command=on_value_change
)

spinbox.pack(pady=20)

root.mainloop()
