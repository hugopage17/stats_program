import math
import numpy as np

class Confidence_Intervals():
    def sample_mean(mean, std, n):
        standard_error = 1.96*(std/math.sqrt(n))
        first_eq = mean - standard_error
        second_eq = mean + standard_error
        first_eq = np.round(first_eq,2)
        second_eq = np.round(second_eq,2)
        print('With 95% confidence the true mean is between '+str(first_eq)+' and '+str(second_eq))
