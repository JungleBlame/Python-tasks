





def random_word_func():
    import random
    word_bank=["DOG", "CAT","WOLF","ELEPHANT","DEER","MOUSE"]
    global answer
    answer= random.choice(word_bank)
    print(answer)

def input_guess():
    guess = input("Take a guess")
    result= guess.upper()
    return result

def main_hang_loop():
    
    
    failed=failed_passed
    guessed=guessed_passed
    attempts=8
    random_word_func()
    while attempts >0:
        check_loop()
        
        if failed ==0:
            print("You got it!")
            break
        
        if input_guess() not in answer:
           print("Nope")
           attempts-=1
           print("You have: ", attempts, "left")

        if attempts==0:
            print("You are out of guesses! It was: ", answer)
 
            break

def check_loop(guessed_passed_over):
    guessed = guessed_passed_over
    passy_pass(guessed=g)
    add_guess(guessed)
    guessed= guessed
    for char in answer:
        if char in guessed:
            print(char, end="")
        else:
            print ("_", end="")
            failed+=1
    
      
def add_guess():
    guessed=""
    result=input_guess()
    guessed+=result
    check_loop(guessed)
    add_guess(guessed)

def passy_pass(guessed=g):
    failed=0
    guessed
    return guessed and failed
    
main_hang_loop()



