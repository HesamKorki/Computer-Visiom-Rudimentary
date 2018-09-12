import numpy as np
import cv2

I = cv2.imread('masoleh.jpg', cv2.IMREAD_UNCHANGED)
B = I.copy()
# notice that OpenCV uses BGR instead of RGB!
B[:,:,1]=0;
B[:,:,2]=0;

G = I.copy()
G[:,:,0]=0;
G[:,:,2]=0;

R = I.copy()
R[:,:,0]=0;
R[:,:,1]=0;

cv2.imshow('masoleh',I)
while True:
    k = cv2.waitKey()
    cv2.destroyAllWindows()

    if k == ord('b'):
        cv2.imshow('Blue',B)
    elif k == ord('g'):
        cv2.imshow('Green',G)
    elif k == ord('r'):
        cv2.imshow('Red',R)
    elif k == ord('q'):
        break



cv2.destroyAllWindows()