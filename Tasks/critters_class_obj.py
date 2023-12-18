#Critter farm caretaker game
# Virtual pet
from random import randint 
from random import choice

class Critter(object):
    """A virtual pet"""

    def __init__(self, name, hunger=4, boredom=4):
        hunger=randint(1,15)
        boredom=randint(1,15)
        self.name=name
        self.hunger=hunger
        self.boredom=boredom

    def __str__(self):
        
        return f"{self.name}(Hunger:  {self.hunger} Boredom {self.boredom})"
    
    def pass_time(self):
        self.hunger+=1
        self.boredom+=1
    
    @property
    def mood(self):
        unhappiness=self.hunger + self.boredom

        if unhappiness <7:
            m="happy"
        elif 7<= unhappiness <=12:
            m = "okay"
        elif 13 <= unhappiness <=17:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print ("I'm", self.name, "and I feel", self.mood, "now.\n")
        if self.boredom >15:
            print("I'm so bored!")
        if self.hunger >15:
            print("I'm so hungry!")
        self.pass_time()

    def eat(self, food=4):
        
        food_thanks=["That was great!","Brrupp. Thank you.","Just what i needed!", "Yay!"]
        print(self.name, "Says:", choice(food_thanks))
        self.hunger-=food 

        if self.hunger<0:
            self.hunger=0
        self.pass_time()
    
    def play(self, fun=4):
        
        fun_thanks= ["Yay!","That was awesome!","That was fun!", "Awesome!"]
        print (self.name,"Says:", choice(fun_thanks))
        self.boredom -=fun

        if self.boredom<0:
            self.boredom=0
        self.pass_time()


def main():
    crit1= input("Give the first critter a name!")
    crit2= input("Give the second critter a name!")
    crit3= input("Give the third critter a name!")

    crit1=Critter(crit1)
    crit2=Critter(crit2)
    crit3=Critter(crit3)
    
    all_critters= [crit1,crit2,crit3]

    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker Farm
    
        0 - Quit
        1- Listen To your Critters
        2- Feed your critters
        3- Play with your critters
        """)
        choice = input("Choice= ")
        print()

        #exit
        if choice =="0":
            print("Good-bye")

        #lsiten 
        elif choice=="1":
            for i in all_critters:
                i.talk()

        #feed
        elif choice=="2":
            food = input("\nHow much do you want to feed?(1-15)")
            try:
                food= int(food)
                if food <=0:
                    print("\nNot being fed then")
                elif food<5:
                    print("\nSmall snack")
                    for i in all_critters:
                        i.eat(food)

                elif food <10:
                    print("\nBig snack")
                    for i in all_critters:
                        i.eat(food)
                    
                elif food<16:
                    print("\nGormet meal!")
                    for i in all_critters:
                        i.eat(food)
                    
                else:
                    print("\n Thats not a valid ammount!")

            except: 
                print("You can't feed that!")
                for i in all_critters:
                        i.pass_time()
                
                
    
    
        #play
        elif choice=="3":
            play = input("How long do you want to play?")
            try:
                play=int(play)
                if play <=0:
                    print("\nNot being played with then)")
                elif play<5:
                    print("\nSmall play")
                    for i in all_critters:
                        i.play(play)
                    

                elif play <10:
                    print("\nBig play")
                    for i in all_critters:
                        i.play(play)
                elif play <16:
                    print("\nFun zone!")
                    for i in all_critters:
                        i.play(play)
                else:
                    print("\n Thats not a valid ammount!")
            except:
                print("That's not valid!")
                for i in all_critters:
                        i.play(play)

        elif choice== crit1.name:
            print(crit1)
        elif choice== crit2.name:
            print(crit2)
        elif choice== crit3.name:
            print(crit3)


            
    
        else:
            print ("\nSorry but", choice, "is not a valid choice.")

main()
("\n Press the enter key to exit.")
 

