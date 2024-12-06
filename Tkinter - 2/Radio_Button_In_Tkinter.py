import tkinter as tk

def select_option():
    print(var.get())

root = tk.Tk()
root.title("Radio Button Example")

var = tk.StringVar()

# Create Radio Buttons with different options
radio1 = tk.Radiobutton(root,
                        text="Option 1",
                        variable=var,
                        value="1",
                        command=select_option,
                        bg="lightblue",
                        fg="black",
                        font=("Arial", 12),
                        activebackground="lightgreen",
                        activeforeground="darkgreen",
                        cursor="hand2",
                        relief="raised",
                        padx=10,
                        pady=5)
radio1.pack()

radio2 = tk.Radiobutton(root,
                        text="Option 2",
                        variable=var,
                        value="2",
                        command=select_option,
                        bg="lightgreen",
                        fg="black",
                        font=("Arial", 12),
                        activebackground="lightblue",
                        activeforeground="darkblue",
                        cursor="hand2",
                        relief="sunken",
                        padx=10,
                        pady=5)
radio2.pack()

radio3 = tk.Radiobutton(root,
                        text="Option 3",
                        variable=var,
                        value="3",
                        command=select_option,
                        bg="lightpink",
                        fg="black",
                        font=("Arial", 12),
                        activebackground="lightcoral",
                        activeforeground="darkred",
                        cursor="hand2",
                        relief="flat",
                        padx=10,
                        pady=5)
radio3.pack()

root.mainloop()
