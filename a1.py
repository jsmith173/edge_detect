import numpy as np
import matplotlib.pyplot as plt

# let img1 be an image with no features
img1 = np.array([np.array([20, 20]), np.array([20, 20])])

kernel_horizontal = np.array([np.array([2, 2]), np.array([-2, -2])])

print(img1)