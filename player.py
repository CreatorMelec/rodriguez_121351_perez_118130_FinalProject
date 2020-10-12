from graphics import *

class Players():

    def __init__(self):
        self.player = [1,2,3,4]

    def drawPlayers(self, win):

        for i in range(self.player):

    
    
    
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