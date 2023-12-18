##=== It's long: https://www.codewars.com/kata/651bfcbd409ea1001ef2c3cb/train/python ==##
"""
class Character:

    def character_info(self) -> str:
         Return a multiline string representing the current characteristics of the hero

    def event_log(self) -> str:
         Return a multiline string representing the events that occured in chronological order
"""
#-----------------------------------------------------------------------------------------------------------------------------------#

class Character():

    def __init__(self,name="Hero", strength=10, dexterity=10,intelligence=10):
        """Initialises stats of the character with defaults"""

        self.name = name
        self.str=strength
        self.dex=dexterity
        self.int=intelligence
        #self.wep= needs to go here or not?

#-----------------------------------------------------------------------------------------------------------------------------------#
    def wepon_of_something(self,str_mod, dex_mod, int_mod, bonus_dmg):
        """Generates basic wepon and replaces with other wepon somehow?"""

        """mod*strength+mod*dexterity+mod*intelligence+bonus_dmg=dmg""" # <-- formulae for calculating dmg

        #wepon = "limbs" default but changes when ch.something_of_something called? but still stores them, dict maybe?"
        damage= str_mod* self.str + dex_mod*self.dex + int_mod*self.int + bonus_dmg #default needs to be 32. could be a func itself?

        # way of triggering string in event log for times and names called?#

        #should always show highest damage wepon, if tied display first alphabetically, needs to store them but just
        #display highest on character info#

#-----------------------------------------------------------------------------------------------------------------------------------#
    def character_info(self):
        """ Prints the character statistics"""

        print("\n",self.name, "\n", "str", self.str,"\n", "dex", self.dex,"\n", "int", self.int,"\n")#,self.wep and damage?)

    #def event_log(self) -> str:
        #return a multiline string in chronological order of things that happened e.g:
            # Kroker finds 'Axe of fire'
            #"\n",self,name," finds ", wepon name?, "\n"




#-----------------------------------------------------------------------------------------------------------------------------------#
""" Tests and calling to work"""

ch = Character("Kroak", strength=11, dexterity=7)
ch.character_info()
#ch.axe_of_fire(3, 1, 0, 20) # weapon method name can be anything as long as it matches weapon_of_something