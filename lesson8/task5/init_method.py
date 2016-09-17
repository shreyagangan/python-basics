class Square:

    def __init__(self):    # special method __init__
        self.sides = 4

square = Square()
print(square.sides)

class Car:
    def __init__(self,color):
        self.color = color

car = Car("blue")    # Note: you should not pass self parameter explicitly, only color parameter

print(car.color)


#__init__ function is used to initialize the objects it creates.
#init is short for "initialize".
#__init__() always takes at least one argument, self, which refers to the object being created.
#__init__() function sets up each object the class creates.
#Add parameters to the Car class so we can create it with a specific color.
