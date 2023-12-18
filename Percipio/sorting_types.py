#-----------------selection sorting#---------------
#when looking at an array, compares the first element to all the others and finds the smallest, then swaps them
#then does same with second, third etc
# saves some memory but each swap takes time so it makes O(n2) comparissons and O(n) swaps

#----------------------------------------bubble sorting---------------------------------------------------------#
#Compares first element with element to it's right, if frst is bigger(Can do smaller to left) they swap. Then it is compared to next one,if it 
#is not bigger there is no swap and it moves to next 2. it will likely take multiple iterations to fully sort the array.
# worst case scenario there will be swaps at every steps. Its time O(n2) comparissons and swaps, but it is stable. It does not take extra space as it is the same list
# ----------------------------------insertion sorting--------------------------------------------------------------#

#Compares elements to the element before it, if it is smaller it swaps places, then keeps checking the next one before it until it is out of places or is in right place
# keeps then going right all the way to left per card like shuffling cards in your hand.
#popular with divide and conquer algorithms, its adaptive nature means its quick. Better than bubble as doesn't need the final check over to be sure its
#right.
#-------------------------------------shell sort---------------------------------------------------------------------#
# a divide and conquer style sort. Split the list into siblists, eg. increment of 2, then sort these lists like in insertion sorting moving them to the left if smaller
#these sub lists are them put back together and sorted again. For larger arrays could be half len n to reduce the swaps down until need to increment it by 1 finnally. Reduces the 
#ammount of swaps required. The diferent increments and values chosen will effect the complexity . O(N^3/2) as an averge O(1) space as diesnt generate other lists, just splits itself
#-----------------------------------merge sorting---------------------------------------------------------------------# 
#recursively split list down into "sorted" list of 1 item, this is divide phase, then in merge portionthe lists are added together, so small list of 2 would get sorted then bigger and
# bigger until 1 large list is sorted uses O(N) space, not adaptive-no matter the list the order of operation is exactly the same, is stable
#-------------------------------------------------------quick sort--------------------------------------------------------------#

<<<<<<< HEAD
=======
# SELECTION SORT ON^2# 


def print_list(num_list):
    print(num_list)

def selection_sort(original_list):

    length = len(original_list)

    for i in range(length): # <-- sets the index to the next in list

        min_value_index = i

        for j in range(i+1, length): # <-- gets them to check the number

            if original_list[min_value_index] > original_list[j]:
                min_value_index=j

        original_list[i], original_list[min_value_index] = original_list[min_value_index], original_list[i] #<-- swaps them 

        print("Sorted till index ", i)
        print_list(original_list)

    print("Sorted list: ")
    print_list(original_list)

num_list= [10,11,5,7,2,8,3,9,6,1,4]

#selection_sort(num_list)

"""
 Sorted till index  0
[1, 11, 5, 7, 2, 8, 3, 9, 6, 10, 4]
Sorted till index  1
[1, 2, 5, 7, 11, 8, 3, 9, 6, 10, 4]
Sorted till index  2
[1, 2, 3, 7, 11, 8, 5, 9, 6, 10, 4]
Sorted till index  3
[1, 2, 3, 4, 11, 8, 5, 9, 6, 10, 7]
Sorted till index  4
[1, 2, 3, 4, 5, 8, 11, 9, 6, 10, 7]
Sorted till index  5
[1, 2, 3, 4, 5, 6, 11, 9, 8, 10, 7]
Sorted till index  6
[1, 2, 3, 4, 5, 6, 7, 9, 8, 10, 11]

Sorted till index  7
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] <-- is actually sorted at this point, but is not adaptive so doesn't know to stop

Sorted till index  8
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Sorted till index  9
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Sorted till index  10
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Sorted list: 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
 
 """       

# BUBBLE SORT ON^2# 

def bubble_sort (original_list):

    length = len(original_list)
    
   

        
    for i in range(length - 1, 0, -1): # <-- iterations length of the list, but starts at last element to the first
        
        for index in range(i):
            
            if original_list[index] > original_list[index + 1]:
                
               
                original_list[index + 1], original_list[index] = \
                    original_list[index], original_list[index + 1]
             

        print("Unsorted till index: ", i-1)
        print_list(original_list)

student_marks = [88,99,34,32,43,25,29,45,49,37]
#bubble_sort(student_marks)

"""
Unsorted till index:  8
[88, 34, 32, 43, 25, 29, 45, 49, 37, 99]
Unsorted till index:  7
[34, 32, 43, 25, 29, 45, 49, 37, 88, 99]
Unsorted till index:  6
[32, 34, 25, 29, 43, 45, 37, 49, 88, 99]

Unsorted till index:  5 <----- Again is already sorted but will still carry on due to length. Could add counter to stop byt counting swaps
[32, 25, 29, 34, 43, 37, 45, 49, 88, 99]

Unsorted till index:  4
[25, 29, 32, 34, 37, 43, 45, 49, 88, 99]
Unsorted till index:  3
[25, 29, 32, 34, 37, 43, 45, 49, 88, 99]
Unsorted till index:  2
[25, 29, 32, 34, 37, 43, 45, 49, 88, 99]
Unsorted till index:  1
[25, 29, 32, 34, 37, 43, 45, 49, 88, 99]
Unsorted till index:  0
[25, 29, 32, 34, 37, 43, 45, 49, 88, 99]

"""


#MERGE SORT#



>>>>>>> 0422d92 (Update)
