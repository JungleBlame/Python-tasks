from random import choice

class Hangman(object):
    """Main class for hangman game"""

  #------------------------------------------------------------------------------------------------------------------------------------------------#
#Initialises variables needed for game, generates the answer#  

    def __init__(self,answer="",attempts=6,guessed="",guess="",test=""):
        self.attempts= attempts
        self.guessed=guessed
        self.end=0
        self.guess=guess
        word_bank = ["BANK", "MOUSE", "ELEPHANT", "DOG", "TREE", "GARAGE", "JUMP"]
        answer = choice(word_bank)
        self.answer= answer
        self.test=test
#------------------------------------------------------------------------------------------------------------------------------------------------#
#Func to reduce attempts counter#

    def attempts_down(self):
        self.attempts-=1

#------------------------------------------------------------------------------------------------------------------------------------------------#
#For loop to check guess and give win condition#

    def show_chars(self):
        
        if self.guess.upper() in self.answer:
            for char in self.answer:
                if char in self.guessed.upper():
                    print(char, end="")
                    self.test+=char
                else:
                    print("_", end ="")
            if self.test.upper() ==self.answer:
                self.win()
                #print(self.test)

        elif self.guess not in self.answer:
            self.attempts_down()
            print("Thats not in it! you have: ", self.attempts, "left!")
                
#------------------------------------------------------------------------------------------------------------------------------------------------#
#Win print message#

    def win(self):
        print("Yes that's right! it was: ", self.answer) 
        self.end=1
        
#------------------------------------------------------------------------------------------------------------------------------------------------#    
#Lose print message#

    def lose(self):
        print("You are out of guesses! It was: ",self.answer)
        print("Good-bye!")
        
#------------------------------------------------------------------------------------------------------------------------------------------------#
#Triggers recursive function for game and generates game object#

def main():
    game= Hangman()
    game_loop(game)
    
#------------------------------------------------------------------------------------------------------------------------------------------------#
#Recursive function that loops until attempts==0, or answer is right#

def game_loop(game):

    
    if game.end==0:

        game.test=""
        game.guess=input(" Take a guess!")

        if game.attempts==1:
            game.lose()
        
        elif game.test == game.answer:    
            game.win()
            

        elif game.test != game.answer:
            
            if len(game.guess)>1:
                print("Only guess one character at a time!")
                game.attempts_down()
                print("You have: ", game.attempts, "left!")
                game_loop(game)
            else:
                game.guessed +=game.guess
                game.show_chars()
                game_loop(game)
        
    elif game.end==1:
        print("Good-bye")
#------------------------------------------------------------------------------------------------------------------------------------------------#
#Triggers game#

main()




    
                


    

