# **Session 2**

#### **Using python 2.7 and opencv 3**

*Welcome to the second session of Computer Vision Rudimentary*

☑️*Contact me: Hesam.korki@gmail.com*

*All the rights of this project are reserved for Hesam Korki.*

## **Goals**

- *Understanding the concept of RGB and grayscale*

- *TASKs:*
1- differentiate the color channels
2- Creating a smooth animation from one image to another 

## **Training**

There are a myriad of ways in which you can read and display an image in python. However, we will be using a particular
way throughout the sessions which is the most readily one.
* Remember that OpenCv uses BGR system that is B=0, G=1, R=2*
Try practicing these because they are very fundamental:
- Reading and displaying a grayscale image:
    ```
    import numpy as np
    import cv2
    I = cv2.imread('masoleh_gray.jpg', cv2.IMREAD_UNCHANGED)
    I.shape
    I.dtype
    I[10,20]
    cv2.imshow('Masoleh Village', I)
    cv2.waitKey(10000)​ # display the image for 10 seconds
    cv2.destroyAllWindows()
    I = cv2.imread('masoleh.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Masoleh grayscale', I)
    cv2.waitkey(0) #waits until you press a button
    cv2.destroyAllWindows()
    ```
- Reading and displaying a colored image:
    ```
    I = cv2.imread('masoleh.jpg', cv2.IMREAD_UNCHANGED)
    I.shape
    I.dtype
    cv2.imshow('Masoleh Village', I)
    cv2.waitKey(10000)​ # display the image for 10 seconds
    cv2.destroyAllWindows()
    I = cv2.imread('masoleh.jpg')
    cv2.imshow('Masoleh ', I)
    cv2.waitkey(0) #waits until you press a button
    cv2.destroyAllWindows()
    ```
- Setting the green channel zero and save the image:
    ```
    I = cv2.imread('masoleh.jpg')
    I[:,:,1] =0;
    cv2.imshow('without G',I)
    cv2.imwrite('masoleh_withoutG',I) #this line saves the image
    cv2.waitkey(0)

    ```
- Keyboard response:
    ```
    k = cv2.waitKey()
    if k == ord('q') :
        cv2.destroyAllWindows()

    ```
- Blending two images:
    ```
    I = cv2.imread('damavand.jpg')
    J = cv2.imread('eram.jpg')
    K = I/2 + J/2
    cv2.imshow('Blended',K)
    # Now you can give weight to each picture
    K = (0.8*I + 0.2*J).astype(np.uint8)
    ```
## **TASKs**
We expect you to perform these tasks on your own. However, there are python files attached which contains the answers.

### *Task1*
You should write a code that would read a colored image(masoleh.jpg), and display each channel individually in merely that color by pressing the shortcut.
To illustrate, when you press "b" on the keyboard, you should get only blue parts of the image.

### *Task2*
Make an animated smooth transition from image​ I​ to ​J​. You can use cv2.waitKey(n) to delay for n milliseconds. Conspicuously, you should use Blending.

*Had you have any further questions, you are welcome to ask me.*

☑️Email: Hesam.korki@gmail.com

*Hope that you find this helpful.*

*Best Regards,*
**Hesam Korki**
