from time import sleep
from random import choice


def greeting():
    """"Function to greet the user"""
    
    sleep(2)
    name=input("Hello, what is you name?")
    sleep(2)
    print("Hi ",name, "Lets play hangman")
    sleep(2)

#----------------------------------------------------------------#

def random_num():
    """ Function to give the answer"""

    word_bank=["DOG", "CAT","WOLF","ELEPHANT","DEER","MOUSE"]
    answer = choice(word_bank)
    guessed=""
    attempts=6
    
    
    user_input(attempts_pass=attempts,guessed_pass=guessed,answer_pass=answer)

#-----------------------------------------------------------------#

def user_input(guessed_pass,answer_pass,attempts_pass):
    """User input for the guess"""

    attempts=attempts_pass
    guessed=guessed_pass
    answer=answer_pass
    
    guess=input("Take a guess!")
    guessed+=guess.upper() 
    
    if attempts==1:
        print("You are out of guesses, it was:", answer)
    else:
        main_hang_loop(attempts_pass=attempts,guessed_pass = guessed,guess_pass=guess,answer_pass=answer)

#---------------------------------------------------------------------#
    
def main_hang_loop(attempts_pass,answer_pass, guessed_pass, guess_pass):
    """ Main hangman loop"""

    attempts=attempts_pass
    answer=answer_pass
    guessed=guessed_pass
    guess=guess_pass
    end=True

    end=check_loop(answer_pass=answer,guessed_pass=guessed)

    if end== True:
        attempts=attempts_func(attempts_pass,answer_pass=answer,guess_pass=guess)

        user_input(answer_pass=answer,guessed_pass=guessed,attempts_pass=attempts)

    elif end==False:
        print("You got it!")
        
#------------------------------------------------------------------------#

def check_loop(answer_pass,guessed_pass):
    """ Check answer loop"""

    guessed=guessed_pass
    answer=answer_pass
    failed=0
    end=True

    for chars in answer:

        if chars in guessed:
            print(chars, end="")
        else:
            print("_", end="")
            failed+=1

    if failed==0:
            end=False
            win_func()
            return end
            
    elif failed>0:
        end=True
        return end
#-------------------------------------------------------------------#

def win_func():
    """Func for winning and ending"""

    print("You win!")
    
   
#---------------------------------------------------------------------#

def attempts_func(attempts_pass,answer_pass,guess_pass):
    """Function to reduce attempts"""
    
    attempts=attempts_pass
    answer=answer_pass
    guess=guess_pass
    
    if attempts ==1:
        lose_func(answer_pass)
         
        
    elif guess.upper() not in answer:
        print("That's not in it!")
        attempts-=1
        print("You have: ", attempts, "left!")

    return attempts
        
#---------------------------------------------------------------------#

def lose_func(answer_pass):
    """function for the loss"""

    answer=answer_pass
    print("You lose! It was: ")
    print(answer)
    

#---------------------------------------------------------------------#

#Start Hangman#

greeting()

random_num()