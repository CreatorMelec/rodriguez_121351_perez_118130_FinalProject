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
        self.availableChips = 1
        self.player = Circle(Point(0,0), 5)
        self.redPieces = 0
        self.remainingSteps = 60

    def returnChips(self):
        return self.availableChips

    def updateChips(self):
        self.availableChips = self.availableChips - 1

    def piecesInHome(self, playerPiece):
        if (playerPiece == self.homePieces):
            return True
        else:
            return False

    def updateSteps(self,takenSteps):
        
        self.remainingSteps -= takenSteps
        
    def returnSteps(self):
        return self.remainingSteps


    def MovePiece(self, circleOb ,diceVal,color,remSteps, win): #remSteps = 80
        while diceVal != 0:
            if 75 <= circleOb.getCenter().getX() < 255 and circleOb.getCenter().getY() == 255 and color == "red"  and 0 < self.returnSteps() <= 6:
                circleOb.move(30.0,0.0)
                diceVal -= 1
                if remSteps == 0:
                    self.redPieces += 1    
            
            if circleOb.getCenter().getX() == 285.0 and 45 <= circleOb.getCenter().getY() < 225 and color == "yellow" and 0 < self.returnSteps() <= 6:
                circleOb.move(0.0, 30.0)
                diceVal -= 1
                if remSteps == 0:
                    self.redPieces += 1

            if circleOb.getCenter().getX() == 285.0 and 285 < circleOb.getCenter().getY() <= 465 and color == "blue" and 0 < self.returnSteps() <= 6:
                circleOb.move(0.0, -30.0)
                diceVal -= 1
                if remSteps == 0:
                    self.redPieces += 1
                

            if 315 < circleOb.getCenter().getX() <= 495 and circleOb.getCenter().getY() == 255 and color == "green" and 0 < self.returnSteps() <= 6:
                circleOb.move(-30.0, 0.0)
                
                diceVal -= 1
                if remSteps == 0:
                    self.redPieces += 1

            

            elif  (75 < circleOb.getCenter().getX() <= 225) and circleOb.getCenter().getY() == 225.0:
                circleOb.move(-30,0)
                
                diceVal -= 1

            elif circleOb.getCenter().getX() == 75.0 and (225 <= circleOb.getCenter().getY() < 285.0):
                circleOb.move(0,30.0)
                
                diceVal -= 1

            elif circleOb.getCenter().getY() == 285.0 and (75 <= circleOb.getCenter().getX() < 225.0):
                circleOb.move(30.0, 0)
               
                diceVal -= 1

            elif circleOb.getCenter().getX() == 225 and circleOb.getCenter().getY() == 285.0:
                circleOb.move(30,30)
                
                diceVal -= 1
            
            elif circleOb.getCenter().getX() == 255.0 and (315 <= circleOb.getCenter().getY() < 465):
                circleOb.move(0,30)
                
                diceVal -= 1

            elif circleOb.getCenter().getY() == 465 and (255 <= circleOb.getCenter().getX() < 315):
                circleOb.move(30,0)
                
                diceVal -= 1

            elif circleOb.getCenter().getX() == 315.0 and (315 < circleOb.getCenter().getY() <= 465):
                circleOb.move(0,-30)
                
                diceVal -= 1

            elif circleOb.getCenter().getY() == 315 and (255 < circleOb.getCenter().getX() <= 315):
                circleOb.move(30,-30)
                
                diceVal -= 1

            elif (345 <= circleOb.getCenter().getX() < 495) and circleOb.getCenter().getY() == 285:
                circleOb.move(30,0)
                
                diceVal -= 1
            
            elif circleOb.getCenter().getX() == 495 and (225 < circleOb.getCenter().getY() <= 285):
                circleOb.move(0,-30)
                
                diceVal -= 1
            
            elif circleOb.getCenter().getY() == 225 and (345 < circleOb.getCenter().getX() <= 495):
                circleOb.move(-30,0)
                
                diceVal -= 1
            
            elif circleOb.getCenter().getX() == 345 and circleOb.getCenter().getY() == 225:
                circleOb.move(-30,-30)
                
                diceVal -= 1
            
            elif circleOb.getCenter().getX() == 315 and (45 < circleOb.getCenter().getY() <= 195):
                circleOb.move(0,-30)
                
                diceVal -= 1

            elif circleOb.getCenter().getY() == 45 and (255 < circleOb.getCenter().getX() <= 315):
                circleOb.move(-30,0)
                
                diceVal -= 1
            
            elif circleOb.getCenter().getX() == 255 and ( 45 <= circleOb.getCenter().getY () < 195):
                circleOb.move(0,30)
                
                diceVal -= 1

            elif circleOb.getCenter().getX() == 255 and circleOb.getCenter().getY() == 195:
                circleOb.move(-30,30)
               
                diceVal -= 1

            self.updateSteps(diceVal)



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

            
            
