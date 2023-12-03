#class Student:
    #pass
#print(type(Student)) ## this is now a class

#object_1=Student()  ## creates an instance/object from this class
#object_2=Student()  ## can have as many as you like, each is an independent instance that won't alter others

#print(isinstance (object_1, Student)) # will return BOOL if this object is an instance of that class

#object_1.name= "Ryan" # the dot is what associates it with the object
#object_1.email= "ryan@notreal.com" # it is assigned to object 1, this does not effect object 2

#print(object_1.name) #as long as it has already been assigned will access it 

#object_3= Student()

# if you tried to access object_3.name will get an error as only applied to 1

#class Student:

    #name=""
    #score=0
   # active=True   #These are now some 

#s1=Student()  
#s2=Student() 

#print(s1.name,s1.score,s1.active)

#s1.name =  "Chris"  #even though it has defaults these can be changed
#s1.active=False

class fiddlesticks:
    def __init__ (self): #self refers to the object itself
        print("Init called")  # always called when object initialised

#champ1= fiddlesticks()
#champ3=fiddlesticks()


"""
class garen:
    def __init__():
        print("Initilisation called!")

lame=garen() """   #This will give an error as it will pass lame through as the arg for the function therefore error out
"""
class garen:
    def __init__(boo): <--- this would work, it doesnt care what it is, but better to use self
        print("Initilisation called!")
"""

class teacher:
    def __init__(self,first, last):
        self.first = first
        self.last = last
        #self.mail = name + "." + "@notreal.com"
        self.email = first+"." + last + "@notreal.com"
    def fullname(self):  #for any method you need self"
        return "{} {}".format(self.first, self.last)
"""
teacher1 = teacher("Stew")
print(teacher1.name)
print(teacher1.mail)

teacher1.name = "Mike"
print(teacher1.name)
print(teacher1.mail)  #<---- this will not change the name as you would think, as it is not the same object
"""
teacher1 =teacher("Jonny", "Bravo")
#print(teacher1.fullname())
teacher2 = teacher("Ryan", "Giggs")
#print(teacher.fullname(teacher1)) 

#del teacher2.first <-- will delete the first name of student 2

class competition:
   
    raise_ammount=1.04

    def __init__(self,name, prize):
        self.__name=name
        self.__prize = prize
    def get_name(self):
        return self.__name
    def get_prize(self):
        return self.__prize
    def raise_prize(self):
        self.__prize=self.__prize * competition.raise_ammount # need to reference like this or it cannot find it as it is in the class

debate = competition("debate",500)
#print(debate.raise_ammount)
#print(competition.prize) will not work as it is an instance of the class not the class itself
essay = competition("essay", 500)

#print(essay.prize)

essay.raise_prize()

#print(essay.prize)

simulation= competition("simulation", 100)

simulation.raise_prize()

#competition.raise_ammount

#simulation.raise_ammount  currently refer to same thing

#print(simulation.__dict__)
#{'name': 'simulation', 'prize': 104.0} #raise ammount and func raise prize is not part of this 

#print(competition.__dict__)
#{'__module__': '__main__', 'raise_ammount': 1.04, '__init__': <function competition.__init__ at 
# 0x7fee0d543370>, 'raise_prize': <function competition.raise_prize at 0x7fee0d543400>, '__dict__': 
# <attribute '__dict__' of 'competition' objects>, '__weakref__': <attribute '__weakref__' of 'competition' 
# objects>, '__doc__': None}

class racing (competition):
    def __init__ (self, name, prize, country):
        super().__init__(name, prize)  #<---reference the parent class competition, invokes other methods in th eparent. so will use the name prize in competition
        self.__country=country
    def get_country(self):
        return self.__country

racing= racing ("10km", 7500, "USA")
print(racing.get_country())
print(racing.get_name(),racing.get_prize())  #<-- these aren't in the racing class but the super means they pull form the parent competition










#print(competition.raise_ammount)
#print(simulation.raise_ammount) <-- changes in all as its the class that has been effected

simulation.raise_ammount = 10
#print(competition.raise_ammount,simulation.raise_ammount, racing.raise_ammount)
#1.05 10 1.05 only the simulation one has changed as its effected the object not the class

#print(simulation.__dict__)
#{'name': 'simulation', 'prize': 104.0, 'raise_ammount': 10}  <-- the raise ammount has been added as a new key

#class variables share memory#

class tournament:

    participants = []

    def __init__(self,name,prize):
            self.__name = name
            self.__prize= prize



running = tournament("running", 500)
#print(running.participants)
#[]
running.__name= "walking"
#print(running.__name)
tournament.participants.append("Jeff")
#print(tournament.participants)
#['Jeff']
running.participants.append("Alice")
#print(running.participants)
#['Jeff', 'Alice']
#print(tournament.participants)
#['Jeff', 'Alice']    <--- these have shared memory so edits to one effect the other as it si in the class

class Dog:
    """ This is a class which defines a dog
    """
    __species = "canine"

    def __init__(self,name,breed):
        self.__name=name  #the double underscore make it much harder for the variables to be changed outside of the class
        self.__breed=breed
        self.__tricks=[]

    def print_details(self):
        print("My name is %s and I am a %s" % (self.__name, self.__breed))  #these getters and setters re best practice to change variables
        print("Here are the tricks i cna do: ", (self.__tricks))

    def change_name(self,name):
        self.__name=name   #setter

    def change_breed(self,breed):
        self.__breed=breed

    def change_name_and_breed(self,name,breed):
        self.change_name(name)
        self.change_breed(breed)

    def add_tricks(self,tricks):
        self.__tricks.append(tricks)

d1 = Dog("Bingo","Labrodor")
#d1.print_details()

d1.add_tricks("Play dead")
#d1.print_details()


class student:

    def __init__(self, name, gpa):

        self.__name = name
        self.__gpa = gpa
        self.__clubs=set()
        self.__active_student=True

    def change_name(self,name):
        self.__name=name

    def change_GPA(self,gpa):
        self.__gpa=gpa

    def add_clubs(self,clubs):
        self.__clubs.add(clubs)

    def set_active_student(self, ):
        self.__active_student=True

    def print_details(self):
        print("Student: ", self.__name)
        print(self.__gpa, self.__clubs, self.__active_student)


s1 = student("Toby", 2.0)
s1.add_clubs("Swimming")

#s1.print_details()
"""
student_details_list = [
    {"name": "Nina","gpa": 3.6,"clubs": ["tennis","chess"]},
    {"name": "Emily","gpa": 3.9,"clubs":["tennis","chess"], "active":False},
    {"name": "Michael","gpa": 3.2,"clubs":["football"]},
    {"name": "Joe","gpa": 3.9,"is_honors_student":True}
]

def get_students(student_details_list):
    student_list = []

    for student_details in student_details_list:

        if "name" not in student_details or "gpa" not in student_details:
            continue
        s=student(student_details["name"], student_details["gpa"])

        if "clubs" in student_details:
            for club in student_details["clubs"]:
                s.add_clubs(club)

        if "active" in student_details:
            s.set_active_student(student_details_list["active"])

        student_list.append(s)

    return student_list


get_students(student_details_list)
"""