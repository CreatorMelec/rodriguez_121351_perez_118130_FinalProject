"""Code created by Elimelec Rodriguez and Cedric Perez
This code introduces a very popular and known game, Parchessi or as some might know it, Trouble
in a simpler way, yet recognizable and fun way"""
#imports of all the classes used in this interactive game
from graphics import * 

class Board: #class to draw board

    def __init__(self):
        pass #no member is need for this class, the only purpose is to draw the board using graphic library elements

    def board(self,win): #draws the board on the window declared in main

        #draws the horizontal rectangle used for the middle section of the board
        leftBase = Rectangle(Point(60.0, 210.0), Point(510.0,300.0))
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
        #red player
        homeLineRed = Rectangle(Point(60.0, 240.0), Point(240.0, 270.0))
        homeLineRed.setFill("red")
        homeLineRed.draw(win)
        #blue player
        homeLineBlue = Rectangle(Point(270.0, 300.0), Point(300.0, 480.0))
        homeLineBlue.setFill("blue")
        homeLineBlue.draw(win)
        #green player
        homeLineGreen = Rectangle(Point(330.0, 240.0), Point(510.0, 270.0))
        homeLineGreen.setFill("Green")
        homeLineGreen.draw(win)
        #yellow player
        homeLineYellow = Rectangle(Point(270.0, 30.0), Point(300.0, 210.0))
        homeLineYellow.setFill("yellow")
        homeLineYellow.draw(win)
        
        #draws and paints each players starting position when exiting their home
        #red player
        homeRed = Rectangle(Point(90.0, 210.0), Point(120.0, 240.0))
        homeRed.setFill("cyan")
        homeRed.draw(win)
        #blue player
        homeBlue = Rectangle(Point(240.0, 420.0), Point(270.0, 450.0))
        homeBlue.setFill("cyan")
        homeBlue.draw(win)
        #green player
        homeGreen = Rectangle(Point(450.0, 270.0), Point(480.0, 300.0))
        homeGreen.setFill("cyan")
        homeGreen.draw(win)
        #yellow player
        homeYellow = Rectangle(Point(300.0, 60.0), Point(330.0, 90.0))
        homeYellow.setFill("cyan")
        homeYellow.draw(win)
        
        #draws each dividing line horizontally 
        for x in range(60,510,30):
            p1 = Point(x,300)
            p2 = Point(x,210)
            line = Line(p1,p2)
            line.draw(win)

        #draws each dividing line vertically 
        for x in range(30,480,30):
            pt1 = Point(240,x)
            pt2 = Point(330,x)
            line2 = Line(pt1,pt2)
            line2.draw(win)

        #draws and paints each players presentation of house
        #red player
        home1 = Rectangle(Point(90.0, 60.0), Point(190.0, 150.0))
        home1.setFill("red")
        home1.draw(win)
        #blue player
        home3 = Rectangle(Point(90.0, 360.0), Point(190.0, 450.0))
        home3.setFill("blue")
        home3.draw(win)
        #green player
        home2 = Rectangle(Point(390.0, 360.0), Point(490.0, 450.0))
        home2.setFill("green")
        home2.draw(win)
        #yellow player
        home3 = Rectangle(Point(390.0, 60.0), Point(490.0, 150.0))
        home3.setFill("yellow")
        home3.draw(win)
        
        #draws and paints each players home base (middle square of the board)
        #red player
        redBase = Polygon(Point(240.0, 210.0), Point(240.0, 300.0), Point(285.0,255.0))
        redBase.setFill("red")
        redBase.draw(win)
        #blue player
        blueBase = Polygon(Point(240.0, 300.0), Point(330.0, 300.0 ), Point(285.0, 255.0))
        blueBase.setFill("blue")
        blueBase.draw(win)
        #green player
        greenBase = Polygon(Point(330.0, 210.0), Point(330.0, 300.0), Point(285.0, 255.0))
        greenBase.setFill("green")
        greenBase.draw(win)
        #yellow player
        yellowBase = Polygon(Point(240.0, 210.0), Point(330.0, 210.0), Point(285.0, 255.0))
        yellowBase.setFill("yellow")
        yellowBase.draw(win)
        
        #draws a line to divide the board and the menu located to the right of the window
        rightMenu = Line(Point(620.0, 0.0), Point(620.0, 620.0))
        rightMenu.draw(win)

    #draws in the menu section whose player's turn it is
    def playerTurn(self, color, win):
        player = Text(Point(720.0, 300), str(color) + "'s Turn")
        player.setStyle("bold")
        player.setSize(16)
        player.draw(win)
        win.getMouse()
        player.undraw()
   