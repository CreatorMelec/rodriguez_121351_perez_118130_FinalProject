from graphics import *
from Dice import Dice


class Game:

    def __init__(self):
        self.greenPlayer = 0
        self.greenPlayer2 = 0
        self.greenPlayer3 = 0
        self.greenPlayer4 = 0
        

    
    def gameInterface(self, win):

        intro = Text(Point(192.0,190.0),"Welcome to Parchessi")
        intro.draw(win)

    def drawPlayers(self, win):

        self.greenPlayers(win)
            
    def greenPlayers(self, win):

        self.greenPlayer = Circle(Point(66.0, 70.0), 8)
        self.greenPlayer.setFill("green")
        self.greenPlayer.setOutline("green")
        self.greenPlayer.draw(win)

        self.greenPlayer2 = Circle(Point(66.0, 110.0), 8)
        self.greenPlayer2.setFill("green")
        self.greenPlayer2.setOutline("green")
        self.greenPlayer2.draw(win)

        self.greenPlayer3 = Circle(Point(115.0, 70.0), 8)
        self.greenPlayer3.setFill("green")
        self.greenPlayer3.setOutline("green")
        self.greenPlayer3.draw(win)

        self.greenPlayer4 = Circle(Point(115.0, 110.0), 8)
        self.greenPlayer4.setFill("green")
        self.greenPlayer4.setOutline("green")
        self.greenPlayer4.draw(win)

    def movePlayer(self,win):
        
        self.greenPlayer.undraw()
        self.greenPlayer = Circle(Point(195.0, 95.0), 8)
        self.greenPlayer.setFill("green")
        self.greenPlayer.setOutline("green")
        self.greenPlayer.draw(win)

        win.getMouse()

        self.greenPlayer.undraw()
        self.greenPlayer = Circle(Point(195.0, 115.0), 8)
        self.greenPlayer.setFill("green")
        self.greenPlayer.setOutline("green")
        self.greenPlayer.draw(win)

    def board(self,win):

        #se dibuja rectangulo horizontal
        leftBase = Rectangle(Point(60.0, 210.0), Point(510.0,300.0))
        leftBase.draw(win)

        #lineas horizontales
        lineLeft = Line(Point(60.0, 240.0), Point(510.0, 240.0))
        lineLeft.draw(win)

        lineLeft2 = Line(Point(60.0, 270.0), Point(510.0, 270.0))
        lineLeft2.draw(win)

        #rectangulo vertical
        topBase = Rectangle(Point(240.0, 30.0), Point(330.0, 480.0))
        topBase.draw(win)

        #lineas verticales
        lineTop = Line(Point(270.0, 30.0), Point(270.0, 480.0))
        lineTop.draw(win)

        lineTop2 = Line(Point(300.0, 30.0), Point(300.0, 480.0))
        lineTop2.draw(win)

        #se dibuja linea para home de cada jugador
        homeLineRed = Rectangle(Point(60.0, 240.0), Point(240.0, 270.0))
        homeLineRed.setFill("red")
        homeLineRed.draw(win)

        homeLineGreen = Rectangle(Point(330.0, 240.0), Point(510.0, 270.0))
        homeLineGreen.setFill("Green")
        homeLineGreen.draw(win)

        homeLineYellow = Rectangle(Point(270.0, 30.0), Point(300.0, 210.0))
        homeLineYellow.setFill("yellow")
        homeLineYellow.draw(win)

        homeLineBlue = Rectangle(Point(270.0, 300.0), Point(300.0, 480.0))
        homeLineBlue.setFill("blue")
        homeLineBlue.draw(win)


        #dibujar posicion inicial de cada jugador
        homeRed = Rectangle(Point(90.0, 210.0), Point(120.0, 240.0))
        homeRed.setFill("cyan")
        homeRed.draw(win)

        homeGreen = Rectangle(Point(450.0, 270.0), Point(480.0, 300.0))
        homeGreen.setFill("cyan")
        homeGreen.draw(win)

        homeYellow = Rectangle(Point(300.0, 60.0), Point(330.0, 90.0))
        homeYellow.setFill("cyan")
        homeYellow.draw(win)

        homeBlue = Rectangle(Point(240.0, 420.0), Point(270.0, 450.0))
        homeBlue.setFill("cyan")
        homeBlue.draw(win)


     
        #se dibujan las lineas en X
        for x in range(60,510,30):
            p1 = Point(x,300)
            p2 = Point(x,210)
            line = Line(p1,p2)
            line.draw(win)


        #se dibujan las lineas en Y 
        for x in range(30,480,30):
            pt1 = Point(240,x)
            pt2 = Point(330,x)
            line2 = Line(pt1,pt2)
            line2.draw(win)


        #se dibuja las casas de cada jugador
        home1 = Rectangle(Point(90.0, 60.0), Point(190.0, 150.0))
        home1.setFill("red")
        home1.draw(win)

        home2 = Rectangle(Point(390.0, 360.0), Point(490.0, 450.0))
        home2.setFill("green")
        home2.draw(win)

        home3 = Rectangle(Point(390.0, 60.0), Point(490.0, 150.0))
        home3.setFill("yellow")
        home3.draw(win)

        home3 = Rectangle(Point(90.0, 360.0), Point(190.0, 450.0))
        home3.setFill("blue")
        home3.draw(win)

        #se pinta el home de cada jugador
        redBase = Polygon(Point(240.0, 210.0), Point(240.0, 300.0), Point(285.0,255.0))
        redBase.setFill("red")
        redBase.draw(win)

        greenBase = Polygon(Point(330.0, 210.0), Point(330.0, 300.0), Point(285.0, 255.0))
        greenBase.setFill("green")
        greenBase.draw(win)

        yellowBase = Polygon(Point(240.0, 210.0), Point(330.0, 210.0), Point(285.0, 255.0))
        yellowBase.setFill("yellow")
        yellowBase.draw(win)

        blueBase = Polygon(Point(240.0, 300.0), Point(330.0, 300.0 ), Point(285.0, 255.0))
        blueBase.setFill("blue")
        blueBase.draw(win)

        #se dibuja linea para dividir juego
        rightMenu = Line(Point(620.0, 0.0), Point(620.0, 620.0))
        rightMenu.draw(win)

        self.menuOption(win)
        self.drawPlayer(win)

    def menuOption(self, win):

        rollSquare = Rectangle(Point(680.0, 45.0), Point(760.0, 75.0))
        rollSquare.setFill("gray")
        rollSquare.draw(win)

        rollDice = Text(Point(720.0 ,60.0), "Roll Dice")
        rollDice.draw(win)

        quitSquare = Rectangle(Point(680.0, 510.0), Point(760.0, 540.0))
        quitSquare.setFill("gray")
        quitSquare.draw(win)

        quitButton = Text(Point(720.0 , 525.0), "Quit")
        quitButton.draw(win)

    def MovePiece(self, circleOb,diceVal,color,remSteps,win): #remSteps = 80
        while diceVal != 0:

            if 75 <= circleOb.getCenter().getX() < 255 and circleOb.getCenter().getY() == 255 and color == "red" and 0 < remSteps <= 6:
                movedCircle = Circle(Point(circleOb.getCenter().getX() + 30, circleOb.getCenter().getY()), 5)
                movedCircle.setFill(color)                
                circleOb.undraw()               
                movedCircle.draw(win)
                circleOb = movedCircle
                diceVal -= 1
                remSteps -= 1

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



    def drawPlayer(self, win):

        red1 = Circle(Point(105.0, 225.0), 5)
        red1.setFill("red")
        red1.setOutline("black")
        red1.draw(win)

        dado = Dice()
        dado.rollDie()
        diceVal = dado.diceValue()
        print(diceVal)

        self.MovePiece(red1, diceVal, "red", 60, win)


