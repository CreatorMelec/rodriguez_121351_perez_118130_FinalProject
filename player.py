"""Code created by Elimelec Rodriguez and Cedric Perez
This code introduces a very popular and known game, Parchessi or as some might know it, Trouble
in a simpler way, yet recognizable and fun way"""
#imports of all the classes used in this interactive game
from graphics import *

class Player:

    def __init__(self):
        self.availableChips = 1 #creates the variable for available chips for each player
        self.player = Circle(Point(0, 0), 5) #player initiated before creation in their home position
        self.pieces = 0 #variable to keep track of the pieces that made it to their home base
        self.remainingSteps = 60 #variable that holds available steps on the board
 
    def returnChips(self): #returns the chips the player has
        return self.availableChips

    def updateChips(self): #updates the chips once taken out of the home for each player
        self.availableChips = self.availableChips - 1

    def updateHome(self): #update the piece count once the chip made it to their home
        self.pieces = self.pieces + 1

    def piecesInHome(self): #returns how many pieces are in their home base
        return self.pieces

    def updateSteps(self, takenSteps): #updates the remaining steps for each player after a move
        for i in range(takenSteps):
            self.remainingSteps -= 1

    def returnSteps(self): #returns the players remaining steps
        return self.remainingSteps

    def reset(self): #resets the players chips and steps if eaten
        self.availableChips = 1
        self.remainingSteps = 60

    #function that move the player calling on the board using the dice values and their remainging steps
    def MovePiece(self, circleOb, diceVal, dice1, dice2, color, remSteps, win):
        while diceVal != 0:
            finalSteps = self.returnSteps()
            #moves the player red in their home row
            if 75 <= circleOb.getCenter().getX() < 255 and circleOb.getCenter().getY() == 255 and color == "red" and finalSteps == 6:
                if dice1 > 6 and dice2 > 6:
                    diceVal = 0
                elif diceVal <= 6:
                    self.updateSteps(1)
                    circleOb.move(30.0, 0.0)
                    diceVal -= 1

            elif 105 <= circleOb.getCenter().getX() < 255 and circleOb.getCenter().getY() == 255 and color == "red" and finalSteps == 5:
                if diceVal > 5:
                    diceVal = 0
                    self.updateSteps(0)
                elif diceVal <= 5:
                    self.updateSteps(1)
                    circleOb.move(30.0, 0.0)
                    diceVal -= 1

            elif 135 <= circleOb.getCenter().getX() < 255 and circleOb.getCenter().getY() == 255 and color == "red" and finalSteps == 4:
                if diceVal > 4:
                    diceVal = 0
                    self.updateSteps(0)
                elif diceVal <= 4:
                    self.updateSteps(1)
                    circleOb.move(30.0, 0.0)
                    diceVal -= 1

            elif 165 <= circleOb.getCenter().getX() < 255 and circleOb.getCenter().getY() == 255 and color == "red" and finalSteps == 3:
                if diceVal > 3:
                    diceVal = 0
                    self.updateSteps(0)
                elif diceVal <= 3:
                    self.updateSteps(1)
                    circleOb.move(30.0, 0.0)
                    diceVal -= 1

            elif 195 <= circleOb.getCenter().getX() < 255 and circleOb.getCenter().getY() == 255 and color == "red" and finalSteps == 2:
                if diceVal > 2:
                    diceVal = 0
                    self.updateSteps(0)
                elif diceVal <= 2:
                    self.updateSteps(1)
                    circleOb.move(30.0, 0.0)
                    diceVal -= 1

            elif 225 <= circleOb.getCenter().getX() < 255 and circleOb.getCenter().getY() == 255 and color == "red" and finalSteps == 1:
                if dice1 > 1 and dice2 > 1:
                    diceVal = 0
                elif dice1 == 1 or dice2 == 1 or diceVal == 1:
                    self.updateSteps(1)
                    circleOb.move(30.0,0.0)
                    self.updateHome()
                    diceVal = 0
            #moves the player blue in their home row
            elif circleOb.getCenter().getX() == 285.0 and 285 < circleOb.getCenter().getY() <= 465 and color == "blue" and finalSteps == 6:
                if diceVal > 6:
                    diceVal = 0
                    self.updateSteps(0)
                elif diceVal <= 6:
                    self.updateSteps(1)
                    circleOb.move(0.0, -30.0)
                    diceVal -= 1

            elif circleOb.getCenter().getX() == 285.0 and 285 < circleOb.getCenter().getY() <= 435 and color == "blue" and finalSteps == 5:
                if diceVal > 5:
                    diceVal = 0
                    self.updateSteps(0)
                elif diceVal <= 5:
                    self.updateSteps(1)
                    circleOb.move(0.0, -30.0)
                    diceVal -= 1

            elif circleOb.getCenter().getX() == 285.0 and 285 < circleOb.getCenter().getY() <= 405 and color == "blue" and finalSteps == 4:
                if diceVal > 4:
                    diceVal = 0
                elif diceVal <= 4:
                    self.updateSteps(1)
                    circleOb.move(0.0, -30.0)
                    diceVal -= 1

            elif circleOb.getCenter().getX() == 285.0 and 285 < circleOb.getCenter().getY() <= 375 and color == "blue" and finalSteps == 3:
                if diceVal > 3:
                    diceVal = 0
                elif diceVal <= 3:
                    self.updateSteps(1)
                    circleOb.move(0.0, -30.0)
                    diceVal -= 1

            elif circleOb.getCenter().getX() == 285.0 and 285 < circleOb.getCenter().getY() <= 345 and color == "blue" and finalSteps == 2:
                if diceVal > 2:
                    diceVal = 0
                elif diceVal <= 2:
                    self.updateSteps(1)
                    circleOb.move(0.0, -30.0)
                    diceVal -= 1

            elif circleOb.getCenter().getX() == 285.0 and 285 < circleOb.getCenter().getY() <= 315 and color == "blue" and finalSteps == 1:
                if dice1 > 1 and dice2 > 1:
                    diceVal = 0
                if dice1 == 1 or dice2 == 1 or diceVal == 1:
                    self.updateSteps(1)
                    circleOb.move(0.0,-30.0)
                    self.updateHome()
                    diceVal = 0
            #moves the player green in their home row
            elif 315 < circleOb.getCenter().getX() <= 495 and circleOb.getCenter().getY() == 255 and color == "green" and finalSteps == 6:
                if diceVal > 6:
                    diceVal = 0
                    self.updateSteps(0)
                elif diceVal <= 6:
                    self.updateSteps(1)
                    circleOb.move(-30.0, 0.0)
                    diceVal -= 1

            elif 315 < circleOb.getCenter().getX() <= 495 and circleOb.getCenter().getY() == 255 and color == "green" and finalSteps == 5:
                if diceVal > 5:
                    diceVal = 0
                    self.updateSteps(0)
                elif diceVal <= 5:
                    self.updateSteps(1)
                    circleOb.move(-30.0, 0.0)
                    diceVal -= 1

            elif 315 < circleOb.getCenter().getX() <= 495 and circleOb.getCenter().getY() == 255 and color == "green" and finalSteps == 4:
                if diceVal > 4:
                    diceVal = 0
                elif diceVal <= 4:
                    self.updateSteps(1)
                    circleOb.move(-30.0, 0.0)
                    diceVal -= 1

            elif 315 < circleOb.getCenter().getX() <= 495 and circleOb.getCenter().getY() == 255 and color == "green" and finalSteps == 3:
                if diceVal > 3:
                    diceVal = 0
                elif diceVal <= 3:
                    self.updateSteps(1)
                    circleOb.move(-30.0, 0.0)
                    diceVal -= 1

            elif 315 < circleOb.getCenter().getX() <= 495 and circleOb.getCenter().getY() == 255 and color == "green" and finalSteps == 2:
                if diceVal > 2:
                    diceVal = 0
                elif diceVal <= 2:
                    self.updateSteps(1)
                    circleOb.move(-30.0, 0.0)
                    diceVal -= 1

            elif 315 < circleOb.getCenter().getX() <= 496 and circleOb.getCenter().getY() == 255 and color == "green" and finalSteps == 1:
                if dice1 > 1 and dice2 > 1:
                    diceVal = 0
                if dice1 == 1 or dice2 == 1 or diceVal == 1:
                    self.updateSteps(1)
                    circleOb.move(-30.0,0.0)
                    self.updateHome()
                    diceVal = 0

            #moves the player yellow in their home row
            elif circleOb.getCenter().getX() == 285.0 and 45 <= circleOb.getCenter().getY() < 225 and color == "yellow" and finalSteps == 6:
                if diceVal > 6:
                    diceVal = 0
                    self.updateSteps(0)
                elif diceVal <= 6:
                    self.updateSteps(1)
                    circleOb.move(0.0, 30.0)
                    diceVal -= 1


            elif circleOb.getCenter().getX() == 285.0 and 75 <= circleOb.getCenter().getY() < 255 and color == "yellow" and finalSteps == 5:
                if diceVal > 5:
                    diceVal = 0
                    self.updateSteps(0)
                elif diceVal <= 5:
                    self.updateSteps(1)
                    circleOb.move(0.0, 30.0)
                    diceVal -= 1

            elif circleOb.getCenter().getX() == 285.0 and 105 <= circleOb.getCenter().getY() < 255 and color == "yellow" and finalSteps == 4:
                if diceVal > 4:
                    diceVal = 0
                elif diceVal <= 4:
                    self.updateSteps(1)
                    circleOb.move(0.0, 30.0)
                    diceVal -= 1

            elif circleOb.getCenter().getX() == 285.0 and 135 <= circleOb.getCenter().getY() < 255 and color == "yellow" and finalSteps == 3:
                if diceVal > 3:
                    diceVal = 0
                elif diceVal <= 3:
                    self.updateSteps(1)
                    circleOb.move(0.0, 30.0)
                    diceVal -= 1

            elif circleOb.getCenter().getX() == 285.0 and 165 <= circleOb.getCenter().getY() < 255 and color == "yellow" and finalSteps == 2:
                if diceVal > 2:
                    diceVal = 0
                elif diceVal <= 2:
                    self.updateSteps(1)
                    circleOb.move(0.0, 30.0)
                    diceVal -= 1

            elif circleOb.getCenter().getX() == 285.0 and 195 <= circleOb.getCenter().getY() < 255 and color == "yellow" and finalSteps == 1:
                if dice1 > 1 and dice2 > 1:
                    diceVal = 0
                if dice1 == 1 or dice2 == 1 or diceVal == 1:
                    self.updateSteps(1)
                    circleOb.move(0.0,30.0)
                    self.updateHome()
                    diceVal = 0

            #normal moves on the board
            elif (75 < circleOb.getCenter().getX() <= 225) and circleOb.getCenter().getY() == 225.0:
                self.updateSteps(1)
                circleOb.move(-30, 0)
                diceVal -= 1

            elif circleOb.getCenter().getX() == 75.0 and (225 <= circleOb.getCenter().getY() < 285.0):
                self.updateSteps(1)
                circleOb.move(0, 30.0)
                diceVal -= 1

            elif circleOb.getCenter().getY() == 285.0 and (75 <= circleOb.getCenter().getX() < 225.0):
                self.updateSteps(1)
                circleOb.move(30.0, 0)
                diceVal -= 1

            elif circleOb.getCenter().getX() == 225 and circleOb.getCenter().getY() == 285.0:
                self.updateSteps(1)
                circleOb.move(30, 30)
                diceVal -= 1

            elif circleOb.getCenter().getX() == 255.0 and (315 <= circleOb.getCenter().getY() < 465):
                self.updateSteps(1)
                circleOb.move(0, 30)
                diceVal -= 1

            elif circleOb.getCenter().getY() == 465 and (255 <= circleOb.getCenter().getX() < 315):
                self.updateSteps(1)
                circleOb.move(30, 0)
                diceVal -= 1

            elif circleOb.getCenter().getX() == 315.0 and (315 < circleOb.getCenter().getY() <= 465):
                self.updateSteps(1)
                circleOb.move(0, -30)
                diceVal -= 1

            elif circleOb.getCenter().getY() == 315 and (255 < circleOb.getCenter().getX() <= 315):
                self.updateSteps(1)
                circleOb.move(30, -30)
                diceVal -= 1

            elif (345 <= circleOb.getCenter().getX() < 495) and circleOb.getCenter().getY() == 285:
                self.updateSteps(1)
                circleOb.move(30, 0)
                diceVal -= 1

            elif circleOb.getCenter().getX() == 495 and (225 < circleOb.getCenter().getY() <= 285):
                self.updateSteps(1)
                circleOb.move(0, -30)
                diceVal -= 1

            elif circleOb.getCenter().getY() == 225 and (345 < circleOb.getCenter().getX() <= 495):
                self.updateSteps(1)
                circleOb.move(-30, 0)
                diceVal -= 1

            elif circleOb.getCenter().getX() == 345 and circleOb.getCenter().getY() == 225:
                self.updateSteps(1)
                circleOb.move(-30, -30)
                diceVal -= 1

            elif circleOb.getCenter().getX() == 315 and (45 < circleOb.getCenter().getY() <= 195):
                self.updateSteps(1)
                circleOb.move(0, -30)
                diceVal -= 1

            elif circleOb.getCenter().getY() == 45 and (255 < circleOb.getCenter().getX() <= 315):
                self.updateSteps(1)
                circleOb.move(-30, 0)
                diceVal -= 1

            elif circleOb.getCenter().getX() == 255 and (45 <= circleOb.getCenter().getY() < 195):
                self.updateSteps(1)
                circleOb.move(0, 30)
                diceVal -= 1

            elif circleOb.getCenter().getX() == 255 and circleOb.getCenter().getY() == 195:
                self.updateSteps(1)
                circleOb.move(-30, 30)
                diceVal -= 1

    #function that draws the player on their starting position 
    def drawPlayer(self, color, win):
        if color == "red":
            self.player = Circle(Point(105.0, 225.0), 5)
            self.player.setFill(color)
            self.player.setOutline("black")
            self.player.draw(win)
        elif color == "blue":
            self.player = Circle(Point(255.0, 435.0), 5)
            self.player.setFill(color)
            self.player.setOutline("black")
            self.player.draw(win)
        elif color == "green":
            self.player = Circle(Point(465.0, 285.0), 5)
            self.player.setFill(color)
            self.player.setOutline("black")
            self.player.draw(win)
        elif color == "yellow":
            self.player = Circle(Point(315.0, 75.0), 5)
            self.player.setFill(color)
            self.player.setOutline("black")
            self.player.draw(win)

    #function that checks the pieces in home and returns if the player won
    def playerWon(self, pieces, color, win):
        if pieces == 1:
            winner = Text(Point(720.0, 300), str(color) + " player WON!")
            winner.setStyle("bold")
            winner.setSize(14)
            winner.draw(win)
            return True
        else:
            return False
