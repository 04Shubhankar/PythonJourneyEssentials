class IOString():
    def __init__(self):
        self.stri = ""

    def get_String(self):
        self.stri = input("Enter a String -->")

    def print_String(self):
        print(self.stri.upper())

str1 = IOString()
str1.get_String()
str1.print_String()
