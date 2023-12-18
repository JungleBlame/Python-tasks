"""
In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore
"""

def alphanumeric(password):
    characters= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7", "8","9","0"]

    password= password.lower()

    for i in password:
        if i not in characters:
            return False
        
    if " " in password:
        return False
    
    if "_" in password:
        return False
    
    elif len(password)>=1:
        return True
    else:
        return False
    
print(alphanumeric("Hi")) #<-False
"""
Could have been done easier with the isalnum string method:

Definition and Usage
The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).

Example of characters that are not alphanumeric: (space)!#%&? etc.
"""