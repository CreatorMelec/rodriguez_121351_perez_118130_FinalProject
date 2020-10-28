from graphics import *
from game import Game
from Buttons import Button
from inheritanceBoard import inheritanceBoard


def main():

    gameImage = Image(Point(180,180), "parchessi.png")
    window = GraphWin("Parchessi", 360,360)
    gameImage.draw(window)

    playButton = Button(window, Point(180.0, 200), 80, 30, "Play")
    quitButton = Button(window, Point(180.0, 240), 80, 30, "QUIT")
    playButton.activate()
    quitButton.activate()

    pt = window.getMouse()
    while not quitButton.clicked(pt):
        window.close()
        win = GraphWin("Parchessi", 820, 620)
        field = inheritanceBoard()
        game = Game()

        field.board(win)
        game.playGame(win)


main()