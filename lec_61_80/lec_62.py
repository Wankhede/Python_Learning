class Quadilateral:
    def __init__(self, s1, s2, s3, s4):
        try:
            if type(s1) != int and type(s2) != int and type(s3) != int and type(s4) != int:
                raise TypeError("The type is not correct")
        except TypeError as e:
            print(e)

        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4

    def perimeter_rectangle(self):
        return f"The perimeter of the rectangle is :-  {(2*self.s1) + (2*self.s2)}" 
    
class Square(Quadilateral):
    def __init__(self, s):
        Quadilateral.__init__(self, s, s, s, s)
        self.s = s

    def show(self):
        return f"The passed number was {self.s}"


class Rectangle(Quadilateral):
    def __init__(self, s1, s2):
        Quadilateral.__init__(self, s1, s2)
        

def main():
    ss = Square(20)
    print(ss.perimeter())
    print(ss.show())
    print(ss.perimeter_rectangle())

main()


# Multilevel Inheritance
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
class X:
    def __init__(self, xx):
        self.x = xx

    def getx(self):
        return self.x

class Y(X):
    def __init__(self, xx, yy):
        X.__init__(self, xx)
        self.y = yy

    def gety(self):
        return self.y

class Z(Y):
    """While calling the Z class, we have to take care that all the previous constructors are also
      passed with it if its multilevel inheritance that we are following
      In case we declare it in the __init__ we have to pass it, or it will give arg error"""
    def __init__(self, xx, yy, zz):
        Y.__init__(self, xx, yy)
        self.z = zz

    def getz(self):
        return self.z

def main():
    z1 = Z(11,22,33)
    print(z1.getx())
    print(z1.gety())
    print(z1.getz())
    print(z1.__dict__)

main()

