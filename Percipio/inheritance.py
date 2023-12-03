##-----------------------------------------------------------------------------------------##
""" Shows how multiple inheritence works"""

class Father:
    def height (self):
        print("I have inherited my height from my father")

class Mother:
    def intelligence(self):
        print("I have inherited my intelligence from my mother")

class child(Father, Mother): #<-- does mean will go through father firsth then mother 
    def experience(self):
        print("My experience is my own")

c= child()
c.height()
c.intelligence()
c.experience()
#---------------------------------------------------------------------------------------------------------------#


class employee:

    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def show_name(self):
        print(self.__name)

    def show_age(self):
        print(self.__age)

class Salary:
    def __init__(self,salary):
        self.__salary=salary

    def get_salary(self):
        print(self.__salary)

class database(employee,Salary):

    def __init__ (self, name, age, salary):

        employee.__init__(self,name,age)
        Salary.__init__(self,salary)
    
employ = database("Robin", 26, 26000)

employ.show_name()
employ.show_age()
employ.get_salary()

#----------------------------------------------------------------------------------------#
""" Multi level inheritance"""

class grandparet:

    def smile(self):
        print ("Smile inherited from Grandparent")

class parent(grandparet):

    def weight(self):
        print( "weight inherited from parent")

class children(parent):

    def basketball(self):
        print("My basketball is my own")

c=children()
c.smile()
c.weight()
c.basketball()

#---------------------------------------------------------------------------------------------#

class grandad(object):

    def __init__ (self, city):
        self.__city=city

    def get_city(self):
        return self.__city

class dad(grandad):

    def __init__(self,city, lastname):
        grandad.__init__(self,city)

        self.__lastname=lastname

    def get_lastname(self):
        return self.__lastname
    
p1 = dad(city="cardiff", lastname="Jacobs")
print(p1.get_city())

class Person(dad):
    
    def __init__ (self, city, lastname, firstname):
        dad.__init__(self, city, lastname)

        self.__firstname=firstname

    def get_firstname(self):
        return self.__firstname
    
    def get_introduction(self):
        lastname= super().get_lastname()
        city= super().get_city()

        print("Hi I am %s %s from %s" % (self.__firstname, lastname, city))

    def get_information(self):
        lastname=self.get_lastname()
        city=self.get_city()

        print("Hi I am %s %s form %s" % (self.__firstname,lastname, city))
    

C1=Person("Swansea", "Williams", "Dai")
print(C1.get_city())
print(C1.get_firstname())
print(C1.get_introduction())
print(C1.get_information())

#-------------------------------------------------------------------------------------------------#
""" Polymorphism"""

class BankAccount:

    def __init__(self, balance):

        self.__balance=balance
    
    def deposit(self,value):

        self.__balance= self.__balance + value

        print("Deposit ammount: ", value)
        print("Balance after depositing: ", self.__balance)

    def withdraw(self,value):

        self.__balance = self.__balance - value

        print("Withdrawal ammount: ", value)
        print("Balance after withdrawal: ", self.__balance)

b1 = BankAccount(1500)
b1.deposit(100)
b1.withdraw(200)

class CurrentAccount (BankAccount):

    def __init__ (self, balance):
        super().__init__(balance) #<-- pulls the balance init from parent

    def withdawal (self, value):
        if value>1000:
            print("Contact bank manager")
        else:
            super().withdrawal(value) #<--- invokes the normal withdraw form the parent 

b2 = CurrentAccount(2000)
b2.deposit(100)
b2.withdawal(1100)