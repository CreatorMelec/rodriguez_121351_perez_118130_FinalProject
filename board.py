from graphics import * 
from Buttons import Button

class Board:

    def __init__(self):
        pass

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


    def playerTurn(self, color, win):
        player = Text(Point(720.0, 300), str(color) + "'s Turn")
        player.setStyle("bold")
        player.setSize(16)
        player.draw(win)
        win.getMouse()
        player.undraw()
   