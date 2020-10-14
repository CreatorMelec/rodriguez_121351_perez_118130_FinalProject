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

        remSteps = chip()

        rollButton = Button(win, Point(720.0, 45),80, 30, "Roll Dice")
        quitButton = Button(win, Point(720.0, 510),80, 30, "QUIT")
        rollButton.activate()
        quitButton.activate()

        pt = win.getMouse()

        while not quitButton.clicked(pt):

            for i in range(4):
                if i == 0:
                    if rollButton.clicked(pt):
                        print("red")
                        dice1, dice2 = self.rollDice(win)
                        if self.player.returnChips() > 0:
                            checkMove, dice = self.startHome(dice1, dice2, "red", win)
                            if checkMove:
                                sumDie = dice
                                self.player.MovePiece(self.players[0].player, sumDie, "red", remSteps.returnSteps(), win)          
                        elif self.player.returnChips() == 0:
                            sumDie = dice1 + dice2
                            self.player.MovePiece(self.players[0].player, sumDie, "red", remSteps.returnSteps(), win)
                        if self.playerWon(win):
                            win.getMouse()
                            win.close()
                        pt = win.getMouse()

                elif i == 1:
                    if rollButton.clicked(pt):
                        print("blue")
                        dice1, dice2 = self.rollDice( win)
                        if self.player.returnChips() > 0:
                            checkMove, dice = self.startHome(dice1, dice2, "blue", win)
                            if checkMove:
                                sumDie = dice
                                self.player.MovePiece(self.players[1].player, sumDie, "blue", remSteps.returnSteps(), win)
                                        
                        elif self.player.returnChips() == 0:
                            sumDie = dice1 + dice2
                            self.player.MovePiece(self.players[1].player, sumDie, "blue", remSteps.returnSteps(), win)
                                
                        if self.playerWon(win):
                            win.getMouse()
                            win.close()
                        pt = win.getMouse()

                
                elif i == 2:
                    if rollButton.clicked(pt):
                        print("green")
                        dice1, dice2 = self.rollDice(win)
                                
                        if self.player.returnChips() > 0:
                            checkMove, dice = self.startHome(dice1, dice2, "green", win)
                            if checkMove:
                                sumDie = dice
                                self.player.MovePiece(self.players[2].player, sumDie, "green", remSteps.returnSteps(), win)
                                        
                        elif self.player.returnChips() == 0:
                            sumDie = dice1 + dice2
                            self.player.MovePiece(self.players[2].player, sumDie, "green", remSteps.returnSteps(), win)
                                
                        if self.playerWon(win):
                            win.getMouse()
                            win.close()
                                        
                            pt = win.getMouse()

                elif i == 3:
                    if rollButton.clicked(pt):
                        print("yellow")
                        dice1, dice2 = self.rollDice(win)    
                        if self.player.returnChips() > 0:
                            checkMove, dice = self.startHome(dice1, dice2, "yellow", win)
                            if checkMove:
                                sumDie = dice
                                self.player.MovePiece(self.players[3].player, sumDie, "yellow", remSteps.returnSteps(), win)
                                    
                        elif self.player.returnChips() == 0:
                            sumDie = dice1 + dice2
                            self.player.MovePiece(self.players[3].player, sumDie, "yellow", remSteps.returnSteps(), win)
                        
                        if self.playerWon(win):
                            win.getMouse()
                            win.close()
                        
                        pt = win.getMouse()
                
                

                      
            
    def playerWon(self, win):

        playerPiece = self.player.returnRed()
        if self.player.piecesInHome(playerPiece):
            winner = Text(Point(720.0, 300), "You WON!")
            winner.setStyle("bold")
            winner.setSize(26)
            winner.draw(win)
            return True
        else:
            return False
            
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
        return diceVal, diceVal2

    def startHome(self, diceVal, diceVal2, color, win):

        if diceVal == 5 or diceVal2 == 5 and color == "red":        
            self.players[0].drawPlayer("red", win)
            if diceVal == 5:
                self.player.updateChips()
                return True, diceVal2
            else: 
                return True, diceVal
        if diceVal == 5 or diceVal2 == 5 and color == "blue":
            self.players[1].drawPlayer("blue", win)
            if diceVal == 5:
                self.player.updateChips()
                return True, diceVal2
            else: 
                return True, diceVal
        if diceVal == 5 or diceVal2 == 5 and color == "green":
            self.players[2].drawPlayer("green", win)
            if diceVal == 5:
                self.player.updateChips()
                return True, diceVal2
            else: 
                return True, diceVal
        if diceVal == 5 or diceVal2 == 5 and color == "yellow":
            self.players[3].drawPlayer("yellow", win)
            if diceVal == 5:
                self.player.updateChips()
                return True, diceVal2
            else: 
                return True, diceVal
        else:
            skip = Text(Point(720.0, 300), "Next player's turn")
            skip.setStyle("bold")
            skip.setSize(16)
            skip.draw(win)
            win.getMouse()
            skip.undraw()
                
            moveDice = diceVal + diceVal2
            return False, moveDice
                


        
        

