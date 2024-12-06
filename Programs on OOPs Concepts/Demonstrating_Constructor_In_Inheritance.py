#Demonstrating Constructor in Inheritance

class Father:
    def __init__(self):
        self.money = 1000
        print("Father class constructor")

    def show(self):
        print("Father class instance method")

class Son(Father):
    def disp(self):
        print("Son class constructor")

s = Son()
s.disp()
print("Father instance variables: ", s.money)
s.show()
