import pandas as pd
import numpy as np

class Data:
    def __init__(self):
        self.is_loaded = False

    def load_data(self, data):
        self.content = pd.read_csv(data)
        self.x_axis = []
        self.num_list = []
        for nums in self.content:
            nums = int(nums)
            self.num_list.append(nums)
        self.get_x_axis()
        self.is_loaded = True
        print(str(data)+' loaded')

    def show_data(self):
        print(self.content)

    def get_x_axis(self):
        i = 1
        while i <= len(self.num_list):
            self.x_axis.append(i)
            i += 1
