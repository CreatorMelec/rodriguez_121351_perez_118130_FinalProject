#60 para llegar al home
#This will later no be a circle

class chip:
    def __init__(self):
        self.remainingSteps = 60
        self.reset = False

    def updateSteps(self,takenSteps):
        if self.reset:
            self.remainingSteps = 60
            self.updateReset()
        else:
            self.remainingSteps = self.remainingSteps - takenSteps


    def updateReset(self):
        self.reset = not self.reset

    def returnSteps(self):
        return self.remainingSteps
