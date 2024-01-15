"""https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. 
The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration 
specified by of a component must not be greater than any valid more significant unit of time.
"""

def format_duration(seconds):
    """
    minutes=60
    hours=3600
    days=3600
    years=1,314,000
    """
    
   
    def Year(seconds,year=0,):
        
        if seconds-1314000 <0:
            print(year)
            Day(year,seconds)

        elif seconds-1314000>0:
            print("yabadoo")
            seconds=seconds-1314000
            year+=1
            Year(year,seconds)
    
    def Day(year,seconds,day=0):
        
        if seconds-3600 <0:
            Hour(day,year,seconds)

        elif seconds-3600>0:
            seconds=seconds-3600
            day+=1
            Day(day,year,seconds)
    
    def Hour(year,day,seconds,hour=0):
        
        if seconds-3600 <0:
            Minute(hour,day,year,seconds)

        elif seconds-3600>0:
            seconds=seconds-3600
            hour+=1
            Hour(hour,year,day,seconds)
    
    def Minute(year,day,hour,seconds,minute=0):
        
        if seconds-60 <0:
            Result(hour,minute,day,year,seconds)

        elif seconds-60>0:
            seconds=seconds-60
            minute+=1
            Minute(minute,year,day,hour,seconds)

    def Result(minute,hour,day,year,seconds):
       
        res= "{} years, {} days,{} hours,{} minutes and {} seconds.".format(year,day,hour,minute,seconds)
        print(res)
        return res
    
    if seconds ==0:
        return "Now"
    elif seconds>0:
        Year(seconds)
        
#print(format_duration(60))
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------#
        
"""
https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python
Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

Example(Input --> Output)

["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 
Note: In COBOL, it should return "found the needle at position 6"



"""
def find_needle(haystack):
    
    indexy=haystack.index("needle")

    return "found the needle at position {}".format(indexy)

#print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] ))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
"""
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
"""

def snail(snail_map):

    if snail_map==[[]]:
        return []
    else:

        snail_result=snail_sort(snail_map)
        return snail_result
    
def snail_sort(snail_map):

    snail_result=[]
    switch=1
    index_list=None
    
    while len(snail_map) !=0:
        index_last=snail_map.index(snail_map[-1])

        if switch==1:   
            for listy in snail_map:
                index_list=snail_map.index(listy)
                
                if snail_map.index(listy)==0:

                    for nums in listy:
                        snail_result.append(nums)

                elif snail_map.index(listy)==index_last:

                    for nums in reversed(listy):
                        snail_result.append(nums)
                    switch=2

                else:
                        snail_result.append(listy[-1])
                        snail_map[index_list].pop(-1)

            if len(snail_map) !=0:
                snail_map.pop(0)
            if len(snail_map) !=0:
                snail_map.pop(-1)

        elif switch==2:
    
            for listy in reversed(snail_map):
                index_list=snail_map.index(listy)
                if snail_map.index(listy)==0:
                    switch=1
                    
                else:

                    snail_result.append(listy[0])
                    snail_map[index_list].pop(0)
                        

    return snail_result

print(snail([[1, 2, 3, 4, 5], 
             [6, 7, 8, 9, 10], 
             [11, 12, 13, 14, 15], 
             [16, 17, 18, 19, 20], 
             [21, 22, 23, 24, 25]]))

# should be -> [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
# currently -> [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 25, 24, 23, 22, 21, 16, 17, 18, 19, 20, 15, 14, 13]

"""
Other answers:

def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out
#--------------------------------------------------------------------------------------------------------------------------------#

def snail(array):
    res = []
    while len(array) > 1:
        res = res + array.pop(0)
        res = res + [row.pop(-1) for row in array]
        res = res + list(reversed(array.pop(-1)))
        res = res + [row.pop(0) for row in array[::-1]]
    return res if not array else res + array[0]

#----------------------------------------------------------------------------------------------------------------------------------#
def snail(array):
    #base case for recursion with n odd
    if len(array)==1: return array[0]
    #base case for recursion with n even
    if len(array)==2: return array[0]+array[1][::-1]
    res=[] #accumulator variable for my result
    #I go on "shaving" the array and taking what I need as a result
    #getting the first row
    res+=array.pop(0)
    #getting the last element of every remaining row but the last
    for i in range(len(array)-1):
        res.append(array[i].pop(-1))
    #getting the last one - reversed
    res+=array.pop(-1)[::-1]
    #and getting the first element of the remaining rows in reverse order
    for i in range(-1,-len(array),-1):
        res.append(array[i].pop(0))
    #calling recursively the function with a smaller array
    return res+snail(array)
    #usually I avoid recursive solutions, but I decided to try my hand
    #in a while with them. I hope you enjoyed reading my code :)

"""