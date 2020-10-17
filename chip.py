#60 para llegar al home
#This will later no be a circle


class chip:
    def __init__(self):
        self.reset = False

    def updateReset(self):
        self.reset = not self.reset
