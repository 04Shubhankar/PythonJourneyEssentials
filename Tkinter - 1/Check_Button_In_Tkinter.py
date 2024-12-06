import tkinter as tk

def checkbutton_clicked():
    print("Checkbutton clicked!")

root = tk.Tk()

# Create a checkbutton with various options
checkbutton = tk.Checkbutton(
    root,
    text="Check me",
    command=checkbutton_clicked,
    activebackground="yellow",
    activeforeground="blue",
    bg="lightblue",
    bitmap="error",
    bd=5,
    cursor="hand2",
    disabledforeground="gray",
    font=("Arial", 12, "bold"),
    fg="green",
    height=2,
    highlightcolor="red",
    image=None,  # You can set an image here
    justify="left",
    offvalue=False,
    onvalue=True,
    padx=10,
    pady=5,
    relief="groove",
    selectcolor="purple",
    selectimage=None,  # You can set an image here
    state="normal",
    underline=0,
    variable=None,  # You can associate a variable
    width=20,
    wraplength=150
)

checkbutton.pack()

root.mainloop()
