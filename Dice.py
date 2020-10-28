"""Code created by Elimelec Rodriguez and Cedric Perez
This code introduces a very popular and known game, Parchessi or as some might know it, Trouble
in a simpler way, yet recognizable and fun way"""
#imports of all the classes used in this interactive game
import random

class Dice:

    def __init__(self):
        self.dice = 0 #variable to hold the dice value

    def rollDie(self):
        self.dice = random.randint(1,6) #generates a random number between 1-6
        
    def diceValue(self): #returns the dice value
        return self.dice