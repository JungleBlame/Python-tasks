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

