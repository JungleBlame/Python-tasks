"""Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome! To celebrate, 
you're taking your team out to the terrible dive bar next door and using the referral bonus to buy, and build, the largest
 three-dimensional beer can pyramid you can. And then probably drink those beers, because let's pretend it's Friday too.

A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second, 9 in the next, 16, 25...

Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make, given the parameters of:

your referral bonus, and

the price of a beer can

For example:

beeramid(1500, 2); // should === 12
beeramid(5000, 3); // should === 16

"""

def beeramid(bonus, price):

    can_on_level=0
    full_levels=1
    level_times=1
    cost_of_cans=0
    end=1

    if bonus-price<0:
        full_levels=0
        return full_levels
    
    elif bonus-price==0:
        full_levels=1
        return full_levels
    
    elif (bonus-price) -(4*price)<0:
        full_levels=1
        return full_levels
    
    elif (bonus-price) -(4*price)==0:
        full_levels=2
        return full_levels
    
    else:

        bonus=bonus-price 

        while end!=0:
            
            level_times+=1
            can_on_level=level_times*level_times
            cost_of_cans= price*can_on_level

            if bonus-cost_of_cans<0:
                return full_levels  

            else:
                bonus=bonus-cost_of_cans
                full_levels+=1

                if bonus-cost_of_cans<0:
                    return full_levels
                else:
                    continue

"""
Better way:

def beeramid(bonus, price):
    beers  = bonus // price
    levels = 0
    
    while beers >= (levels + 1) ** 2:
        levels += 1
        beers  -= levels ** 2
    
    return levels

"""
"""
Task
You are given a string s. Every letter in s appears once.

Consider all strings formed by rearranging the letters in s. After ordering these strings in dictionary order, return the middle term. (If the sequence has a even length n, define its middle term to be the (n/2)th term.)

Example
For s = "abc", the result should be "bac".

 The permutations in order are: "abc", "acb", "bac", "bca", "cab", "cba" So, The middle term is "bac".

Input/Output
[input] string s
unique letters (2 <= length <= 26)

[output] a string
middle permutation.
"""
from itertools import permutations

def middle_permutation(string):

    

    listy=list(permutations(string))

    lengthy=len(listy)
    lengthy_half=lengthy//2-1
    
    result=""
    res=listy[lengthy_half]
    
    for char in res:
        result+=char

    return result

print(middle_permutation('nyhsiloatcumwzxp'))
