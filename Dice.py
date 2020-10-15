import random

class Dice:

    def __init__(self):
        self.dice = 0

    def rollDie(self):
        self.dice = random.randint(1,6)
        
    def diceValue(self):
        return self.dice