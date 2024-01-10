"""
https://www.codewars.com/kata/5263c6999e0f40dee200059d

The keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit 
(horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could
 also be the 2, 4, 6 or 8.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array
of all variations for an observed PIN with a length of 1 to 8 digits.
  We could name the function getPINs (get_pins in python). But please note that all PINs,
   the observed one and also the results, must be strings, because of potentially leading '0's.
 """
import itertools

def get_pins(observed):

    One="124"
    Two="1235"
    Three= "236"
    Four="1457"
    Five="24865"
    Six="6359"
    Seven="478"
    Eight="87590"
    Nine="968"
    Zero="08"

    possible_list=[]

    for nums in observed:
        if nums =="1":
            possible_list.append(One)
            
        elif nums =="2":
            possible_list.append(Two)
            
        elif nums =="3":
            possible_list.append(Three)
            
        elif nums =="4":
            possible_list.append(Four)
            
        elif nums =="5":
            possible_list.append(Five)
            
        elif nums =="6":
            possible_list.append(Six)
            
        elif nums =="7":
            possible_list.append(Seven)
            
        elif nums =="8":
            possible_list.append(Eight)
            
        elif nums =="9":
            possible_list.append(Nine)
            
        elif nums =="0":
            possible_list.append(Zero)
            

    if len(observed)==1:
        result=list(itertools.product(possible_list[0]))
    elif len(observed)==2:
        result=list(itertools.product(possible_list[0],possible_list[1]))
    elif len(observed)==3:
        result=list(itertools.product(possible_list[0],possible_list[1],possible_list[2]))
    elif len(observed)==4:                
        result=list(itertools.product(possible_list[0],possible_list[1],possible_list[2],possible_list[3]))
    elif len(observed)==5:                
        result=list(itertools.product(possible_list[0],possible_list[1],possible_list[2],possible_list[3],possible_list[4]))
    elif len(observed)==6:                
        result=list(itertools.product(possible_list[0],possible_list[1],possible_list[2],possible_list[3],possible_list[4],possible_list[5]))
    elif len(observed)==7:                
        result=list(itertools.product(possible_list[0],possible_list[1],possible_list[2],possible_list[3],possible_list[4],possible_list[5],possible_list[6]))
    elif len(observed)==8:                
        result=list(itertools.product(possible_list[0],possible_list[1],possible_list[2],possible_list[3],possible_list[4],possible_list[5],possible_list[6],possible_list[7]))    
    
    pre_answer=""
    answer=[]
    count=0

    for pins in result:

        for nums in pins:
            pre_answer=pre_answer+nums
            count +=1
            if count==len(pins):
                count=0
                answer.append(pre_answer)
                pre_answer=""
        
    return answer
print(get_pins("11"))


        

#--> what have [('1', '1', '2', '1'), ('1', '1', '2', '4')]
#-->target ["1121","1124"]

"""
Best:

from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]





"""