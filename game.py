from graphics import *
from Dice import Dice
from dieview import DieView
from player import Player
from chip import chip
from Buttons import Button


class Game:

    def __init__(self):
        self.player = Player()

        self.players = []
        for x in range(4):
            self.players.append(Player())


    def playGame(self, win):

        self.players[0].drawPlayer("red", win)
        self.players[1].drawPlayer("blue", win)
        self.players[2].drawPlayer("green", win)
        self.players[3].drawPlayer("yellow", win)

        remSteps = chip()

        rollButton = Button(win, Point(720.0, 45),80, 30, "Roll Dice")
        quitButton = Button(win, Point(720.0, 510),80, 30, "QUIT")
        rollButton.activate()
        quitButton.activate()

        pt = win.getMouse()


        while not quitButton.clicked(pt) or self.playerWon(win):
        

            if self.players[0]:
                if rollButton.clicked(pt):
                    sumDie = self.rollDice(win)
                    self.player.MovePiece(self.players[0].player, sumDie, "red", remSteps.returnSteps(), win)

            if self.players[1]:
                if rollButton.clicked(pt):
                    sumDie = self.rollDice(win)
                    self.player.MovePiece(self.players[1].player, sumDie, "blue", remSteps.returnSteps(), win)

            if self.players[2]:
                if rollButton.clicked(pt):

                    self.player.MovePiece(self.players[2].player, sumDie, "green", remSteps.returnSteps(), win)

            if self.players[1]:
                if rollButton.clicked(pt):

                    self.player.MovePiece(self.players[3].player, sumDie, "yellow", remSteps.returnSteps(), win)

            pt = win.getMouse()


            
    def playerWon(self, win):
        playerPiece = self.player.returnRed()
        print(self.player.returnRed)
        if self.player.piecesInHome(playerPiece):
            winner = Text(Point(720.0, 300), "You WON!")
            winner.setStyle("bold")
            winner.setSize(26)
            winner.draw(win)
            return True
            
    def rollDice(self, win):
        dado = Dice()

        dado.rollDie()
        diceVal = dado.diceValue()

        viewDice = DieView(win,Point(690.0, 120.0), 50)
        viewDice.setValue(diceVal)
        dado.rollDie()
        diceVal2 = dado.diceValue()
        viewDice2 = DieView(win,Point(760.0, 120.0), 50)
        viewDice2.setValue(diceVal2)


        return diceVal + diceVal2
                


        
        

