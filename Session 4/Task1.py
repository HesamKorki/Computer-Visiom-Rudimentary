import numpy as np
import cv2

I = cv2.imread('Apple_HQ.jpg',cv2.IMREAD_GRAYSCALE)
I = I.astype(np.float)/255
sigma = 0.04


while True :
    N = np.random.randn(*I.shape)* sigma
    J = I +N


    cv2.imshow('snow noise',J)
    key = cv2.waitKey(33)
    if key & 0xFF == ord('u'):
        sigma = sigma + 0.005
        pass
    elif key & 0xFF == ord('d'):
        if sigma <= 0.001 :

            pass
        elif sigma >= 0.001 :
            sigma = sigma - 0.005

        pass
    elif key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
