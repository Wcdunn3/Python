# Creating a regression line - aka line of best fit 
# Y = mx + b 
from statistics import mean 
import numpy as np 
import matplotlib.pyplot as plt

# defined as numpy arrays 
xs = np.array([1,2,3,4,5,6], dtype=np.float64)
ys = np.array([5,4,6,5,6,7], dtype=np.float64)

def best_fit_slope(xs,ys):
    m = (((mean(xs) * mean(ys)) - mean(xs*ys)) / ( (mean(xs) * mean(xs)) - mean(xs**2)    ) )
    return m;

m = best_fit_slope(xs,ys)

print(m)
