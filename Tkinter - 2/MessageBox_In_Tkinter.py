import tkinter as tk
import tkinter.messagebox as messagebox

def show_message():
    messagebox.showinfo("Information", "This is an informational message.")

def show_warning():
    messagebox.showwarning("Warning", "This is a warning message.")

def show_error():
    messagebox.showerror("Error", "An error occurred.")

def ask_question():
    result = messagebox.askquestion("Question", "Do you want to continue?")
    if result == 'yes':
        print("User clicked Yes")
    else:
        print("User clicked No")

root = tk.Tk()
button1 = tk.Button(root, text="Show Info", command=show_message)
button2 = tk.Button(root, text="Show Warning", command=show_warning)
button3 = tk.Button(root, text="Show Error", command=show_error)
button4 = tk.Button(root, text="Ask Question", command=ask_question)
button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()
