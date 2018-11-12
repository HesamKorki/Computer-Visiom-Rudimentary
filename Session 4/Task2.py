import numpy as  np
import cv2

I = cv2.imread('Google_HQ.jpg',cv2.IMREAD_GRAYSCALE)
I = I.astype(np.float)/255

noise_sigma = 0.04
m=1
filter ='b'
while True:
    N = np.random.randn(*I.shape)* noise_sigma
    J = I + N
    if filter == 'b' :
        F = np.ones((m,m),np.float64)/(m*m)
        K = cv2.filter2D(J, -1, F)
    elif filter == 'g':
        K = cv2.GaussianBlur(J,(m,m),-1)
        pass



    cv2.imshow('filtered',K)
    key = cv2.waitKey(30) & 0xFF

    if key == ord('b'):
        filter = 'b'
        print 'Box Filter'
        pass
    elif key == ord('g'):
        filter = 'g'
        print 'Gaussian Filter'
        pass
    elif key ==ord('+'):
        m = m +2
        print 'm=',m
        pass
    elif key == ord('-'):
        if m >=3 :
            m = m -2
        print 'm=',m
        pass
    elif key == ord('u'):
        noise_sigma = noise_sigma + 0.005
        pass
    elif key == ord('d'):
        if noise_sigma >= 0.006 :
            noise_sigma = noise_sigma - 0.005
            pass
        pass
    elif key == ord('q'):
        break

cv2.destroyAllWindows()
