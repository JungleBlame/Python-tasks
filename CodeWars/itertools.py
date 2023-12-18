#ROT 13
def rot13(message):

    alphabet_lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alphabet_upper=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    result=""
    index=0

    for char in message:
        if char in alphabet_upper:
            index= alphabet_upper.index(char)
            index=index+13
            char=alphabet_upper[index]
            #print(char)
            result=result+char
            #print(result)

        elif char in alphabet_lower:
            index= alphabet_lower.index(char)
            index=index+13
            char=alphabet_lower[index]
            #print(char)
            result=result + char
            #print(result)

        else:
            result=result + char

    return result
    
    #print (alphabet_upper)


#print(rot13("EBG13 rknzcyr."))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

"""
Task
Write a function that accepts battlefield string and returns letters that survived the nuclear strike.

The battlefield string consists of only small letters, #,[ and ].
The nuclear shelter is represented by square brackets []. The letters inside the square brackets represent letters inside the shelter.
The # means a place where nuclear strike hit the battlefield. If there is at least one # on the battlefield, all letters outside of shelter die.
 When there is no any # on the battlefield, all letters survive (but do not expect such scenario too often ;-P ).
The shelters have some durability. When 2 or more # hit close to the shelter, the shelter is destroyed and all letters inside evaporate. 
The 'close to the shelter' means on the ground between the shelter and the next shelter (or beginning/end of battlefield). The below samples make it clear for you.

abde[fgh]ijk     => "abdefghijk"  (all letters survive because there is no # )
ab#de[fgh]ijk    => "fgh" (all letters outside die because there is a # )
ab#de[fgh]ij#k   => ""  (all letters dies, there are 2 # close to the shellter )
##abde[fgh]ijk   => ""  (all letters dies, there are 2 # close to the shellter )
##abde[fgh]ijk[mn]op => "mn" (letters from the second shelter survive, there is no # close)
#ab#de[fgh]ijk[mn]op => "mn" (letters from the second shelter survive, there is no # close)
#abde[fgh]i#jk[mn]op => "mn" (letters from the second shelter survive, there is only 1 # close)
[a]#[b]#[c]  => "ac"
[a]#b#[c][d] => "d"
[a][b][c]    => "abc"
##a[a]b[c]#  => "c"


if "[" in battlefield:
        safe_start=battlefield.index("[")
        safe_end=battlefield.index("]")
        shelter= battlefield[safe_start:safe_end]
"""

def alphabet_war(battlefield):
    if "#" not in battlefield:
        return battlefield.replace("[", "").replace("]", "")
    shelters = []
    in_shelter = False
    for el in battlefield:
        if el == '[':
            in_shelter = True
            shelter = []
        elif el == "]":
            in_shelter = False
            shelters.append("".join(shelter))
        else:
            if in_shelter:
                shelter.append(el)
            elif el == "#":
                shelters.append(el)
    for i, trio in enumerate(zip(shelters, shelters[1:], shelters[2:])):
        if trio[1] == '#' and trio[2] == '#':
            shelters[i] = ''
        elif trio[0] == '#' and trio[2] == '#':
            shelters[i+1] = ''
        elif trio[0] == '#' and trio[1] == '#':
            shelters[i+2] = ''
    survivers = "".join(shelters).replace('#', "")
    return survivers

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
"""
To get the outcome,
First, cross out all letters the names have in common.
Second, remove the cross out letter on both names.
Third, get the count of the characters that are left.
Fourth, given the word FLAMES, with each letter, starting from the left, count up to the number you got in the previous step and return to the F on the left with each pass.
Finally, the letter you land on has a word that it stands for in the acronym 'flames'.

    F = Friendship
    L = Love
    A = Affection
    M = Marriage
    E = Enemies
    S = Siblings

    Example of FLAMES Game Given names are NEIL and MAE, respectively.

E is common on NEIL and MAE.
Removing E from NEIL and MAE, will left NIL and MA on both names, respectively
NIL have 3 characters and MA have 2 characters, a total of 5 characters
FLAMES --> 1>F 2>L 3>A 4>M 5>E
E stands for "Enemies"
NEIL and MAE are enemies
"""
def loopy(num):

    FLAMES= ["F","L","A","M","E","S"]
    index=0
    result=""

    while num !=0:
        if index>5:
            index=0

        result=FLAMES[index]

        index+=1
        num-=1

    return result


def show_relationship(male, female):
    
    for char in male.upper():
        if char in female.upper():
            male=male.replace(char,"")
            female=female.replace(char,"")

    male_listy=list(male)
    female_listy=list(female)
    length=0
    length= len(male_listy) + len(female_listy) 
    #print(length)

    flamey=loopy(length)
    #print(flamey)
    
    relationship=""

    if flamey=="F":
        relationship= "Friendship"
    elif flamey=="L":
        relationship= "Love"
    elif flamey=="A":
        relationship= "Affection"
    elif flamey=="M":
        relationship= "Marriage"
    elif flamey=="E":
        relationship= "Enemies"
    elif flamey=="S":
        relationship= "Siblings"

    return relationship


#print(show_relationship("KEVIN", "KATH"))
            




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

"""
ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. The last digit can be 0-9 or X, to indicate a value of 10.

An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.

For example:

ISBN     : 1 1 1 2 2 2 3 3 3  9
position : 1 2 3 4 5 6 7 8 9 10
This is a valid ISBN, because:

(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0

Examples
1112223339   -->  true
111222333    -->  false
1112223339X  -->  false
1234554321   -->  true
1234512345   -->  false
048665088X   -->  true
X123456788   -->  false

"""

def valid_ISBN10(isbn): 

    num= ["0","1","2","3","4","5","6","7","8","9","10"]
    
    #check last digit
    isbn=list(isbn)
    if isbn[-1] == "X":
        isbn[-1]="10"

    #check are numbers
    for char in isbn:
        if char not in num:
            return False
    
    #check length
    if len(isbn) !=10:
        return False
    
    #multiply by index
    sum=0
    index=1
    
    for char in isbn:
        sum+=(int(char) *index)
        index+=1
        print(sum)
        
    #test if valid
    if sum %11 ==0:
        return True
    else:
        return False


#(valid_ISBN10("1293"))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
"""
John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of distances between these towns. 
ls = [50, 55, 57, 58, 60]. John is tired of driving and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible to please Mary and John?

Example:
With list ls and 3 towns to visit they can make a choice between: [50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].

The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 corresponding towns is [55, 58, 60].

The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters t (maximum sum of distances, integer >= 0), 
k (number of towns to visit, k >= 1) and ls (list of distances, all distances are positive or zero integers and this list has at least one element). 
The function returns the "best" sum ie the biggest possible sum of k distances less than or equal to the given limit t, if that sum exists, or otherwise nil,
 null, None, Nothing, depending on the language. 

Examples:
ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163

xs = [50] choose_best_sum(163, 3, xs) -> nil (or null or ... or -1 (C++, C, D, Rust, Swift, Go, ...)

ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228

Notes:
try not to modify the input list of distances ls
in some languages this "list" is in fact a string (see the Sample Tests).


"""
import itertools

def choose_best_sum(t, k, ls):

    combinations=[]

    for r in range(k+1):
        combinations+= itertools.combinations(ls,r)
    
    combinations=list(combinations)
    combo=[]
    for listy in combinations:
        if len(listy) == k:
            combo.append(listy)   
    sums=[]

    for groups in combo:
        sums.append(sum(groups))

    result=[]

    for nums in sums:
        if nums <=t:
                result.append(nums)

    result.sort()
    res=result[-1:]
    if (len(res)) ==1:
        res=res[0]
    
        return res
    else:
        return None
       
xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_best_sum(230, 4, xs))
"""

example from codewaars:


import itertools
def choose_best_sum(t, k, ls):
    try: 
        return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
    except:
        return None



Iterator                            Arguments                                           Results

product()                                  p, q, … [repeat=1]                           cartesian product, equivalent to a nested for-loop

permutations()                             p[, r]                                       r-length tuples, all possible orderings, no repeated elements

combinations()                             p, r                                         r-length tuples, in sorted order, no repeated elements

combinations_with_replacement()            p, r                                         r-length tuples, in sorted order, with repeated elements







"""














"""
   combination = [] # empty list 
   for r in range(1, len(lst) + 1):
      # to generate combination
      combination += itertools.combinations(lst, r)
   return combination
objects = ['9', '8', '0'] # creating a list named objects
all_combinations = get_combinations(objects) # method call
print(all_combinations)
    """




