import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('files\picture2.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) #hide x and y ticks --> these are axes markings
plt.show()
