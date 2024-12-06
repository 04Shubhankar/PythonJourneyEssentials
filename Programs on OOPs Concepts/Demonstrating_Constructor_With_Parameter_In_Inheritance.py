class Father:
    def __init__(self, m):
        self.money = m
        print("Father class constructor")

    def show(self):
        print("Father class instance method")

class Son(Father):
    def disp(self):
        print("Son class Instance method")

s = Son(1000)
s.disp()
print("Father instance variable: ", s.money)
s.show()
