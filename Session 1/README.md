# **Session 1**

#### **Using python 2.7 and opencv 3**

*Welcome to the first session of Computer Vision Rudimentary*

☑️*Contact me: Hesam.korki@gmail.com*

*All the rights of this project are reserved for Hesam Korki*

## **Goals**

- *Introducing the mandatory impelements: #Python2.7 #Opencv3 #Numpy*

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


## **HoG Descriptor**

You can find the official documentation here:

[HoG Descriptor](https://docs.opencv.org/3.4.1/d5/d33/structcv_1_1HOGDescriptor.html)

In order to set the conductor parameter of HoGDescriptor, we will create an XML file.

After reading images and extracting their features with the `HoG.compute()` class, append them to an empty list and give the label of 1 to those including pedestrian in them and 0 to those not including pedestrians.

## **Training our SVM**

In this project, the goal is to use a custom SVM classifier and not ~~the cv2.HOGDescriptor_getDefaultPeopleDetector()~~, and that is the meaning of training.

Now we have to train a SVM classifier. OpenCV provides its implementation of SVM. But since OpenCV’s SVM is not properly documented, we will be using the `SVC (support vector classifier)` class in the scikit-learn library, a very popular machine learning package. Find the documentation here:

[SVC from scikit.svm](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)


### **Pickle Trick**


Since the process of training involves reading up to 5000 pictures and extracting their features, it will take time and of course something about 1.5 GB of your RAM.

So we will train our classifier only once and save it with the pickle library and load the file for other times.

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

