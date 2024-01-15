import scipy.signal
import numpy as np

image = [[1, 2, 3, 4, 5, 6, 7],
         [8, 9, 10, 11, 12, 13, 14],
         [15, 16, 17, 18, 19, 20, 21],
         [22, 23, 24, 25, 26, 27, 28],
         [29, 30, 31, 32, 33, 34, 35],
         [36, 37, 38, 39, 40, 41, 42],
         [43, 44, 45, 46, 47, 48, 49]]


filter_kernel = [[0, -6, 2],
                 [1, 3, -2],
                 [-1, 1, -1]]

test = np.array([[ -3-3j, 1-10j,  +3-3j],
	 		     [-10+2j, 4+6j, +10-3j],
				 [ -3+9j, -2+10j, +3-3j]]) # Gx + j*Gy
				 
scharr = np.array([[ -3-3j, 0-10j,  +3 -3j],
				   [-10+0j, 0+ 0j, +10 +0j],
				   [ -3+3j, 0+10j,  +3 +3j]]) # Gx + j*Gy
				 
					   
res = scipy.signal.convolve2d(image, test,
                              mode='same', boundary='fill', fillvalue=0)
print(res)

