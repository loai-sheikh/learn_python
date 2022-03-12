class A:
    pass

class B(A):
    pass

a = A()
b = B()

print(issubclass(type(b),type(a)))
print(issubclass(B,A))
print('\n***************\n')

class Citizen:
    def __init__(self,nm):
        self.firstName = nm

    def whoIs(self):
        print('i am', self.firstName)
    
class Student(Citizen):
    def __init__(self, nm,stuid):
        Citizen.__init__(self,nm)
        self.studetId = stuid
    
    def whoIs(self):
        print('i am', self.firstName, 'i am student #', self.studetId)

s = Student("bob", 1234)
c = Citizen("loai")

print(issubclass(type(s),type(c)))
print('\n***************\n')
print(s.whoIs())
print(c.whoIs())
print('\n***************\n')

class PAPA:
    def eatHotSpice(self):
        print("mmm i love hot spice!")

class MAMA:
    def dontEatDirtyFood(self):
        print('is this dirty? i dont eat dirty food...')

class SON(PAPA,MAMA):
    pass

son = SON()
son.eatHotSpice()
son.dontEatDirtyFood()