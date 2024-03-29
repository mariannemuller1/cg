# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:00:39 2019

@author: Mary
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('blur.jpeg')

blur = cv2.blur(img,(5,5))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()