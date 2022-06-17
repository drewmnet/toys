import operator
from random import random as rnd

class Battler:
    def __init__(self, name):
        self.name = name
        self.initiative = 0
        
    def roll(self):
        self.initiative = int(rnd() * 20) + 1

initiative = {}

fighters = [ Battler("Elaine"),Battler("Talin"),Battler("AVAT5"),Battler("Cok1"),Battler("Cok2") ]

for fighter in fighters:
    fighter.roll()

for fighter in sorted(fighters, key=operator.attrgetter('initiative')):
    print(f"{fighter.name}")
