import numpy as np


class PIXELDATA:
    def __init__(self, blue, green, red):
        self.redC = red
        self.greenC = green
        self.blueC = blue

    def colors(self):
        return self.blueC, self.greenC, self.redC
