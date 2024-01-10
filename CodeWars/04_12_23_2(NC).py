"""Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.

Examples
"1999" --> "20th"
"2011" --> "21st"
"2154" --> "22nd"
"2259" --> "23rd"
"1124" --> "12th"
"2000" --> "20th"
"""

def what_century(year):
    """Func to return century from 4 digit string"""

    start =0 #<- used for incrementing up century

#--------------Check for if century stays same as first 2 digits, then adds ordinal-----------------------------------#

    if year[2:] =="00":
        #----------------------ordinal for 10-19 range--------------------------------------------------#
        if str(year)[0]=="1":
            return year[0:2] +"th"
        else:
            #----------------------ordinal for all others--------------------------------------------------#
            if year[1] =="1":
                return year[0:2] + "st"
            elif year[1] =="2":
                return year[0:2] + "nd"
            elif year[1] =="3":
                return year[0:2] + "rd"
            else:
                return year[0:2] +"th"
        
    #------------Increments first 2 digits by 1 to get century then add ordinal-------------------------#    
    else:
        start = int(year[0:2])
        start = start+1
        #----------------------ordinal for 10-19 range--------------------------------------------------#
        
        
def ordinals(year):
    start=0
    if str(start)[0]=="1":
            return str(start) +"th"
        
    else:
            #----------------------ordinal for all others--------------------------------------------------#
            if str(start) [-1]=="1":
                return str(start) + "st"
            elif str(start) [-1]=="2":
                return str(start) + "nd"
            elif str(start) [-1]=="3":
                return str(start) + "rd"
            else:
                return str(start) +"th"

#print(what_century("1300"))

##--------------------------------------------------------------------------------------------------------------------------##