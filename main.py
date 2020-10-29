"""Code created by Elimelec Rodriguez and Cedric Perez
This code introduces a very popular and known game, Parchessi or as some might know it, Trouble
in a simpler way, yet recognizable and fun way"""
#imports of all the classes used in this interactive game
from graphics import *
from game import Game
from Buttons import Button
from inheritanceBoard import inheritanceBoard


def main():

    #Creates a greeting window using a image taken from the internet to allow the player to choose to: Play or Quit
    gameImage = Image(Point(180,180), "parchessi.png")
    window = GraphWin("Parcheesi", 360,360)
    gameImage.draw(window)

    #Creates the Buttons for Play or Quit using the Class Button
    playButton = Button(window, Point(180.0, 200), 80, 30, "Play")
    quitButton = Button(window, Point(180.0, 240), 80, 30, "QUIT")
    playButton.activate()
    quitButton.activate()
    
    pt = window.getMouse()#Gets the users click on which button

    if not quitButton.clicked(pt):#if the Play button is clicked, the game begins
        window.close() #closes the previous window so that the game window in the only one remaining
        win = GraphWin("Parcheesi", 820, 620) #We declare and define our window
        field = inheritanceBoard()#we make an object from the inheritanceBoard class so that the user may customize the board game (colors) if desired
        game = Game() #creates the object from Game class

        field.board(win) #draws the board
        game.playGame(win) #starts the game

main()