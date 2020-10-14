from graphics import *

from chip import chip
#64 para llegar a la base del home
#7 rojos para llegar a home

class Player:

    def __init__(self):
        self.chips = []
        for x in range(4):
            self.chips.append(chip())
        self.homePieces = 1
        self.availableChips = 4
        self.baseChips = 4
        self.player = Circle(Point(0,0), 5)
        self.redPieces = 0


    def returnBaseChips(self):
        return self.baseChips

    def updateBaseChips(self):
        self.baseChips = self.baseChips - 1

    def returnChips(self):
        return self.availableChips

    def updateChips(self):
        self.availableChips = self.availableChips - 1

    def piecesInHome(self, playerPiece):
        if (playerPiece == self.homePieces):
            return True
        else:
            return False

    def MovePiece(self, circleOb,diceVal,color,remSteps, win): #remSteps = 80
        while diceVal != 0:

            if 75 <= circleOb.getCenter().getX() < 255 and circleOb.getCenter().getY() == 255 and color == "red" and 0 < remSteps <= 6:
                movedCircle = Circle(Point(circleOb.getCenter().getX() + 30, circleOb.getCenter().getY()), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1
                if remSteps == 0:
                    self.redPieces += 1
                
            
            if circleOb.getCenter().getX() == 285.0 and 45 <= circleOb.getCenter().getY() < 225 and color == "yellow" and 0 < remSteps <= 6:
                movedCircle = Circle(Point(circleOb.getCenter().getX(), circleOb.getCenter().getY() + 30), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1
                if remSteps == 0:
                    self.redPieces += 1

            if circleOb.getCenter().getX() == 285.0 and 285 < circleOb.getCenter().getY() <= 465 and color == "blue" and 0 < remSteps <= 6:
                movedCircle = Circle(Point(circleOb.getCenter().getX(), circleOb.getCenter().getY() - 30), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1
                if remSteps == 0:
                    self.redPieces += 1
                

            if 315 < circleOb.getCenter().getX() <= 495 and circleOb.getCenter().getY() == 255 and color == "green" and 0 < remSteps <= 6:
                movedCircle = Circle(Point(circleOb.getCenter().getX() - 30, circleOb.getCenter().getY()), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1
                if remSteps == 0:
                    self.redPieces += 1

            

            elif  (75 < circleOb.getCenter().getX() <= 225) and circleOb.getCenter().getY() == 225.0:
                    movedCircle = Circle(Point(circleOb.getCenter().getX() - 30, circleOb.getCenter().getY()), 5)
                    movedCircle.setFill(color)                
                    circleOb.undraw()               
                    movedCircle.draw(win)
                    circleOb = movedCircle
                    diceVal -= 1
                    remSteps -= 1

            elif circleOb.getCenter().getX() == 75.0 and (225 <= circleOb.getCenter().getY() < 285.0):
                    movedCircle = Circle(Point(circleOb.getCenter().getX(), circleOb.getCenter().getY() + 30), 5)
                    movedCircle.setFill(color)               
                    circleOb.undraw()                
                    movedCircle.draw(win)
                    circleOb = movedCircle
                    diceVal -= 1
                    remSteps -= 1

            elif circleOb.getCenter().getY() == 285.0 and (75 <= circleOb.getCenter().getX() < 225.0):
                    movedCircle = Circle(Point(circleOb.getCenter().getX() + 30, circleOb.getCenter().getY()), 5)
                    movedCircle.setFill(color)                
                    circleOb.undraw()               
                    movedCircle.draw(win)
                    circleOb = movedCircle
                    diceVal -= 1
                    remSteps -= 1

            elif circleOb.getCenter().getX() == 225 and circleOb.getCenter().getY() == 285.0:
                movedCircle = Circle(Point(circleOb.getCenter().getX() + 30, circleOb.getCenter().getY() + 30), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1
            
            elif circleOb.getCenter().getX() == 255.0 and (315 <= circleOb.getCenter().getY() < 465):
                movedCircle = Circle(Point(circleOb.getCenter().getX(), circleOb.getCenter().getY() + 30), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1

            elif circleOb.getCenter().getY() == 465 and (255 <= circleOb.getCenter().getX() < 315):
                movedCircle = Circle(Point(circleOb.getCenter().getX() + 30, circleOb.getCenter().getY()), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1

            elif circleOb.getCenter().getX() == 315.0 and (315 < circleOb.getCenter().getY() <= 465):
                movedCircle = Circle(Point(circleOb.getCenter().getX(), circleOb.getCenter().getY() - 30), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1

            elif circleOb.getCenter().getY() == 315 and (255 < circleOb.getCenter().getX() <= 315):
                movedCircle = Circle(Point(circleOb.getCenter().getX() + 30, circleOb.getCenter().getY() - 30), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1

            elif (345 <= circleOb.getCenter().getX() < 495) and circleOb.getCenter().getY() == 285:
                movedCircle = Circle(Point(circleOb.getCenter().getX() + 30, circleOb.getCenter().getY()), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1
            
            elif circleOb.getCenter().getX() == 495 and (225 < circleOb.getCenter().getY() <= 285):
                movedCircle = Circle(Point(circleOb.getCenter().getX(), circleOb.getCenter().getY() - 30), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1
            
            elif circleOb.getCenter().getY() == 225 and (345 < circleOb.getCenter().getX() <= 495):
                movedCircle = Circle(Point(circleOb.getCenter().getX() - 30, circleOb.getCenter().getY()), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1
            
            elif circleOb.getCenter().getX() == 345 and circleOb.getCenter().getY() == 225:
                movedCircle = Circle(Point(circleOb.getCenter().getX() - 30, circleOb.getCenter().getY() - 30), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1
            
            elif circleOb.getCenter().getX() == 315 and (45 < circleOb.getCenter().getY() <= 195):
                movedCircle = Circle(Point(circleOb.getCenter().getX(), circleOb.getCenter().getY() - 30), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1

            elif circleOb.getCenter().getY() == 45 and (255 < circleOb.getCenter().getX() <= 315):
                movedCircle = Circle(Point(circleOb.getCenter().getX() - 30, circleOb.getCenter().getY()), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1
            
            elif circleOb.getCenter().getX() == 255 and ( 45 <= circleOb.getCenter().getY () < 195):
                movedCircle = Circle(Point(circleOb.getCenter().getX(), circleOb.getCenter().getY() + 30), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1

            elif circleOb.getCenter().getX() == 255 and circleOb.getCenter().getY() == 195:
                movedCircle = Circle(Point(circleOb.getCenter().getX() - 30, circleOb.getCenter().getY() + 30), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1


            


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


    def returnRed(self):
        return self.redPieces

            
            
