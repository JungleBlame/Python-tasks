#print(variable)

try:
    print(variable)
except NameError:
    print("'variable' was not defined")
except:
    print("Unknown error occured")

try:    
    f = open("nonexistantfile")
except FileNotFoundError:
    print("No such file")
except:
    print("Unknown error occured")
finally:  ## will always happen even if happens succesfully, can have just after try no need for except
    #file.close() useful for file functions to ensure it is closed 
    print("This is all over now")
                                    #if there are multiple exceptions there is a hierarchy

attempts = 0
while True:
    try:
        input_var = input ("Please enter a number")
        input_var = int(input_var)
        break
    except ValueError:
        attempts+=1
        if attempts<3:
            print("Thats not a number dummy")
        else:
            print("Fine be a string")
            input_var= str(input_var)
            print(input_var)
            break

import time

try:
    time.sleep111 # pauses code for that ammount of seconds
except KeyboardInterrupt:
    print("You have no patience")
else: # else will oly happen if no exceptoions have been raised
    print("Wow you are bored")


try:
    a = str(5)
    b= str("Hi")
    c="world"
    d = a+b+c

except TypeError:
    print("Type error")
except NameError:
    print("Name error")
except ValueError:
    print("Value error")
except:  ## good practice to have a catch all 
    print("I don't know you figure it out")


number = int(input("Enter a num"))
try:
    if number >5:
        raise Exception("The number {} is too big".format(number)) # raises a custom exception for this condition
except Exception as error:
    print("Caught this error: " + repr(error))

