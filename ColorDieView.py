"""Code created by Elimelec Rodriguez and Cedric Perez
This code introduces a very popular and known game, Parchessi or as some might know it, Trouble
in a simpler way, yet recognizable and fun way"""
#imports of all the classes used in this interactive game
from dieview import DieView

class ColorDieView(DieView):

    #function to set the dice values
    def setValue(self,value): 
        self.value = value
        DieView.setValue(self,value)
    #function the set the pips color
    def setColor(self,color):
        self.foreGround = color
        self.setValue(self.value)

