from graphics import *
from Dice import Dice
from dieview import DieView
from player import Player
from chip import chip


class Game:

    def __init__(self):
        self.player = Player()



    def playGame(self, win):

        self.player.drawPlayer("red", win)
        remSteps = chip()
        dado = Dice()

        dado.rollDie()
        diceVal = dado.diceValue()

        viewDice = DieView(win,Point(690.0, 120.0), 50)
        viewDice.setValue(diceVal)
        dado.rollDie()
        diceVal2 = dado.diceValue()
        viewDice2 = DieView(win,Point(760.0, 120.0), 50)
        viewDice2.setValue(diceVal2)

        #sumDie = diceVal + diceVal2

        self.player.MovePiece(self.player.player, 60, "red", remSteps.returnSteps(), win)
        self.playerWon(win)

    def playerWon(self, win):
        playerPiece = self.player.returnRed()
        print(self.player.returnRed)
        if self.player.piecesInHome(playerPiece):
            winner = Text(Point(720.0, 300), "You WON!")
            winner.setStyle("bold")
            winner.setSize(26)
            winner.draw(win)

                


        
        

