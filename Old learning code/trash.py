class Point:
    MIN_RANGE = 0
    MAX_RANGE = 100

    @classmethod
    def checkvalue(cls, arg):
        if cls.MAX_RANGE> arg > cls.MIN_RANGE:
            return True
        else: 
            print (" Value error ")  

    def __init__(self,x,y):
            self.x = x
            self.y = y

    @property
    def x(self):
         return self.__x
    @x.setter
    def x(self, x):
         print(" calling setter for X")
         self.__x = x if self.checkvalue(x) else self.MIN_RANGE

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        print(" calling setter for Y")
        self.__y = y if self.checkvalue(y) else self.MIN_RANGE

try:
     a = Point (1,-5)
except ValueError as e:
     print (e)
a.x = 3
print(a.__dict__)