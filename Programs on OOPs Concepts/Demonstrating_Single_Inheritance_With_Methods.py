#Demonstrating Single Inheritance with methods


class Father:
    money = 1000

    def show(self):
        print("Parent class Instance method")

    @classmethod
    def showmoney(cls):
        print("Parent class class method")

    @staticmethod
    def stat():
        a = 10
        print("Parent class static method")

class Son(Father):
    def disp(self):
        print("Child class Instance method")

s = Son()
s.disp()
s.show()
s.showmoney()
s.stat()
