"""Code created by Elimelec Rodriguez and Cedric Perez
This code introduces a very popular and known game, Parchessi or as some might know it, Trouble
in a simpler way, yet recognizable and fun way"""
#imports of all the classes used in this interactive game
from board import Board
from graphics import *

class inheritanceBoard(Board):

    def chooseColorBoard(self,win,color1,color2,color3,color4):
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

        #draws and paints the players home row leading to the base filled with their respective colors
        homeLine1 = Rectangle(Point(60.0, 240.0), Point(240.0, 270.0))
        homeLine1.setFill(color1)
        homeLine1.draw(win)
        homeLine2 = Rectangle(Point(270.0, 300.0), Point(300.0, 480.0))
        homeLine2.setFill(color4)
        homeLine2.draw(win)
        homeLine3 = Rectangle(Point(330.0, 240.0), Point(510.0, 270.0))
        homeLine3.setFill(color2)
        homeLine3.draw(win)
        homeLine4 = Rectangle(Point(270.0, 30.0), Point(300.0, 210.0))
        homeLine4.setFill(color3)
        homeLine4.draw(win)

        #draws and paints each players starting position when exiting their home
        homeColor1 = Rectangle(Point(90.0, 210.0), Point(120.0, 240.0))
        homeColor1.setFill("cyan")
        homeColor1.draw(win)
        homeColor2 = Rectangle(Point(240.0, 420.0), Point(270.0, 450.0))
        homeColor2.setFill("cyan")
        homeColor2.draw(win)
        homeColor3 = Rectangle(Point(450.0, 270.0), Point(480.0, 300.0))
        homeColor3.setFill("cyan")
        homeColor3.draw(win)
        homeColor4 = Rectangle(Point(300.0, 60.0), Point(330.0, 90.0))
        homeColor4.setFill("cyan")
        homeColor4.draw(win)

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
        home1 = Rectangle(Point(90.0, 60.0), Point(190.0, 150.0))
        home1.setFill(color1)
        home1.draw(win)
        home2 = Rectangle(Point(390.0, 360.0), Point(490.0, 450.0))
        home2.setFill(color2)
        home2.draw(win)
        home3 = Rectangle(Point(390.0, 60.0), Point(490.0, 150.0))
        home3.setFill(color3)
        home3.draw(win)
        home3 = Rectangle(Point(90.0, 360.0), Point(190.0, 450.0))
        home3.setFill(color4)
        home3.draw(win)

        #draws and paints each players home base (middle square of the board)
        base1 = Polygon(Point(240.0, 210.0), Point(240.0, 300.0), Point(285.0, 255.0))
        base1.setFill(color1)
        base1.draw(win)
        base2 = Polygon(Point(330.0, 210.0), Point(330.0, 300.0), Point(285.0, 255.0))
        base2.setFill(color2)
        base2.draw(win)
        base3 = Polygon(Point(240.0, 210.0), Point(330.0, 210.0), Point(285.0, 255.0))
        base3.setFill(color3)
        base3.draw(win)
        base4 = Polygon(Point(240.0, 300.0), Point(330.0, 300.0), Point(285.0, 255.0))
        base4.setFill(color4)
        base4.draw(win)

        #draws a line to divide the board and the menu located to the right of the window
        rightMenu = Line(Point(620.0, 0.0), Point(620.0, 620.0))
        rightMenu.draw(win)