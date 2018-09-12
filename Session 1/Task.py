import numpy as np
import cv2

I = cv2.imread('Em gray.jpg')
J = I.copy()
In = J[::-1]
cv2.imshow('TASK',np.vstack((I,In)))
cv2.waitKey(0)