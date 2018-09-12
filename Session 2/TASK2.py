import cv2
import numpy as np
I = cv2.imread('damavand.jpg')
J = cv2.imread('eram.jpg')
alpha = 1;
beta= 0;
while beta<1.01:
    K = (alpha * I + beta * J).astype(np.uint8)
    alpha = alpha - 0.02
    beta = beta + 0.02
    cv2.imshow("Blending", K)
    cv2.waitKey(200)


cv2.waitKey(0)
cv2.destroyAllWindows()