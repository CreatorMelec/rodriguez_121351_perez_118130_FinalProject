from graphics import *
from game import Game
from dieview import DieView


def main():


    win = GraphWin("Parchessi", 820, 620)
    player = Game()

    viewDice = DieView(win,Point(690.0, 120.0), 50)
    viewDice.setValue(6)
    viewDice2 = DieView(win,Point(760.0, 120.0), 50)
    viewDice2.setValue(3)

    player.board(win)

    win.getMouse()
    win.close()

main()