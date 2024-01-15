#!/usr/bin/env python
# coding: utf-8

# In[41]:


import matplotlib.pyplot as plt
import numpy as np
import PIL, json, glob, cv2
import pathlib
from scipy import signal


# In[42]:


img_width = 400
input_files = glob.glob("*.jpg")
img_files = []
for img_file in input_files:
 img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
 h, w = img.shape
 if w > img_width:
  r = img_width/w;
  img = cv2.resize(img, (img_width,int(r*h))) 
  img_files.append(img)


# In[43]:


for img in img_files:
    scharr = np.array([[ -3-3j, 0-10j,  +3 -3j],
                       [-10+0j, 0+ 0j, +10 +0j],
                       [ -3+3j, 0+10j,  +3 +3j]]) # Gx + j*Gy
    grad = signal.convolve2d(img, scharr, boundary='symm', mode='same')
    
    fig, (ax_orig, ax_mag) = plt.subplots(2, 1, figsize=(6, 15))
    ax_orig.imshow(img, cmap='gray')
    ax_orig.set_title('Original')
    ax_orig.set_axis_off()
    ax_mag.imshow(np.absolute(grad), cmap='gray')
    ax_mag.set_title('Gradient magnitude')
    ax_mag.set_axis_off()


# In[ ]:




