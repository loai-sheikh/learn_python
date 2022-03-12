class MyClass:
    def __init__(self):
        self.x = "public"
        self._x = "protected"
        self.__x= "private"

    def print__x(self):
        print(self.__x)

c = MyClass()
c.print__x()
