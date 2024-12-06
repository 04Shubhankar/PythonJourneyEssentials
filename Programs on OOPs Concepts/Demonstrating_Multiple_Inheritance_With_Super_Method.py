class Father:
    """
    This class represents a father.
    """

    def __init__(self):
        """
        Constructor for the Father class.
        Calls the constructor of the parent class (if any) using `super().__init__()`.
        Prints a message indicating that the Father class constructor is called.
        """
        super().__init__()  # Calls the parent's constructor (if any)
        print("Father class constructor")

    def showf(self):
        """
        Instance method of the Father class.
        Prints a message indicating that it's an instance method of the Father class.
        """
        print("Father class method")


class Mother:
    """
    This class represents a mother.
    """

    def __init__(self):
        """
        Constructor for the Mother class.
        Calls the constructor of the parent class (if any) using `super().__init__()`.
        Prints a message indicating that the Mother class constructor is called.
        """
        super().__init__()  # Calls the parent's constructor (if any)
        print("Mother class constructor")

    def showm(self):
        """
        Instance method of the Mother class.
        Prints a message indicating that it's an instance method of the Mother class.
        """
        print("Mother class method")


class Son(Father, Mother):
    """
    This class represents a son, inheriting from both the Father and Mother classes.
    """

    def __init__(self):
        """
        Constructor for the Son class.
        Calls the constructors of both parent classes using `super().__init__()` to initialize the inherited attributes.
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


# Create an instance of the Son class
s = Son()

# Call the showf method inherited from the Father class
s.showf()

# Call the showm method inherited from the Mother class
s.showm()

# Call the shows method specific to the Son class
s.shows()
