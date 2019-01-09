import numpy as np

class NormalDistribution():
    def __init__(self, data):
        mean = np.mean(data)
        mean = np.round(mean,2)
        var = np.var(data)
        var = np.round(var,2)
        std = np.std(data, ddof=1)
        std = np.round(std,2)
        self.mean = mean
        self.var = var
        self.std = std
        self.N = len(data)
        print('Mean: '+str(mean))
        print('Variance: '+str(var))
        print('Standard Deviation: '+str(std))
