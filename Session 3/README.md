# **Session 3**

#### **Using python 2.7 and opencv 3**

*Welcome to the third session of Computer Vision Rudimentary*

☑️*Contact me: Hesam.korki@gmail.com*

*All the rights of this project are reserved for Hesam Korki.*

## **Goals**

- *Reading and displaying videos*
- *Working with histograms*

- *TASKs*:
- *Reversing a video*
- *Expanding the histogram*

## **Training**

This session is comprised of two different parts. first of which is pertinent to videos and working with them in python.

### **Part 1: Videos**

You can find a short video clip called "kntu-computer.avi" in this folder attachments. The following code would open the video and displays it. Notice that you may use any other video by changing the related path.

Try practicing this because it is very fundamental:

- Reading and displaying a video:
```
import numpy as np
import cv2
# create a VideoCapture object
cap = cv2.VideoCapture('kntu-computer.avi')
# sometimes this is needed:
# if not cap.isOpened():
#    cap.open();
while True:
    ​# Capture frame-by-frame
    ​ret,I = cap.read()
    ​​if ret == False: ​# end of video (perhaps)
    ​    break
    ​cv2.imshow('win1',I) ​# Display I
    ​​key = cv2.waitKey(33) ​# ~ 30 frames per second
    ​​if key == ord('q'): ​# exit when “q” is pressed
        ​​​​break
    ​​​​​# replace the above with "if key 0xFF == ord('q')" # if it fails
​cap.release()
​cv2.destroyAllWindows()
​
```
*_ key = cv2.waitKey(33) creates a delay of 33 milisecond, and actually this delay is the definition of fps (frame per second). Try changing it to 2 or 299 and see what happens. _*

The following code reads a video called "eggs.avi" and then, saves the frames into another video named "eggs-reverse.avi".

- Writing a video on the disk
```
import​ numpy ​as​ np import​ cv2
# create a VideoCapture object
cap​ = cv2.VideoCapture(​'eggs.avi')

# get the dimensions of the frame
# you can also read the first frame to get these
w​ = ​int​(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) ​# width of the frame
h​ = ​int​(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) ​# height of the frame
fourcc​ = cv2.VideoWriter_fourcc(*​'XVID'​) ​# choose codec
out​ = cv2.VideoWriter(​'eggs-reverse.avi'​,fourcc, 30.0, (w,h))

while​ ​True​:
    ​ret​, ​I​ = cap.read()
    ​​if​ ret == ​False​: #​ end of video (or error)
    ​   break
​# write the current frame I
​out.write(I)
​cap.release()
​out.release()
​
```

### **Part 2: Histograms**

In this part we use matplotlib (not OpenCV) in order to show histograms, for it is more convinient and we can see the histogram and the picture itself simultaneously.

```
import​ cv2
import​ numpy ​as​ np
from​ matplotlib ​import​ pyplot ​as​ plt
fname​ = ​'crayfish.jpg'
#fname = 'office.jpg'
I​ = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
f​, ​axes​ = plt.subplots(2, 3)
axes[0,0].imshow(I, ​'gray'​, vmin=0, vmax=255)
axes[0,0].axis(​'off'​)
axes[1,0].hist(I.ravel(),256,[0,256]);
plt.show()

```
**plt.subplots(2,3)​creates a 2 by 3 array of subplots (2 rows, 3 columns). By running the above code, you can see that only the first column of the subplots are used (axes[0,0] and axes[1,0]). The image is plotted in axes[0,0] and its histogram in axes[1,0].**


Now we know how to get histogram of a pictute in python and plot it. Plus, we received some information about videos and working with them in python. Hence, it is the time to assess our knowledge.

*_DO NOT just read the train part and pass. Try these codes on your own platform and feel the results _*
## **TASKs**
We expect you to perform these tasks on your own. However, there are python files attached which contains the answers.

### *Task1*
Remember that "reverse-eggs.avi" that we saved to our disk. Write a code that would read the "eggs.avi" and save the frames in reverse order. In other words, "reverse-eggs.avi" should be a backward playback of "eggs.avi". Feel free to run your code on any other video, and it must work.

### *Task2*
We want to linearly expand the histogram to get a better contrast. Determine points ​a​ and ​b​ for linear histogram expansion according to the original image's histogram. There are several grayscale images in this session's directory that you can use either one of them. Now, you should fill the 2*3 subplot. First column , the original image and its histogram. Second column, the linear expanded image and its histogram. Third column, the histogram equalized picture and its histogram.
*hint:*
- *Values of 'a' and 'b' are the least and the most value possible for the histogram, respectively.*
- *There is a function in OpenCV that would get equalized histogram from any picture, you can find it [here](https://docs.opencv.org/3.0-beta/modules/imgproc/doc/histograms.html?highlight=cv2.equalizehist#cv2.equalizeHist).

*Had you have any further questions, you are welcome to ask me.*

☑️Email: Hesam.korki@gmail.com

*Hope that you find this helpful.*

*Best Regards,*
**Hesam Korki**

