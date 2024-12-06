def program1():
    """This function creates a new text file named 'intro.txt' and writes user-entered text to it."""

    f = open("intro.txt", "w")  # Opens a file named 'intro.txt' in write mode
    txt = input("Enter the text: ")  # Takes user input and stores it in the 'txt' variable
    f.write(txt)  # Writes the content of 'txt' to the file
    f.close()  # Closes the file

program1()  # Calls the 'program1' function to execute the code
