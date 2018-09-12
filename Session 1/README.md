# **Session 1**

#### **Using python 2.7 and opencv 3**

*Welcome to the first session of Computer Vision Rudimentary*

☑️*Contact me: Hesam.korki@gmail.com*

*All the rights of this project are reserved for Hesam Korki*

## **Goals**

- *Introducing the mandatory impelements: #Python2.7 #Opencv3 #Numpy #CV2*

- *Reading an image and concatenating it with its vertically inverted image*

## **Numpy**
The most useful package for computer vision is numpy and using it is inevitable. Basically, it would help us do the simple math and whatever you think on arrays. You can find the necessary information and tutorials on their website [NumPy](http://www.numpy.org/).
After you did install the package, Try these codes and check the results to get to know the usage of this package:
- Basic Operations: 
    ```
    import numpy as np
    a = np.array([1,2,3])
    b = np.array([4,5,6])
    a+b
    a*b
    a-b
    a**b
    a.dtype
    a/b
    
    ```
- Slicing:  
    ```
    a = np.array([0,10,20,30,40,50,60,70,80,90,100])
    a[2]
    a[2:8]
    a[2:-1]
    a[8:2:-1]
    a[::-1]
    ```
- 2D arrays(*it is important since we consider an image as a 2D array*):
    ```
    A = np.zeroes((4,6), dtype = np.uint8)
    A
    A = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
    A[1,2]
    A[0,-1]
    A.shape
    A.shape[0]
    
    ```
 - Concatenation:
    ```
    X = np.array([1,2],[3,4])
    Y = np.array([10,20,30],[40,50,60])
    Z = np.array([7,7],[8,8],[9,9])
    Z
    X
    np.concatenate((X,Z))
    np.concatenate((X,Z), axis=0)
    Y
    np.concatenate((X,Y), axis=1)
    np.vstack((X,Z))
    np.r_[X,Z]
    np.hstack(X,Y)
    np.hstack((X,Y))
    np.c_[X,Y]
    Y
    np.tile(Y,(4,3))
    
    ```
       



## **Matplot**
One approach for plotting functions in general is using Matplotlib:
    ```
    from matplotlib import pyplot as plt
    x = np.arange(0, 2 * np.pi, 0.1)
    x
    y = np.cos(x)
    y
    plt.plot(x,y)
    plt.show()
    plt.plot(x,np.sin(x))
    plt.plot(x,np.cos(x))
    plt.show()
    ```


### **Cv2**
Cv stands for Computer Vision as you may noticed. Generally, all of the image related functions are in this package and we will be using it constantly.
Here are some integral exploitation:

- Reading an image
    ```
    import cv2
    I = cv2.imread('the path of the image')
    ```
- Monitoring the output
    ```
    cv2.imshow('arbitrary name for the window',I)
    cv2.waitKey(0)
    ```
## **SetSVMDetector**

Now that we have our support vector, we can easily set our svmdetector using the class `HOG.setSVMDetector()`.

*One crucial fact about OpenCV’s SVM detector is that it takes the SVM parameters in the following order:*

*the coefficients of support vectors machine followed by the intercept (constant) of the model.*

So it has to be like this:
```
supportvectors.append(np.dot(svm.dual_coef_,svm.support_vectors_)[​0​])
supportvectors.append([svm.intercept_])
supportvectors = list(itertools.chain(*supportvectors))
#passing the model params to HOG
HOG.setSVMDetector(np.array(supportvectors, dtype=np.float64))
```

## **Testing and drawing a box around pedestrians**

We will use class `HOG.detectMultiScale()` in order to get a moveable window through our test image and different scales of our test image. The whole information you need to deal with to comprehend its parameters and functionality is mentioned here:

[HoG.Multiscale() parameters](https://www.pyimagesearch.com/2015/11/16/hog-detectmultiscale-parameters-explained/)

*Had you have any further questions, you are welcome to ask me*

☑️Email: Hesam.korki@gmail.com

*Hope that you find this helpful.
Best Regards Hesam Korki*

