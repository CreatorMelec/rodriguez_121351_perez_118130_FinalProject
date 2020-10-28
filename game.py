"""Code created by Elimelec Rodriguez and Cedric Perez
This code introduces a very popular and known game, Parchessi or as some might know it, Trouble
in a simpler way, yet recognizable and fun way"""
#imports of all the classes used in this interactive game
from graphics import *
from Dice import Dice
from ColorDieView import ColorDieView
from player import Player
from Buttons import Button
from inheritanceBoard import inheritanceBoard


class Game: #class to start game and its features

    def __init__(self):
        self.player = Player() #creates object from class Player to be able to call the functions needed
        self.players = [] #creates a list of objects from Player
        for x in range(4):
            self.players.append(Player())
        self.board = inheritanceBoard() #creates object from Board to call functions needed

    def playGame(self, win): #main function that runs the game

        #creates buttons for roll dice and quit
        rollButton = Button(win, Point(720.0, 45), 80, 30, "Roll Dice") 
        quitButton = Button(win, Point(720.0, 510), 80, 30, "QUIT")
        rollButton.activate()
        quitButton.activate()

        pt = win.getMouse()#Gets the users click on which button
        turn = 0 #variable used to create turns for each player
        counter = 0 #variable used to keep count of the times the user gets a double die 

        while not quitButton.clicked(pt): #while the player doesn't click Quit the game continues

            if turn == 0: #starts player red's turn
                if rollButton.clicked(pt): #checks if the player clicks roll dice, if true then their turn proceeds
                    self.board.playerTurn("Red", win) #calls the function that draws in the menu who's player's turn it is
                    dice1, dice2 = self.rollDice(win) #calls the function to roll the dice and returns the values for each one
                    if self.players[0].returnChips() > 0:#calls the function returnChips() to determine available chips in the player's home, if true then proceeds
                        checkMove, dice = self.startHome(dice1, dice2, "red", win) #calls function startHome to check if the player rolled a 5 on either dice and returns the value of the other
                        if checkMove:#true if the player rolled a 5 on either die
                            self.players[0].MovePiece(self.players[0].player, dice, dice1, dice2, "red", #calls function that moves the player's piece according to the dice value returned after rolling 5
                                                      self.players[0].returnSteps(), win)
                            self.eatPlayer("red", win) #calls function that checks if the player ate another player

                    elif self.players[0].returnChips() == 0: #calls function that checks the players available chips, if true then proceeds
                        dice = dice1 + dice2 #sums both die values 
                        self.players[0].MovePiece(self.players[0].player, dice, dice1, dice2, "red", # calls function that moves the player's piece according to the sum of both die
                                                  self.players[0].returnSteps(), win)
                        self.eatPlayer("red", win) #calls function that checks if the player ate another player

                    if self.doubleTurn(dice1, dice2): #calls funciton to check both die values, if true then proceeds to create another turn
                        counter += 1 #adds one to counter to keep track of doubles
                        turn = 0 #sets turn = 0 so that its player Red's turn again
                        #prints a text in the menu letting the player know its their turn again
                        turnAgain = Text(Point(720.0, 300), "Your turn again") 
                        turnAgain.setStyle("bold")
                        turnAgain.setSize(16)
                        turnAgain.draw(win)
                        win.getMouse()
                        turnAgain.undraw()

                        if counter == 2: #once counter hits 2, the player's turn is skipped
                            turn += 1 #adds one to turn to continue to next player
                            counter = 0 #resets counter = 0
                            skip = Text(Point(720.0, 300), "Next player's turn") #prints in the menu that it's the next player's turn
                            skip.setStyle("bold")
                            skip.setSize(16)
                            skip.draw(win)
                            win.getMouse()
                            skip.undraw()
                    else: #if no double was rolled then proceeds
                        turn += 1 #adds one to turn to continue to next player
                        counter = 0 #resets counter = 0
                        skip = Text(Point(720.0, 300), "Next player's turn")#prints in the menu that it's the next player's turn
                        skip.setStyle("bold")
                        skip.setSize(16)
                        skip.draw(win)
                        win.getMouse()
                        skip.undraw()

                    if self.players[0].playerWon(self.players[0].piecesInHome(), win): #calls function that checks if the player won
                        win.getMouse()
                        win.close() #closes the window if player won

                    pt = win.getMouse() #resets the click for the next player

            elif turn == 1: #blue player's turn, everything works as mentioned above

                if rollButton.clicked(pt):
                    self.board.playerTurn("Blue", win)
                    dice1, dice2 = self.rollDice(win)
                    if self.players[1].returnChips() > 0:
                        checkMove, dice = self.startHome(dice1, dice2, "blue", win)
                        if checkMove:
                            self.players[1].MovePiece(self.players[1].player, dice, dice1, dice2, "blue",
                                                      self.players[1].returnSteps(), win)
                            self.eatPlayer("blue", win)

                    elif self.players[1].returnChips() == 0:
                        self.players[1].MovePiece(self.players[1].player, dice, dice1, dice2, "blue",
                                                  self.players[1].returnSteps(), win)
                        self.eatPlayer("blue", win)

                    if self.doubleTurn(dice1, dice2):
                        counter += 1
                        turn = 1
                        turnAgain = Text(Point(720.0, 300), "Your turn again")
                        turnAgain.setStyle("bold")
                        turnAgain.setSize(16)
                        turnAgain.draw(win)
                        win.getMouse()
                        turnAgain.undraw()
                        if counter == 2:
                            turn += 1
                            counter = 0
                            skip = Text(Point(720.0, 300), "Next player's turn")
                            skip.setStyle("bold")
                            skip.setSize(16)
                            skip.draw(win)
                            win.getMouse()
                            skip.undraw()

                    else:
                        turn += 1
                        counter = 0
                        skip = Text(Point(720.0, 300), "Next player's turn")
                        skip.setStyle("bold")
                        skip.setSize(16)
                        skip.draw(win)
                        win.getMouse()
                        skip.undraw()

                    if self.players[1].playerWon(self.players[1].piecesInHome(), win):
                        win.getMouse()
                        win.close()

                    pt = win.getMouse()



            elif turn == 2: #green player's turn, everything works as mentioned above

                if rollButton.clicked(pt):
                    self.board.playerTurn("Green", win)
                    dice1, dice2 = self.rollDice(win)
                    if self.players[2].returnChips() > 0:
                        checkMove, dice = self.startHome(dice1, dice2, "green", win)
                        if checkMove:
                            self.players[2].MovePiece(self.players[2].player, dice, dice1, dice2, "green",
                                                      self.players[2].returnSteps(), win)
                            self.eatPlayer("green", win)

                    elif self.players[2].returnChips() == 0:
                        dice = dice1 + dice2
                        self.players[2].MovePiece(self.players[2].player, dice, dice1, dice2, "green",
                                                  self.players[2].returnSteps(), win)
                        self.eatPlayer("green", win)

                    if self.doubleTurn(dice1, dice2):
                        counter += 1
                        turn = 2
                        turnAgain = Text(Point(720.0, 300), "Your turn again")
                        turnAgain.setStyle("bold")
                        turnAgain.setSize(16)
                        turnAgain.draw(win)
                        win.getMouse()
                        turnAgain.undraw()
                        if counter == 2:
                            turn += 1
                            counter = 0
                            skip = Text(Point(720.0, 300), "Next player's turn")
                            skip.setStyle("bold")
                            skip.setSize(16)
                            skip.draw(win)
                            win.getMouse()
                            skip.undraw()

                    else:
                        turn += 1
                        counter = 0
                        skip = Text(Point(720.0, 300), "Next player's turn")
                        skip.setStyle("bold")
                        skip.setSize(16)
                        skip.draw(win)
                        win.getMouse()
                        skip.undraw()

                    if self.players[2].playerWon(self.players[2].piecesInHome(), win):
                        win.getMouse()
                        win.close()

                    pt = win.getMouse()



            elif turn == 3: #yellow player's turn, everything works as mentioned above

                if rollButton.clicked(pt):
                    self.board.playerTurn("Yellow", win)
                    dice1, dice2 = self.rollDice(win)
                    if self.players[3].returnChips() > 0:
                        checkMove, dice = self.startHome(dice1, dice2, "yellow", win)
                        if checkMove:
                            self.players[3].MovePiece(self.players[3].player, dice, dice1, dice2, "yellow",
                                                      self.players[3].returnSteps(), win)
                            self.eatPlayer("yellow", win)

                    elif self.players[3].returnChips() == 0:
                        self.players[3].MovePiece(self.players[3].player, dice, dice1, dice2, "yellow",
                                                  self.players[3].returnSteps(), win)
                        self.eatPlayer("yellow", win)

                    if self.doubleTurn(dice1, dice2):
                        counter += 1
                        turn = 3
                        turnAgain = Text(Point(720.0, 300), "Your turn again")
                        turnAgain.setStyle("bold")
                        turnAgain.setSize(16)
                        turnAgain.draw(win)
                        win.getMouse()
                        turnAgain.undraw()
                        if counter == 2:
                            turn += 1
                            counter = 0
                            skip = Text(Point(720.0, 300), "Next player's turn")
                            skip.setStyle("bold")
                            skip.setSize(16)
                            skip.draw(win)
                            win.getMouse()
                            skip.undraw()

                    else:
                        turn += 1
                        counter = 0
                        skip = Text(Point(720.0, 300), "Next player's turn")
                        skip.setStyle("bold")
                        skip.setSize(16)
                        skip.draw(win)
                        win.getMouse()
                        skip.undraw()

                    if self.players[3].playerWon(self.players[3].piecesInHome(), win):
                        win.getMouse()
                        win.close()

                    pt = win.getMouse()


            elif turn == 4: #keeps the loop going starting back at the first player's turn
                turn = 0

                pt = win.getMouse() #resets click 

    #function that calls upon Dice class and ColorDieView to roll and draw the dice in the menu
    def rollDice(self, win):

        dado = Dice() #object created from Dice class
        dado.rollDie() #calls function that rolls the dice
        diceVal = dado.diceValue() #variable used to hold the value of the dice 
        viewDice = ColorDieView(win, Point(690.0, 120.0), 50) #calls the function that creates the dice in the menu 
        viewDice.setValue(diceVal) #gives the value of the dice to the created dice so that the value is also drawn
        #works as mentioned above
        dado.rollDie()
        diceVal2 = dado.diceValue()
        viewDice2 = ColorDieView(win, Point(760.0, 120.0), 50)
        viewDice2.setValue(diceVal2)
        return diceVal, diceVal2

    #function that checks if one of the dice values is 5 to start the player at their home position
    def startHome(self, diceVal, diceVal2, color, win):

        if diceVal == 5 or diceVal2 == 5: #checks both dice values, if there is a 5, then it proceeds
            if color == "red": #checks the color of the player, then proceeds
                self.players[0].drawPlayer("red", win) #calls the function that draws the player at their home position
                #check conditions to see which die had the 5 and return the other die instead
                if diceVal == 5: 
                    self.players[0].updateChips()
                    return True, diceVal2
                else:
                    self.players[0].updateChips()
                    return True, diceVal
            elif color == "blue": #blue player, works as mentioned above
                self.players[1].drawPlayer("blue", win)
                if diceVal == 5:
                    self.players[1].updateChips()
                    return True, diceVal2
                else:
                    self.players[1].updateChips()
                    return True, diceVal
            elif color == "green": #green player, works as mentioned above
                self.players[2].drawPlayer("green", win)
                if diceVal == 5:
                    self.players[2].updateChips()
                    return True, diceVal2
                else:
                    self.players[2].updateChips()
                    return True, diceVal
            elif color == "yellow": #yellow player, works as mentioned above
                self.players[3].drawPlayer("yellow", win)
                if diceVal == 5:
                    self.players[3].updateChips()
                    return True, diceVal2
                else:
                    self.players[3].updateChips()
                    return True, diceVal
        else: #if no die has a 5, then returns false and the sum of both die
            moveDice = diceVal + diceVal2
            return False, moveDice

    #function that checks if both die are the same
    def doubleTurn(self, dice1, dice2):

        if dice1 == dice2:
            return True
        else:
            return False

    #function that checks the position of the player calling and checks if there is an existing player there and undraws that player
    def eatPlayer(self, color, win):
        if color == "red":
            if self.players[0].player.getCenter().getX() == self.players[1].player.getCenter().getX() and self.players[
                0].player.getCenter().getY() == self.players[1].player.getCenter().getY():
                self.players[1].player.undraw()
                self.players[1].reset()
                self.players[1] = Player()
                self.eatenMessage("Blue", win)
            elif self.players[0].player.getCenter().getX() == self.players[2].player.getCenter().getX() and \
                    self.players[0].player.getCenter().getY() == self.players[2].player.getCenter().getY():
                self.players[2].player.undraw()
                self.players[2].reset()
                self.players[2] = Player()
                self.eatenMessage("Green", win)
            elif self.players[0].player.getCenter().getX() == self.players[3].player.getCenter().getX() and \
                    self.players[0].player.getCenter().getY() == self.players[3].player.getCenter().getY():
                self.players[3].player.undraw()
                self.players[3].reset()
                self.players[3] = Player()
                self.eatenMessage("Yellow", win)
        elif color == "blue":
            if self.players[1].player.getCenter().getX() == self.players[0].player.getCenter().getX() and self.players[
                1].player.getCenter().getY() == self.players[0].player.getCenter().getY():
                self.players[0].player.undraw()
                self.players[0].reset()
                self.players[0] = Player()
                self.eatenMessage("Red", win)
            elif self.players[1].player.getCenter().getX() == self.players[2].player.getCenter().getX() and \
                    self.players[1].player.getCenter().getY() == self.players[2].player.getCenter().getY():
                self.players[2].player.undraw()
                self.players[2].reset()
                self.players[2] = Player()
                self.eatenMessage("Green", win)
            elif self.players[1].player.getCenter().getX() == self.players[3].player.getCenter().getX() and \
                    self.players[1].player.getCenter().getY() == self.players[3].player.getCenter().getY():
                self.players[3].player.undraw()
                self.players[3].reset()
                self.players[3] = Player()
                self.eatenMessage("Yellow", win)
        elif color == "green":
            if self.players[2].player.getCenter().getX() == self.players[0].player.getCenter().getX() and self.players[
                2].player.getCenter().getY() == self.players[0].player.getCenter().getY():
                self.players[0].player.undraw()
                self.players[0].reset()
                self.players[0] = Player()
                self.eatenMessage("Red", win)
            elif self.players[2].player.getCenter().getX() == self.players[1].player.getCenter().getX() and \
                    self.players[2].player.getCenter().getY() == self.players[1].player.getCenter().getY():
                self.players[1].player.undraw()
                self.players[1].reset()
                self.players[1] = Player()
                self.eatenMessage("Blue", win)
            elif self.players[2].player.getCenter().getX() == self.players[3].player.getCenter().getX() and \
                    self.players[2].player.getCenter().getY() == self.players[3].player.getCenter().getY():
                self.players[3].player.undraw()
                self.players[3].reset()
                self.players[3] = Player()
                self.eatenMessage("Yellow", win)

        elif color == "yellow":
            if self.players[3].player.getCenter().getX() == self.players[0].player.getCenter().getX() and self.players[
                3].player.getCenter().getY() == self.players[0].player.getCenter().getY():
                self.players[0].player.undraw()
                self.players[0].reset()
                self.players[0] = Player()
                self.eatenMessage("Red", win)
            elif self.players[3].player.getCenter().getX() == self.players[2].player.getCenter().getX() and \
                    self.players[3].player.getCenter().getY() == self.players[2].player.getCenter().getY():
                self.players[2].player.undraw()
                self.players[2].reset()
                self.players[2] = Player()
                self.eatenMessage("Green", win)
            elif self.players[3].player.getCenter().getX() == self.players[1].player.getCenter().getX() and \
                    self.players[3].player.getCenter().getY() == self.players[1].player.getCenter().getY():
                self.players[1].player.undraw()
                self.players[1].reset()
                self.players[1] = Player()
                self.eatenMessage("Blue", win)

    #function that displays the player that was eaten in the menu 
    def eatenMessage(self, color, win):
        eat = Text(Point(720.0, 300), str(color) + " Player Eaten")
        eat.setStyle("bold")
        eat.setSize(16)
        eat.draw(win)
        win.getMouse()
        eat.undraw()
    
    #function used to check for a 1 on either die, used to be able to move from the last place on the board to the home
    def oneDice(self, dice1, dice2):
        if dice1 or dice2 == 1:
            if dice1 == 1:
                return True, dice1
            elif dice2 == 1:
                return True, dice2
        else:
            return False, dice1






