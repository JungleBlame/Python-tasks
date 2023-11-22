#class shape:
    #pass

#class shape():
    #pass

#class shape(object): # shape inherits form object as standard
    #pass  <- all 3 valid

class shape:

    def __init__ (self, shapeType,color="red"):
        self.__type=shapeType
        self.__color=color

    def get_type(self):
        return self.__type
    
    def get_color(self):
        return self.__color
    
    def get_area(self):
        pass

    def get_perimeter(self): # <----if you wanted to work it out for square, cirlce, triangle would need different formulaes in the function
        pass
    
#circle= shape("circle")
#print(circle.get_color)
#print(type(circle)) <class '__main__.shape'>
#square=shape("square")

#class circle(shape): #<-- inherits from shape
    #pass

#circle = circle() wouldnt work as the init of the shape require args to work

#circle = circle("circle")
#type(circle)

#square = square("square")
#type(square)

#class circle(shape):
    #def __init__(self, color="green"): #<--- will enter this as a color so no longer will be default red
        #shape.__init__(self, "circle",color) # <-- need to tell it to take the color 

#class square(shape): # <--- doesnt mention color so will get default red from shape
    #def __init__(self):
        #shape.__init__(self, "square")

#circle=circle("yellow") # overwrites what we set
#square=square()

#print(circle.get_color())
#print(square.get_color())

import math

class circle (shape):
    def __init__(self, radius):
        shape.__init__(self,"circle")

        self.__radius=radius
    def get_area(self):
        return math.pi *self.__radius * self.__radius
    def get_perimeter (self):
        return 2* math.pi *self.__radius
    
c= circle(10)

print(c.get_area())

class square (shape):
    def __init__(self, side):
        shape.__init__(self,"square")

        self.__side=side

    def get_area(self):
        return self.__side * self.__side
    def get_perimeter (self):
        return 4* self.__side
    
s= square(10)

print(s.get_area())