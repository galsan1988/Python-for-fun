class Counter:

    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print ("__call__")
        self.__counter +=1
        return self.__counter
a= Counter()
a2 = Counter()

print(a())
a()
res =a()

print(res)