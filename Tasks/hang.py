import random


word_bank = "BANK","CAR","CAT","TRACTOR","ELEPHANT","PERSON","WELL","TRAIN","FOLLOW","RED"
answer = random.choice(word_bank)

#print(answer)

guessed = ""
attempts = 8

while attempts >0:
    failed = 0

    for char in answer:
        if char in guessed:
            print(char, end="")
        else:
            print("_", end="")
            failed+=1

    if failed ==0:
            print("You got it")
            break

    guess = input("Take a guess")
    guessed +=guess.upper()

    if guess.upper() not in answer:
            print("Nope")
            attempts -=1
            print("You have",attempts, "left")

    if attempts ==0:
         print("You are out of attempts! it was: ", answer)
         break
