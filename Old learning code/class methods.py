# __add__()
# __radd__()
# __iadd__()

# __str__()
# __repr__()
# __len__()
# __abs__()

# __call__()

# descriptor /data-descriptor
# @property
# monostatus


class User:
    def __init__(self, name, age):
        print ("created one user")
        self.__name = name
        self.__age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if 0<age<100:
            self.__age = age
        else:
            print ("unavailable age number")

    def get_age(self):
        print (self.__age)


abc = User("Galsan", 38)
print(abc._User__name)
abc.age=48
abc.get_age()