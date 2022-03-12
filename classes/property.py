class Test:
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        print("x calld!")
        return self.__x

    @x.setter
    def x(self,x):
        if x < 101:
            self.__x = x
            print(f"x value is {self.x}")
        else:
            print(f"bad value.. x value is {self.x}")

t = Test(23)
print(t.x)
t.x=100
print(t.x)