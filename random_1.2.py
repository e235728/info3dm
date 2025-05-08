import numpy as np
import matplotlib.pyplot as plt
from true_function import true_function

def random_points(n=20, seed=1000):
    np.random.seed(seed)
    return np.random.uniform(-1, 1, n)

x = random_points()

print(x)

y = true_function(x)

print(y)
