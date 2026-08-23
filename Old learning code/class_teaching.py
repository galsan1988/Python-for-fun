class Shape:
    """Class for Shapes"""

    # monoinstance = {
    #     'color': 'red',
    #     'size':3,
    #     'shape':  "circle",
    # }
    # def __init__(self):
    #     self.__dict__ = self.monoinstance

    __color = 'black'
    size = 3
    shape = 'circle'


    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
 
    def __del__(self):
        # print ("deleting obj of Class Shape, ID is ", id(self))
        Shape.__instance = None

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x,self.y)

    @property
    def color(self):
        return self.__color
    @color.setter
    def color (self, color):
        self.__color = color
    @color.deleter
    def color(self):
        del self.__color



    # color = property(get_color,set_color)
    # color = property()
    # color = color.se

        
Shape.thickness = 5 #creating new attribute of class

first_circle = Shape() #new obj 
first_circle.color = 'Pink'# setting attribute for an object
print(first_circle.color)
# setattr(first_circle, 'x', 5.5)
# print (first_circle.__dict__)
# print (Shape.__dict__)


first_circle.color ='Purple' #using property object setter
print (first_circle.color) #using property object getter
print (first_circle.__dict__)
del first_circle.color
print (first_circle.color)
print (first_circle.__dict__)



# print (first_circle.__class__)
# print (Shape.__class__)
# print (Shape.__dict__)
# print('***' * 20)

# print(first_circle.__getattribute__('size'))
# print(getattr(first_circle, 'color'))
# print(getattr(Shape, 'color'))
# print (getattr(first_circle, 'x'))

# print (hasattr(first_circle, 'id'))

# setattr(first_circle, 'newattr', 'not really')
# print(first_circle.__dict__)
# delattr(first_circle, 'newattr')
# print(first_circle.__dict__)
# print(first_circle.__doc__)

# print(first_circle.get_coords())
# f = getattr(first_circle, 'get_coords')
# print(f())

