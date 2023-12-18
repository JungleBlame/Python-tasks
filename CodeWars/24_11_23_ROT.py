""" ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13
 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be 
returned as they are. Only letters from the latin/english alphabet should be shifted, 
like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""

def rot13(message):

    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    index=0
    result=""

    for char in message:
        new_char=""
        if char.lower() in alphabet:
            index=alphabet.index(char.lower())
            index= index+13
            new_char=alphabet[index]
            #print(new_char)
            if char==char.upper():
                result+=new_char.upper()
            elif char==char.lower():
                result+=new_char.lower()

        else:
            result+= char

    return result

#rot13("Test") #<--'grfg' expected
"""
Your job is to write a function which increments a string, to create a new string.
If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""

def increment_string(strng):
    number_check =["1","2","3","4","5","6","7", "8","9","0"]
    num=""
    result=""
    zero_check=["1","2","3","4","5","6","7", "8","9"]
    
    if strng[-1:] in number_check:
        num_new=""
            
        for char in strng:
            if char in number_check:
               num+=char
            else:
                continue
                
        if num in zero_check:
            for i in num:
                if int(i) ==0:
                    continue
                elif int(i) >0:
                    num_new=num[int(i)+1:]
                    break
            
            num_new=int(num)+1
            #result=num_new

            for char in strng:
                if char not in number_check:
                    result+=char

                elif char in number_check:
                    if char =="0":
                        result+=char
                    else:
                        break   
        else:
                
            endnum=num[:-1]
            endnum=int(endnum)+1
            final_num= num[0:-1]
            print(final_num)
            num_new=str(final_num) + str(endnum)
            print(num_new)

            for char in strng:
                if char not in number_check:
                    result+=char
                    
                             
            
        result= result+str(num_new)


    elif strng[:-1] not in number_check:
         result= strng +"1"


    return result

print(increment_string("foobar001"))
