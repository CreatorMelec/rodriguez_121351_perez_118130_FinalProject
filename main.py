from graphics import *
from game import Game
from dieview import DieView
from board import Board


def main():


    win = GraphWin("Parchessi", 820, 620)
    field = Board()
    game = Game()

    field.board(win)
    game.playGame(win)


    win.getMouse()
    win.close()

main()