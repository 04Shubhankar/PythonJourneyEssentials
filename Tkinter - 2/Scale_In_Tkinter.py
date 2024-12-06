import tkinter as tk

def scale_changed(value):
    print("Scale value:", value)

root = tk.Tk()
root.title("Scale Widget Example")

# Create a horizontal scale with various options
scale = tk.Scale(root,
                from_=0,
                to=100,
                orient=tk.HORIZONTAL,
                length=300,
                label="Adjust the value:",
                tickinterval=10,
                command=scale_changed,
                bg="lightblue",
                fg="black",
                font=("Arial", 12),
                activebackground="lightgreen",
                cursor="hand2",
                relief="raised",
                showvalue=True,
                sliderlength=20)
scale.pack()

root.mainloop()
