#func input
#func work out
#func 4 int
#func 4 str
#func 4 bool

def user_input(test):
    first_input=test
    work_out(bork=first_input, dork= "Lemon!")
    

def work_out(bork, dork):
    #variable = bork
    if type(bork) == int:
        int_func()
    if type(bork) == str:
        str_func()
    if type(bork) == bool:
        bool_func()
    print(dork)
def int_func():
    print("This is an int!")

def str_func():
    print("This is a string!")

def bool_func():
    print("This is a bool!")

def test_func():

    my_test = [3030, 450, "String", True, "Golf", 67]
    for i in my_test:
        user_input(i)
    
    #user_input(3030)
    #user_input("I am a string")
    #user_input(True)
    #user_input("I am a string")    
    #user_input(True)
    #user_input(3030)




test_func()