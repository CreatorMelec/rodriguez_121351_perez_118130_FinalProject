from graphics import *
from chip import chip

# 64 para llegar a la base del home
# 7 rojos para llegar a home

class Player:

    def __init__(self):
        self.chips = []
        for x in range(4):
            self.chips.append(chip())
        self.availableChips = 1
        self.player = Circle(Point(0, 0), 5)
        self.pieces = 0
        self.remainingSteps = 60

    def returnChips(self):
        return self.availableChips

    def updateChips(self):
        self.availableChips = self.availableChips - 1

    def updateHome(self):
        self.pieces = self.pieces + 1

    def piecesInHome(self):
        return self.pieces

    def updateSteps(self, takenSteps):

        for i in range(takenSteps):
            self.remainingSteps -= 1

    def returnSteps(self):
        return self.remainingSteps

    def reset(self):
        self.availableChips = 1
        self.remainingSteps = 60

    def MovePiece(self, circleOb, diceVal, dice1, dice2, color, remSteps, win):  # remSteps = 80
        # self.updateSteps(diceVal)
        while diceVal != 0:

            finalSteps = self.returnSteps()
            # red home
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


            # yellow home
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



            elif circleOb.getCenter().getX() == 285.0 and 175 <= circleOb.getCenter().getY() < 255 and color == "yellow" and finalSteps == 2:
                if diceVal > 2:
                    diceVal = 0
                elif diceVal <= 2:
                    self.updateSteps(1)
                    circleOb.move(0.0, 30.0)
                    diceVal -= 1

            elif circleOb.getCenter().getX() == 285.0 and 205 <= circleOb.getCenter().getY() < 255 and color == "yellow" and finalSteps == 1:
                if dice1 > 1 and dice2 > 1:
                    diceVal = 0
                if dice1 == 1 or dice2 == 1 or diceVal == 1:
                    self.updateSteps(1)
                    circleOb.move(0.0,30.0)
                    self.updateHome()
                    diceVal = 0


            # blue home

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

    def playerWon(self, pieces, win):

        if pieces == 1:
            winner = Text(Point(720.0, 300), "You WON!")
            winner.setStyle("bold")
            winner.setSize(26)
            winner.draw(win)
            win.getMouse()
            win.close()
            return True
        else:
            return False
