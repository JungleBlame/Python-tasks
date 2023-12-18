#__init__    whenever object is initialised applies whatever is after the init

# __repr__   determines how somehting is represented when you print something out

class Competition:

    def __init__(self,name, prize):
        self.__name=name
        self.__prize=prize

    def __repr__(self):
        return "('{}', {})".format(self.__name, self.__prize)  #so print like ' ' have these<- {} replace with the format things

archery = Competition("Archery", 8000)
print(archery) #->('Archery', 8000) rather than "('Archery', 8000)"

#__add__ can add int together. Basically same as +

class Savings:
    def __init__(self,ammount):
        self.__ammount= ammount
    def __add__(self,other):
        return self.__ammount + other.__ammount #<--- without this if you put just s1+s2 it would error saying cannot use with this type
                            # ^ is important as whatever you have here is what Python will do even if it is different and act on it as sub 
s1 = Savings(10000)
s2 = Savings (2000)

print(s1 + s2)

# Would be same for __sub__ for subtract or -
# Same for __mul__ or * But normally __mul__ requires a float not a int

class Savings:
    def __init__ (self, amount):
        self.__amount=amount
    def __add__(self,other):
        return self.__amount + other.__amount
    
    def __mul__ (self,other):
        if type(other) == int or type(other) ==float:  #<-- won't allow you to * savings with savings as savings is not a int or float itslef but will allow s1*5 for example 
            return self.__amount*other
        else:
            raise ValueError("Can only multiply by int of float")
        

#__floordiv__ for floor division

class mthodFloor:
    def __init__(self, number):
        self.__number = number
    def __floordiv__ (self,other):
        return self.__number // other.__number
    
num1= mthodFloor(10)
num2= mthodFloor(3)

print(num1//num2)

# same for the modulo %  __mod__ int.__mod__(5,2)

#__pow__ for method od powers to 

#str.__len__() gives length of strings

#__iter__ want to eb able to resturn an itrable result 
# in order to be an iterator it needs to respond to __next__

class Participants:

    def __init__(self):
        self.__participants = []
        self.__index=0

    def add_participants(self,name):
        self.__participants.append(name)
    
    def __len__(self):
        return len(self.__participants)
    
    def __iter__ (self):
        self.__index=0
        return self
    def __next__(self):
        if self.__index == len(self.__participants):
            raise StopIteration
        p= self.__participants[self.__index]

        self.__index +=1

        return p 
    
par = Participants()

par.add_participants("Ryan")
par.add_participants("Tomos")
par.add_participants("Jack")
par.add_participants("Bleddyn")
par.add_participants("Rhys")

for p in par:
    print(p)

    #iter() will show th iterable
    #next() will call the next of whatever is in the list
    # you will need to reset the index to cycle back through hense, index = 0 in the class

    class Wrestler:

        def set_name(self,name):
            self.__name=""

        
        def set_name(self, name):
            print("Setter method called")
            self.__name=name

       
        def get_name(self):
            print("Getter method called")
            return self.__name
        
        
        def del_name(self):
            print(" delter method called")

            del self.__name

        name = property (get_name, set_name, del_name)

w= Wrestler()
w.name = "Steve"
print(w.name)

