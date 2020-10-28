"""Code extracted from Python Programming: An introduction to Computer Science by John M. Zelle, Ph.D.
used to create the dices with their generated values"""
#imports of all the classes used in this interactive game
from graphics import *

class DieView:

    def __init__(self,win,center,size):

        self.win = win
        self.backGround = "white"
        self.foreGround = "black"
        self.pSize = 0.1 * size
        hsize = size / 2.0
        offset  = 0.6*hsize

        #create the square for the face
        cx,cy = center.getX(), center.getY()
        p1 = Point(cx - hsize, cy - hsize)
        p2 = Point(cx + hsize, cy + hsize)
        rect = Rectangle(p1,p2)
        rect.draw(win)
        rect.setFill(self.backGround)

        #create standard pip locations
        self.pip1 = self.__makePip(cx - offset, cy - offset)
        self.pip2 = self.__makePip(cx - offset, cy)
        self.pip3 = self.__makePip(cx - offset, cy + offset)
        self.pip4 = self.__makePip(cx, cy)
        self.pip5 = self.__makePip(cx + offset, cy - offset)
        self.pip6 = self.__makePip(cx + offset, cy)
        self.pip7 = self.__makePip(cx + offset, cy + offset)

        self.setValue(1)

    def __makePip(self,x,y):
        pip = Circle(Point(x,y),self.pSize)
        pip.setFill(self.backGround)
        pip.setOutline(self.backGround)
        pip.draw(self.win)
        return pip

    def setValue(self,value):
        self.pip1.setFill(self.backGround)
        self.pip2.setFill(self.backGround)
        self.pip3.setFill(self.backGround)
        self.pip4.setFill(self.backGround)
        self.pip5.setFill(self.backGround)
        self.pip6.setFill(self.backGround)
        self.pip7.setFill(self.backGround)

        if value == 1:
            self.pip4.setFill(self.foreGround)
        elif value == 2:
            self.pip1.setFill(self.foreGround)
            self.pip7.setFill(self.foreGround)
        elif value == 3:
            self.pip1.setFill(self.foreGround)
            self.pip7.setFill(self.foreGround)
            self.pip4.setFill(self.foreGround)
        elif value == 4:
            self.pip1.setFill(self.foreGround)
            self.pip3.setFill(self.foreGround)
            self.pip5.setFill(self.foreGround)
            self.pip7.setFill(self.foreGround)
        elif value == 5:
            self.pip1.setFill(self.foreGround)
            self.pip3.setFill(self.foreGround)
            self.pip4.setFill(self.foreGround)
            self.pip5.setFill(self.foreGround)
            self.pip7.setFill(self.foreGround)
        else:
            self.pip1.setFill(self.foreGround)
            self.pip2.setFill(self.foreGround)
            self.pip3.setFill(self.foreGround)
            self.pip5.setFill(self.foreGround)
            self.pip6.setFill(self.foreGround)
            self.pip7.setFill(self.foreGround)






