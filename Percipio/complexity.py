#----------------------O(1) COMPLEXITY----------------------------------------------------------------------#

def addition(num1,num2):
    num_iterations = 0

    total=num1+num2
    num_iterations+=1

    print ("The sum of %d and %d is %d \nTotal number of iterations is: %d" % (num1,num2,total, num_iterations))

addition(220495,594756) # <--- No matter the complexity it will be 1 iteration. It is a constant time operation.

#----------------------O(n) COMPLEXITY----------------------------------------------------------------------#

def check_prime(num):
    num_iterations=0

    for i in range (2,num):
        num_iterations+=1

        if num%i ==0:
            print("%d is not a prime number\n Total iterations: %d" %(num, num_iterations))

            return
    print("%d is a prime number. Total iterations: %d" % (num,num_iterations))

check_prime(49)
#----------------------O(n^2) COMPLEXITY----------------------------------------------------------------------#
#Nested for loops usually are n^2
def print_pairs(number_list):
    num_iterations = 0
    n=len(number_list)

    for i in range(n):
        for j in range(n):
            print(number_list[i], number_list[j])
            num_iterations+=1

    print("Total iterations are %d" % num_iterations)

print_pairs([123,67,25,79])