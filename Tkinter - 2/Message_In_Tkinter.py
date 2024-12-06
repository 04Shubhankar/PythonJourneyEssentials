import tkinter as tk

def create_message_widget():
    root = tk.Tk()
    root.title("Message Widget Example")

    # Create a Message widget with multi-line text and formatting
    message_text = """
    This is a multi-line message displayed using the Message widget.
    You can customize the appearance and behavior of the text using various options.
    For example, you can set the font, color, alignment, and wrapping.
    """
    message = tk.Message(root, text=message_text,
                         font=("Arial", 12),
                         bg="lightblue",
                         fg="black",
                         width=300,
                         justify="center",
                         relief="sunken",
                         padx=10,
                         pady=10)
    message.pack()

    root.mainloop()

if __name__ == "__main__":
    create_message_widget()
