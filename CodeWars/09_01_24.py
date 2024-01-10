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

        middle_index=find_middle_element(snail_map)
        snail_result=snail_sort(snail_map,middle_index)
        return snail_result

def find_middle_element(snail_map):

    middle_element=[]
    middle_index=""

    for listy in snail_map:
        for nums in listy:
            middle_element.append(nums)
            middle_index= middle_index+str(nums)

    #print(middle_element)
    #print(middle_index)
    middle_index=len(middle_element)//2
    #print(middle_index)
    
    
    return middle_index
    
def snail_sort(snail_map,middle_index):

    snail_result=[]
    snail_reversed=[]
    odd_even=0
    for listy in snail_map:
        if odd_even%2==0:
            for nums in listy:
                snail_result.append(nums)
                odd_even+=1
        elif odd_even%2!=0:
            for nums in reversed(listy):
                snail_result.append(nums)
                odd_even+=1

    snail_result=snail_result[0:middle_index]
   

    odd_even=0
    for listy in reversed(snail_map):
        if odd_even%2==0:
            for nums in reversed(listy):
                snail_reversed.append(nums)
                odd_even+=1
        elif odd_even%2!=0:
            for nums in listy:
                snail_reversed.append(nums)
                odd_even+=1

    snail_reversed=snail_reversed[0:middle_index+1]
    
    #print(snail_reversed)
    #print(snail_result)

    snail_result=snail_result+snail_reversed
    #print(snail_result)
    return snail_result

print(snail([1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 25, 24, 23, 22, 21, 16, 17, 18, 19, 20, 15, 14, 13]))