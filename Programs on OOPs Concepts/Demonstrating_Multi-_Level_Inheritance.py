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

    def showf(self):
        """
        Instance method of the Father class.
        Prints a message indicating that it's an instance method of the Father class.
        """
        print("Father class method")


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

    def shows(self):
        """
        Instance method of the Son class.
        Prints a message indicating that it's an instance method of the Son class.
        """
        print("Son class method")


class Grandson(Son):
    """
    This class represents a grandson, inheriting from the Son class.
    """

    def __init__(self):
        """
        Constructor for the Grandson class.
        Calls the constructor of the parent Son class using `super().__init__()` to initialize the inherited attributes.
        Prints a message indicating that the Grandson class constructor is called.
        """
        super().__init__()  # Calls the parent's constructor
        print("Grandson class constructor")

    def showg(self):
        """
        Instance method of the Grandson class.
        Prints a message indicating that it's an instance method of the Grandson class.
        """
        print("Grandson class method")


# Create an instance of the Grandson class
g = Grandson()

# Call the showf method inherited from the Father class
g.showf()

# Call the shows method inherited from the Son class
g.shows()

# Call the showg method specific to the Grandson class
g.showg()
