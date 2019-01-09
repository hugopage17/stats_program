import matplotlib.pyplot as plt

class Graph():
    def __init__(self, x_axis, y_axis):
        self.x = x_axis
        self.y = y_axis
        plt.plot(self.x ,self.y)
        plt.show()
