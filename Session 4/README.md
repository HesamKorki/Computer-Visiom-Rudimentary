# **Session 4**

#### **Using python 2.7 and opencv 3**

*Welcome to the fourth session of Computer Vision Rudimentary*

☑️*Contact me: Hesam.korki@gmail.com*

*All the rights of this project are reserved for Hesam Korki.*

## **Goals**

- *Blurring images with Gaussian noise*
- *Working with filters such as box filter*
- *Smoothing images with Gaussian kernel*

## *Tasks*
- *Simulating snow noise*
- *Building a filter bank*

## **Training**

### **Part 1: Guassian noise**

First of all, we will learn how to add Gaussian noise to images. Why Gaussian noise? Well in practice, anything that we do would contain noise, and the noise is mostly normally distributed that is Gaussian noise.

**Now Let's Get right to it**

apprehend the following code and run it for yourself.

```
import​ numpy ​as​ np
import​ cv2
I​ = cv2.imread(​'Google_HQ.jpg'​, cv2.IMREAD_GRAYSCALE);
# convert I to floating point from unsigned integer
# Note: For displaying floating point images the maximum
# intensity has to be 1 instead of 255
I​ = I.astype(np.​float​) / 255
# create the noise image
sigma​ = 0.04 ​# notice maximum intensity is 1
N​ = np.random.randn(*I.shape) * sigma
# add noise to the original image
J​ = I+N;
cv2.imshow(​'original'​,I)
cv2.waitKey(0) ​# press any key to exit
cv2.imshow(​'noisy image'​,J)
cv2.waitKey(0) ​# press any key to exit
cv2.destroyAllWindows()
```
- __NOTE: An asterisk ​"*"​ before an argument in a python function call, gives elements of the argument (which is typically a tuple) as argument to the function. In the above, if ​I.shape = (200,300)​, then ​np.random.randn(*I.shape) ​is the same thing as​ np.random.randn(I.shape[0],I.shape[1])​.__

- Try different values of sigma and sense the results.

### **Part 2: Image Smoothing/Blurring**

- __Box Filter__

If you are not familiar with the box filter and its application, try reading [this document](https://docs.opencv.org/3.0-beta/modules/imgproc/doc/filtering.html?highlight=box%20filter#cv2.boxFilter).

*Smoothing images with a box kernel*
```
import​ numpy ​as​ np
import​ cv2
I​ = cv2.imread(​'Google_HQ.jpg'​).astype(np.float64) / 255;
# display the original image
cv2.imshow(​'original'​,I)
cv2.waitKey()
# creating a box filter
m​ = 7 ​# choose filter size
# create an m by m box filter
F​ = np.ones((m,m), np.float64)/(m*m)
print​ F
# Now, filter the image
J​ = cv2.filter2D(I,-1, F)
cv2.imshow(​'blurred'​,J)
cv2.waitKey()
cv2.destroyAllWindows()

```
   - Alter the value of "m" and see what happens.
   - Why division by (m*m) in F​ = np.ones((m,m), np.float64)/(m*m)?


- __Guassian Kernel__

The actual outline of what we are doing here is creating a 1D Gaussian kernel at first. Then, make it a 2D kernel out of the 1D kernel and after that apply it to the image.

```
import​ numpy ​as​ np
import​ cv2
I​ = cv2.imread(​'Apple_HQ.jpg'​).astype(np.float64) / 255;
m​ =13; ​#we will create an m by m filter
# create a 1D Gaussian filter
Fg​ = cv2.getGaussianKernel(m, sigma=-1);
# by setting sigma=-1, the value of sigma is computed
# automatically as: sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8
print​ Fg
print​ Fg.shape ​# Fg is 1-dimensional (m by 1)

#​ Now we create a 2D filter
# We use matrix multiplication to create an m by m 2D filter
# out of "m by 1" and "1 by m" 1D filters, which in this case happens
# to be the same thing as the correlation between 1D filters
Fg​ = Fg.dot(Fg.T)​ ​# an "m by 1" matrix multiplied by a "1 by m" matrix
print​ Fg
print​ Fg.shape

# filter the image with the Gaussian filter
Jg​ = cv2.filter2D(I,-1, Fg)
cv2.imshow(​'original'​,I)
cv2.waitKey()
cv2.imshow(​'blurred_Gaussian'​,Jg) cv2.waitKey()
cv2.destroyAllWindows()
```
   - Alter the value of "m" and check what changes.
   - This approach is for understanding deeply, you can easily use [guassianblur](https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html#void%20GaussianBlur(InputArray%20src,%20OutputArray%20dst,%20Size%20ksize,%20double%20sigmaX,%20double%20sigmaY,%20int%20borderType)) function.

**DO NOT just read the train part and pass. Try these codes on your platform and feel the results.**

## **TASKs**
We expect you to perform these tasks on your own. However, there are python files attached which contains the answers.

### *Task1*
We want to simulate white noise (__snow noise__ ) in the old analog TVs. You need to read an image, and then, in every iteration of a loop add a different​ randomly generated Gaussian noise to it. We show the image at around ​30 frames per second (​Hence, the command ​cv2.waitKey(33)​)​. Notice that you need to create a new noise image at every new frame (in most cases with the same sigma). Your program must increase or decrease the intensity of noise when the user presses the keys ​"u" and ​"d," respectively. __​Notice that sigma should never get negative__.


### *Task2*
This Task is a supplement to the first one. Create a filter bank in which the following keys correspond to a particular filter as mentioned.
- __press the "b" key:__ use box filter
- __press the "g" key:__ use Gaussian filter
- __press the "+" key:__ increase the filter size (m)
- __press the "-" key:__ decrease the filter size (m)
- __press the "u" key:__ increase the intensity of noise
- __press the "d" key:__ decrease the intensity of noise
- __press the "q" key:__ quit the program an close all windows


*Had you have any further questions, you are welcome to ask me.*

☑️Email: Hesam.korki@gmail.com

*Hope that you find this helpful.*

*Best Regards,*
**Hesam Korki**

