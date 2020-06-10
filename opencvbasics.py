# Computer Vision with OpenCV Basics

import numpy as np
import matplotlib.pyplot as plt 

%matplotlib inline

# use PIL for the image

from PIL import Image 

img = Image.open('images/rock.jpg')

# rotate the image

img.rotate(-90)

# check image type

print(type(img))

# turn image into an array

img_array = np.asarray(img)
print(type(img_array)) # prints numpy.ndarray

# get height, width, and channels

print(img_array.shape) 
plt.imshow(img_array)

# RGB channels (red, green, blue)
# color values from 0 to 255

img_test = img_array.copy()

# only RED channel

plt.imshow(img_test[:, :, 0]) # img_test[width, height, color channel]

# scale RED channel to gray

plt.imshow(img_test[:, :, 0], cmap = 'gray') # American spelling of gray

# only GREEN channel

plt.imshow(img_test[:, :, 1]) 

# scale GREEN channel to gray

plt.imshow(img_test[:, :, 1], cmap = 'gray') 

# only BLUE channel

plt.imshow(img_test[:, :, 2])

# scale BLUE channel to gray

plt.imshow(img_test[:, :, 2], cmap = 'gray') 

# remove red color

img_test[:, :, 0] = 0 # access the red channel, set to 0
plt.imshow(img_test) # results in blue-green image

# remove green color from red-less image

img_test[:, :, 1] = 0
plt.imshow(img_test) # results in blue image

# remove blue from blue-only channel

img_test[:, :, 2] = 0
plt.imshow(img_test) # results in black image

# openCV

import cv2

# get image with imread

img = cv2.imread('images/rock.jpg')

# check type

print(type(img)) # prints numpy.ndarray

# get image shape and show

print(img.shape)
plt.imshow(img)

# Matplotlib is RGB (comes out more reddish)
# OpenCV is BGR (comes out more blueish)

# convert OpenCV to RGB

img_fix = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_fix)

# scale to gray

img_gray = cv2.imread('images/rock.jpg', cv2.IMREAD_GRAYSCALE)
print(img_gray.shape)
plt.imshow(img_gray, cmap = 'gray')


# resize image
img_new = cv2.resize(img_fix(1000, 400)) #img_fix(width, height)
plt.imshow(img_new)

# resize with ratio

width_ratio = 0.5
height_ratio = 0.5

img2 = cv2.resize(img_fix, (0, 0), img_fix, width_ratio)
plt.imshow(img2)

print(img2.shape)

# flip on horizontal axis

img_3 = cv2.flip(img_fix, 0)
plt.imshow(img_3)

# flip on veritical axis

img_3 = cv2.flip(img_fix, 1)
plt.imshow(img_3)

# flip on horizontal and vertcal axis

img_3 = cv2.flip(img_fix, -1)
plt.imshow(img_3)

# change canvas size

last_img = plt.figure(figsize = (10, 7))
ilp = last_img.add_subplot(111)
ilp.imshow(img_fix)