#Given a positive integer of up to 16 digits, return true if it is a valid credit card number, and false if it is not.
#Double every other digit, scanning from right to left, starting from the second digit (from the right).
#Another way to think about it is: if there are an even number of digits, double every other digit starting with the
#first; if there are an odd number of digits, double every other digit starting with the second:

#If a resulting number is greater than 9, replace it with the sum of its own digits (which is the same as subtracting 9 from it):


#Finally, take that sum and divide it by 10. If the remainder equals zero, the original credit card number is valid.

def validate(num):
    result=[]
    result_second=[]
    result_pre=[]
    spare_listy=[]
    even_listy=[]
    test = str(num)
    #print(len(test))
    if len(test) %2 ==0:
        listy = list(str(num))
        even_listy= listy[0::2]
        spare_listy=listy[1::2]
        print(spare_listy)
        for i in spare_listy:
            result.append(int(i))
            print(even_listy)
        for i in even_listy:
            result.append(int(i)*2)
            print(result)

    if len(test) %2 !=0:
        listy = list(str(num))
        even_listy= listy[1::2]
        spare_listy=listy[0::2]
        print(spare_listy)
        for i in spare_listy:
            result.append(int(i))
        for i in even_listy:
            result.append(int(i)*2)
            print(result)
    for i in result:
        if i >9:
            result_second.append(i-9)
        else:
            result_second.append(i)
            print(result_second)

    final = sum(result_second)%10
    print(sum(result_second))
    print(final)
    if final ==0:
        print (True)
        return True
    else:
        print (False)
        return False
      

print(validate(69807033941))

