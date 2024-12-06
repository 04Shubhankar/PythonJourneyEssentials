class Father:
    """
    This class represents a father.
    """

    def __init__(self):
        """
        Constructor for the Father class.
        Initializes the money attribute to 1000.
        """
        self.money = 1000
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
        Calls the constructor of the parent Father class to initialize the money attribute.
        Sets the car attribute to "BMW".
        """
        super().__init__()  # Calls the parent's constructor
        self.car = "BMW"
        print("Son class constructor")

    def disp(self):
        """
        Instance method of the Son class.
        Prints a message indicating that it's an instance method of the Son class.
        """
        print("Son class instance method")


# Create an instance of the Son class
s = Son()

# Print the value of the money attribute inherited from the Father class
print(s.money)

# Print the value of the car attribute specific to the Son class
print(s.car)

# Call the disp method of the Son class
s.disp()
