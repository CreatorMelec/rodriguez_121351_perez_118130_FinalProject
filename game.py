from graphics import *
from Dice import Dice
from dieview import DieView
from player import Player
from Buttons import Button
from board import Board


class Game:

    def __init__(self):
        self.player = Player()
        self.players = []
        for x in range(4):
            self.players.append(Player())
        self.board = Board()

    def playGame(self, win):

        rollButton = Button(win, Point(720.0, 45), 80, 30, "Roll Dice")
        quitButton = Button(win, Point(720.0, 510), 80, 30, "QUIT")
        rollButton.activate()
        quitButton.activate()

        pt = win.getMouse()
        turn = 0
        counter = 0

        while not quitButton.clicked(pt):

            if turn == 0:
                if rollButton.clicked(pt):
                    self.board.playerTurn("Red",win)
                    dice1, dice2 = self.rollDice(win)
                    if self.players[0].returnChips() > 0:
                        checkMove, dice = self.startHome(dice1, dice2, "red", win)
                        if checkMove:
                            self.players[0].MovePiece(self.players[0].player, dice, dice1,dice2, "red", self.players[0].returnSteps(),win)
                            self.eatPlayer("red", win)

                    elif self.players[0].returnChips() == 0:
                        dice = dice1 + dice2
                        self.players[0].MovePiece(self.players[0].player, dice, dice1,dice2, "red", self.players[0].returnSteps(),win)
                        self.eatPlayer("red", win)

                    if self.doubleTurn(dice1, dice2):
                        counter += 1
                        turn = 0
                        turnAgain = Text(Point(720.0, 300), "Your turn again")
                        turnAgain.setStyle("bold")
                        turnAgain.setSize(16)
                        turnAgain.draw(win)
                        win.getMouse()
                        turnAgain.undraw()

                        if counter == 2:
                            turn += 1
                            counter = 0
                            skip = Text(Point(720.0, 300), "Next player's turn")
                            skip.setStyle("bold")
                            skip.setSize(16)
                            skip.draw(win)
                            win.getMouse()
                            skip.undraw()                  
                    else:
                        turn += 1
                        counter = 0
                        skip = Text(Point(720.0, 300), "Next player's turn")
                        skip.setStyle("bold")
                        skip.setSize(16)
                        skip.draw(win)
                        win.getMouse()
                        skip.undraw()

                    if self.players[0].playerWon(self.players[0].piecesInHome(), win):
                        win.getMouse()
                        win.close()

                    pt = win.getMouse()

            elif turn == 1:

                if rollButton.clicked(pt):
                    self.board.playerTurn("Blue",win)
                    dice1, dice2 = self.rollDice(win)
                    if self.players[1].returnChips() > 0:
                        checkMove, dice = self.startHome(dice1, dice2, "blue", win)
                        if checkMove:
                            self.players[1].MovePiece(self.players[1].player, dice, dice1,dice2, "blue",self.players[1].returnSteps(), win)
                            self.eatPlayer("blue", win)

                    elif self.players[1].returnChips() == 0:
                        self.players[1].MovePiece(self.players[1].player, dice, dice1,dice2, "blue", self.players[1].returnSteps(),win)
                        self.eatPlayer("blue", win)

                    if self.doubleTurn(dice1, dice2):
                        counter += 1
                        turn = 1
                        turnAgain = Text(Point(720.0, 300), "Your turn again")
                        turnAgain.setStyle("bold")
                        turnAgain.setSize(16)
                        turnAgain.draw(win)
                        win.getMouse()
                        turnAgain.undraw()
                        if counter == 2:
                            turn += 1
                            counter = 0
                            skip = Text(Point(720.0, 300), "Next player's turn")
                            skip.setStyle("bold")
                            skip.setSize(16)
                            skip.draw(win)
                            win.getMouse()
                            skip.undraw()
                        
                    else:
                        turn += 1
                        counter = 0
                        skip = Text(Point(720.0, 300), "Next player's turn")
                        skip.setStyle("bold")
                        skip.setSize(16)
                        skip.draw(win)
                        win.getMouse()
                        skip.undraw()

                    if self.players[1].playerWon(self.players[1].piecesInHome(), win):
                        win.getMouse()
                        win.close()

                    pt = win.getMouse()



            elif turn == 2:

                if rollButton.clicked(pt):
                    self.board.playerTurn("Green",win)
                    dice1, dice2 = self.rollDice(win)
                    if self.players[2].returnChips() > 0:
                        checkMove, dice = self.startHome(dice1, dice2, "green", win)
                        if checkMove:
                            self.players[2].MovePiece(self.players[2].player, dice, dice1,dice2, "green",self.players[2].returnSteps(), win)
                            self.eatPlayer("green", win)

                    elif self.players[2].returnChips() == 0:
                        dice = dice1 + dice2
                        self.players[2].MovePiece(self.players[2].player, dice, dice1,dice2, "green", self.players[2].returnSteps(),win)
                        self.eatPlayer("green", win)

                    if self.doubleTurn(dice1, dice2):
                        counter += 1
                        turn = 2
                        turnAgain = Text(Point(720.0, 300), "Your turn again")
                        turnAgain.setStyle("bold")
                        turnAgain.setSize(16)
                        turnAgain.draw(win)
                        win.getMouse()
                        turnAgain.undraw()
                        if counter == 2:
                            turn += 1
                            counter = 0
                            skip = Text(Point(720.0, 300), "Next player's turn")
                            skip.setStyle("bold")
                            skip.setSize(16)
                            skip.draw(win)
                            win.getMouse()
                            skip.undraw()
                        
                    else:
                        turn += 1
                        counter = 0
                        skip = Text(Point(720.0, 300), "Next player's turn")
                        skip.setStyle("bold")
                        skip.setSize(16)
                        skip.draw(win)
                        win.getMouse()
                        skip.undraw()

                    if self.players[2].playerWon(self.players[2].piecesInHome(), win):
                        win.getMouse()
                        win.close()

                    pt = win.getMouse()



            elif turn == 3:

                if rollButton.clicked(pt):
                    self.board.playerTurn("Yellow",win)
                    dice1, dice2 = self.rollDice(win)
                    if self.players[3].returnChips() > 0:
                        checkMove, dice = self.startHome(dice1, dice2, "yellow", win)
                        if checkMove:
                            self.players[3].MovePiece(self.players[3].player, dice, dice1,dice2, "yellow",self.players[3].returnSteps(), win)
                            self.eatPlayer("yellow", win)

                    elif self.players[3].returnChips() == 0:
                        self.players[3].MovePiece(self.players[3].player, dice, dice1,dice2, "yellow", self.players[3].returnSteps(),win)
                        self.eatPlayer("yellow", win)

                    if self.doubleTurn(dice1, dice2):
                        counter += 1
                        turn = 3
                        turnAgain = Text(Point(720.0, 300), "Your turn again")
                        turnAgain.setStyle("bold")
                        turnAgain.setSize(16)
                        turnAgain.draw(win)
                        win.getMouse()
                        turnAgain.undraw()
                        if counter == 2:
                            turn += 1
                            counter = 0
                            skip = Text(Point(720.0, 300), "Next player's turn")
                            skip.setStyle("bold")
                            skip.setSize(16)
                            skip.draw(win)
                            win.getMouse()
                            skip.undraw()
                        
                    else:
                        turn += 1
                        counter = 0
                        skip = Text(Point(720.0, 300), "Next player's turn")
                        skip.setStyle("bold")
                        skip.setSize(16)
                        skip.draw(win)
                        win.getMouse()
                        skip.undraw()

                    if self.players[3].playerWon(self.players[3].piecesInHome(), win):
                        win.getMouse()
                        win.close()

                    pt = win.getMouse()


            elif turn == 4:
                turn = 0

                pt = win.getMouse()

    def rollDice(self, win):

        dado = Dice()
        dado.rollDie()
        diceVal = dado.diceValue()
        viewDice = DieView(win, Point(690.0, 120.0), 50)
        viewDice.setValue(diceVal)
        dado.rollDie()
        diceVal2 = dado.diceValue()
        viewDice2 = DieView(win, Point(760.0, 120.0), 50)
        viewDice2.setValue(diceVal2)
        return diceVal, diceVal2

    def startHome(self, diceVal, diceVal2, color, win):

        if diceVal == 5 or diceVal2 == 5:
            if color == "red":
                self.players[0].drawPlayer("red", win)
                if diceVal == 5:
                    self.players[0].updateChips()
                    return True, diceVal2
                else:
                    self.players[0].updateChips()
                    return True, diceVal
            elif color == "blue":
                self.players[1].drawPlayer("blue", win)
                if diceVal == 5:
                    self.players[1].updateChips()
                    return True, diceVal2
                else:
                    self.players[1].updateChips()
                    return True, diceVal
            elif color == "green":
                self.players[2].drawPlayer("green", win)
                if diceVal == 5:
                    self.players[2].updateChips()
                    return True, diceVal2
                else:
                    self.players[2].updateChips()
                    return True, diceVal
            elif color == "yellow":
                self.players[3].drawPlayer("yellow", win)
                if diceVal == 5:
                    self.players[3].updateChips()
                    return True, diceVal2
                else:
                    self.players[3].updateChips()
                    return True, diceVal   
        else:
        
            moveDice = diceVal + diceVal2
            return False, moveDice

    def doubleTurn(self, dice1, dice2):

        if dice1 == dice2:
            return True
        else:
            return False

    def eatPlayer(self, color, win):
        if color == "red":
            if self.players[0].player.getCenter().getX() == self.players[1].player.getCenter().getX() and self.players[
                0].player.getCenter().getY() == self.players[1].player.getCenter().getY():
                self.players[1].player.undraw()
                self.players[1].reset()
                self.players[1] = Player()
                self.eatenMessage("Blue",win)
            elif self.players[0].player.getCenter().getX() == self.players[2].player.getCenter().getX() and \
                    self.players[0].player.getCenter().getY() == self.players[2].player.getCenter().getY():
                self.players[2].player.undraw()
                self.players[2].reset()
                self.players[2] = Player()
                self.eatenMessage("Green",win)
            elif self.players[0].player.getCenter().getX() == self.players[3].player.getCenter().getX() and \
                    self.players[0].player.getCenter().getY() == self.players[3].player.getCenter().getY():
                self.players[3].player.undraw()
                self.players[3].reset()
                self.players[3] = Player()
                self.eatenMessage("Yellow",win)
        elif color == "blue":
            if self.players[1].player.getCenter().getX() == self.players[0].player.getCenter().getX() and self.players[
                1].player.getCenter().getY() == self.players[0].player.getCenter().getY():
                self.players[0].player.undraw()
                self.players[0].reset()
                self.players[0] = Player()
                self.eatenMessage("Red",win)
            elif self.players[1].player.getCenter().getX() == self.players[2].player.getCenter().getX() and \
                    self.players[1].player.getCenter().getY() == self.players[2].player.getCenter().getY():
                self.players[2].player.undraw()
                self.players[2].reset()
                self.players[2] = Player()
                self.eatenMessage("Green",win)
            elif self.players[1].player.getCenter().getX() == self.players[3].player.getCenter().getX() and \
                    self.players[1].player.getCenter().getY() == self.players[3].player.getCenter().getY():
                self.players[3].player.undraw()
                self.players[3].reset()
                self.players[3] = Player()
                self.eatenMessage("Yellow",win)
        elif color == "green":
            if self.players[2].player.getCenter().getX() == self.players[0].player.getCenter().getX() and self.players[
                2].player.getCenter().getY() == self.players[0].player.getCenter().getY():
                self.players[0].player.undraw()
                self.players[0].reset()
                self.players[0] = Player()
                self.eatenMessage("Red",win)
            elif self.players[2].player.getCenter().getX() == self.players[1].player.getCenter().getX() and \
                    self.players[2].player.getCenter().getY() == self.players[1].player.getCenter().getY():
                self.players[1].player.undraw()
                self.players[1].reset()
                self.players[1] = Player()
                self.eatenMessage("Blue",win)
            elif self.players[2].player.getCenter().getX() == self.players[3].player.getCenter().getX() and \
                    self.players[2].player.getCenter().getY() == self.players[3].player.getCenter().getY():
                self.players[3].player.undraw()
                self.players[3].reset()
                self.players[3] = Player()
                self.eatenMessage("Yellow",win)

        elif color == "yellow":
            if self.players[3].player.getCenter().getX() == self.players[0].player.getCenter().getX() and self.players[
                3].player.getCenter().getY() == self.players[0].player.getCenter().getY():
                self.players[0].player.undraw()
                self.players[0].reset()
                self.players[0] = Player()
                self.eatenMessage("Red",win)
            elif self.players[3].player.getCenter().getX() == self.players[2].player.getCenter().getX() and \
                    self.players[3].player.getCenter().getY() == self.players[2].player.getCenter().getY():
                self.players[2].player.undraw()
                self.players[2].reset()
                self.players[2] = Player()
                self.eatenMessage("Green",win)
            elif self.players[3].player.getCenter().getX() == self.players[1].player.getCenter().getX() and \
                    self.players[3].player.getCenter().getY() == self.players[1].player.getCenter().getY():
                self.players[1].player.undraw()
                self.players[1].reset()
                self.players[1] = Player()
                self.eatenMessage("Blue",win)

    def eatenMessage(self, color, win):
        eat = Text(Point(720.0, 300), str(color) + " Player Eaten")
        eat.setStyle("bold")
        eat.setSize(16)
        eat.draw(win)
        win.getMouse()
        eat.undraw()

    def oneDice(self, dice1, dice2):
        if dice1 or dice2 == 1:
            if dice1 == 1:
                return True, dice1
            elif dice2 == 1:
                return True, dice2
        else:
            return False, dice1




