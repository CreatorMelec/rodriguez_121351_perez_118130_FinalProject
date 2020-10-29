"""Code created by Elimelec Rodriguez and Cedric Perez
This code introduces a very popular and known game, Parchessi or as some might know it, Trouble
in a simpler way, yet recognizable and fun way"""
#imports of all the classes used in this interactive game
from board import Board
from graphics import *

class inheritanceBoard(Board):

    def chooseColorBoard(self,win,color1,color2,color3,color4):
        #draws table image imported for the internet
        table = Image(Point(410, 310), "table(1).png")
        table.draw(win)

        #draws outer board
        outerBoard = Rectangle(Point(55, 25), Point(515, 485))
        outerBoard.setFill("navy blue")
        outerBoard.draw(win)
        outerBoard1 = Rectangle(Point(60, 30), Point(510, 480))
        outerBoard1.setFill("white smoke")
        outerBoard1.draw(win)

        #draws the horizontal rectangle used for the middle section of the board
        leftBase = Rectangle(Point(60.0, 210.0), Point(510.0, 300.0))
        leftBase.draw(win)

        #draws a horizontal line to later divide into steps horizontally
        lineLeft = Line(Point(60.0, 240.0), Point(510.0, 240.0))
        lineLeft.draw(win)
        #same as above
        lineLeft2 = Line(Point(60.0, 270.0), Point(510.0, 270.0))
        lineLeft2.draw(win)

        #draws the vertical rectangle used for the top and bottom section of the board
        topBase = Rectangle(Point(240.0, 30.0), Point(330.0, 480.0))
        topBase.draw(win)

        #draws a vertical line to later divide into steps vertically
        lineTop = Line(Point(270.0, 30.0), Point(270.0, 480.0))
        lineTop.draw(win)
        #same as above
        lineTop2 = Line(Point(300.0, 30.0), Point(300.0, 480.0))
        lineTop2.draw(win)

        #paints the steps white on the board
        board1 = Rectangle(Point(60.0, 210), Point(240, 240))
        board1.setFill("white")
        board1.draw(win)
        board2 = Rectangle(Point(315.0, 210), Point(510, 240))
        board2.setFill("white")
        board2.draw(win)
        board3 = Rectangle(Point(60.0, 270), Point(240, 300))
        board3.setFill("white")
        board3.draw(win)
        board4 = Rectangle(Point(315.0, 270), Point(510, 300))
        board4.setFill("white")
        board4.draw(win)
        board5 = Rectangle(Point(240.0, 30), Point(270, 210))
        board5.setFill("white")
        board5.draw(win)
        board6 = Rectangle(Point(300.0, 30), Point(330, 210))
        board6.setFill("white")
        board6.draw(win)
        board7 = Rectangle(Point(300.0, 300), Point(330, 480))
        board7.setFill("white")
        board7.draw(win)
        board8 = Rectangle(Point(240.0, 300), Point(270, 480))
        board8.setFill("white")
        board8.draw(win)

        #draws and paints the players home row leading to the base filled with their respective colors
        #player 1
        homeLine1 = Rectangle(Point(60.0, 240.0), Point(240.0, 270.0))
        homeLine1.setFill(color1)
        homeLine1.draw(win)
        #player 2
        homeLine2 = Rectangle(Point(270.0, 300.0), Point(300.0, 480.0))
        homeLine2.setFill(color2)
        homeLine2.draw(win)
        #player 3
        homeLine3 = Rectangle(Point(330.0, 240.0), Point(510.0, 270.0))
        homeLine3.setFill(color3)
        homeLine3.draw(win)
        #player 4
        homeLine4 = Rectangle(Point(270.0, 30.0), Point(300.0, 210.0))
        homeLine4.setFill(color4)
        homeLine4.draw(win)

        #draws and paints each players starting position when exiting their home
        #player 1
        homeColor1 = Rectangle(Point(90.0, 210.0), Point(120.0, 240.0))
        homeColor1.setFill("cyan")
        homeColor1.draw(win)
        homeRed1 = Rectangle(Point(90.0, 270.0), Point(120.0, 300.0))
        homeRed1.setFill("cyan")
        homeRed1.draw(win)
        #player 2
        homeColor2 = Rectangle(Point(240.0, 420.0), Point(270.0, 450.0))
        homeColor2.setFill("cyan")
        homeColor2.draw(win)
        homeBlue1 = Rectangle(Point(300.0, 420.0), Point(330.0, 450.0))
        homeBlue1.setFill("cyan")
        homeBlue1.draw(win)
        #player 3
        homeColor3 = Rectangle(Point(450.0, 270.0), Point(480.0, 300.0))
        homeColor3.setFill("cyan")
        homeColor3.draw(win)
        homeGreen1 = Rectangle(Point(450.0, 210.0), Point(480.0, 240.0))
        homeGreen1.setFill("cyan")
        homeGreen1.draw(win)
        #player 4
        homeColor4 = Rectangle(Point(300.0, 60.0), Point(330.0, 90.0))
        homeColor4.setFill("cyan")
        homeColor4.draw(win)
        homeYellow1 = Rectangle(Point(240.0, 60.0), Point(270.0, 90.0))
        homeYellow1.setFill("cyan")
        homeYellow1.draw(win)

        #draws each dividing line horizontally 
        for x in range(60, 510, 30):
            p1 = Point(x, 300)
            p2 = Point(x, 210)
            line = Line(p1, p2)
            line.draw(win)

        #draws each dividing line vertically 
        for x in range(30, 480, 30):
            pt1 = Point(240, x)
            pt2 = Point(330, x)
            line2 = Line(pt1, pt2)
            line2.draw(win)

        #draws and paints each players presentation of house
        #player 1
        home1 = Rectangle(Point(60.0, 30.0), Point(240.0, 210.0))
        home1.setFill("indian red")
        home1.draw(win)
        homeCircle = Circle(Point(150.0, 120.0), 50)
        homeCircle.setFill(color1)
        homeCircle.setOutline("black")
        homeCircle.draw(win)
        #player 2
        home2 = Rectangle(Point(60.0, 300.0), Point(240.0, 480.0))
        home2.setFill("royal blue")
        home2.draw(win)
        homeCircle1 = Circle(Point(150.0, 390.0), 50)
        homeCircle1.setFill(color2)
        homeCircle1.setOutline("black")
        homeCircle1.draw(win)
        #player 3
        home3 = Rectangle(Point(330.0, 300.0), Point(510.0, 480.0))
        home3.setFill("sea green")
        home3.draw(win)
        homeCircle2 = Circle(Point(420.0, 390.0), 50)
        homeCircle2.setFill(color3)
        homeCircle2.setOutline("black")
        homeCircle2.draw(win)
        #player 4
        home4 = Rectangle(Point(330.0, 30.0), Point(510.0, 210.0))
        home4.setFill("light goldenrod")
        home4.draw(win)
        homeCircle3 = Circle(Point(420.0, 120.0), 50)
        homeCircle3.setFill(color4)
        homeCircle3.setOutline("black")
        homeCircle3.draw(win)

        #draws and paints each players home base (middle square of the board)
        base1 = Polygon(Point(240.0, 210.0), Point(240.0, 300.0), Point(285.0, 255.0))
        base1.setFill(color1)
        base1.draw(win)
        base2 = Polygon(Point(240.0, 300.0), Point(330.0, 300.0), Point(285.0, 255.0))
        base2.setFill(color2)
        base2.draw(win)
        base3 = Polygon(Point(330.0, 210.0), Point(330.0, 300.0), Point(285.0, 255.0))
        base3.setFill(color3)
        base3.draw(win)
        base4 = Polygon(Point(240.0, 210.0), Point(330.0, 210.0), Point(285.0, 255.0))
        base4.setFill(color4)
        base4.draw(win)
        
        #draws a line to divide the board and the menu located to the right of the window
        rightMenu = Line(Point(620.0, 0.0), Point(620.0, 620.0))
        rightMenu.draw(win)