class Father:
    """
    This class represents a father.
    """

    def __init__(self):
        """
        Constructor for the Father class.
        Prints a message indicating that the Father class constructor is called.
        """
        print("Father class constructor")

    def show(self):
        """
        Instance method of the Father class.
        Prints a message indicating that it's an instance method of the Father class.
        """
        print("Father class instance method")


class Son(Father):
    """
    This class represents a son, inheriting from the Father class.
    """

    def __init__(self):
        """
        Constructor for the Son class.
        Calls the constructor of the parent Father class using `super().__init__()` to initialize the inherited attributes.
        Prints a message indicating that the Son class constructor is called.
        """
        super().__init__()  # Calls the parent's constructor
        print("Son class constructor")

    def disp(self):
        """
        Instance method of the Son class.
        Prints a message indicating that it's an instance method of the Son class.
        """
        print("Son class instance method")


# Create an instance of the Son class
s = Son()

# Call the disp method of the Son class
s.disp()

# Call the show method inherited from the Father class
s.show()
