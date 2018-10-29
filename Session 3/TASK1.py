import numpy as np
import cv2
cap = cv2.VideoCapture('eggs.avi')
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('eggs-reverse.avi', fourcc , 30.0 , (w,h))

buffer = []
ret , I = cap.read()


while True :
    ret , I = cap.read()
    if ret == False :
        break
    buffer.append(I)
l = len(buffer)
for i in range(l):



    out.write(buffer[l-i-1])

cap.release()
cv2.destroyAllWindows()

