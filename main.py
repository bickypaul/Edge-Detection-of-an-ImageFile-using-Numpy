#importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from vertical_edge import vert_edge #importing module from vertical_edge.py
from horizontal_edge import hor_edge #importing module from horizontal_edge.py

img = mpimg.imread('lena.png')     #reading the image (.jpg) file.
black_n_white = img.mean(axis=2)   #converting the 3D channeled image into 2D channeled.
h,w = black_n_white.shape          #shape of the matrix

vertical = vert_edge(w,h,black_n_white)  #calling the function in vertical_edge.py module
horizontal = hor_edge(w,h,black_n_white) #calling the function in horizontal_edge.py module
image = np.sqrt((vertical**2) + (horizontal**2)) #combining both the vector values.
plt.imshow(image, cmap='gray', interpolation='nearest') #collecting the final image
plt.show() #plotting the image
