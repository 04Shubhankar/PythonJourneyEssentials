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


class Daughter(Father):
    """
    This class represents a daughter, inheriting from the Father class.
    """

    def __init__(self):
        """
        Constructor for the Daughter class.
        Calls the constructor of the parent Father class using `super().__init__()` to initialize the inherited attributes.
        Prints a message indicating that the Daughter class constructor is called.
        """
        super().__init__()  # Calls the parent's constructor
        print("Daughter class constructor")

    def showd(self):
        """
        Instance method of the Daughter class.
        Prints a message indicating that it's an instance method of the Daughter class.
        """
        print("Daughter class method")


# Create an instance of the Daughter class
d = Daughter()

# Call the showf method inherited from the Father class
d.showf()

# Call the showd method specific to the Daughter class
d.showd()
