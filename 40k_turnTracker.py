#Plan to make 40k tracker

#class for game, tracks turns, function decides mission(module?), function for drawing secondary cards (module?), function to redraw that reduces command points by 1 once per game

#class for player containing: name, score, command points, army, fucntion to add points and commnad points?

#function to initiate, 10 rounds total, split into 6 phases, prompts in each that are relevant?
#if tactical chosen lock out card options?
# check for some cards that cannot eb scred turn 1/ cannot be scored?

# while loop choice menu?


class cards():

    def __init__(self,name):
        self.name=name

class card_maker():

    def __init__(self,name,change=0):

        self.name=name
        self.change=change

    def __str__(self,name):

        self.name=name
        return self.name

card1= cards("Destroy")
card2= cards("Build")

class player(card_maker):

    def __init__(self,name):
        self.name=name
        self.hand=[]
        self.card1=card1
        self.card2=card2

    def __str__(self,name):

        self.name=name
        return self.name
        

Player1=player("Ryan")
Player2=player("Steve")

Player1.hand.append(Player1.card1)
Player1.hand.append(Player1.card2)



print(Player1.hand)
print(Player2.hand)
#go first doesnt recognise name
# timer so you can see messafes?
#endless loop second player fixed?
#Says invalid choice when valid fixed picked first


