# drawing shapes on an image with OpenCV

import cv2
import numpy as np 
import matplotlu.pyplot as plt 

%matplotlib inline

# create black image to work on

black_img = np.zeros(shape = (512, 512, 3), dtype = np.int16)

# get shape of image

print(black_img.shape)

# show the image

plt.inshow(black_img)

# draw circle

cv2.circle(img = black_img, center = (400, 100), radius = 50, color = (255, 0, 0), thickness = 5)
plt.imshow(black_img)

# filled circle

cv2.circle(img = black_img, center = (400, 200), radius = 50, color = (0, 255, 0), thickness = -1)
plt.imshow(black_img)

# draw rectangle

cv2.rectangle(black_img, pt1 = (200, 200), pt2 = (300, 300), color = (100, 100, 255), thickness = 2)
plt.imshow(black_img)

# filled rectangle just change thickness to -1

# draw triangle

vertices = np.array([[10, 450], [110, 350], [180, 450]], np.int32)
pts = vertices.reshape(-1, 1, 2)
cv2.polylines(black_img, [pts], isClosed = True, color = (0, 0, 255), thickness = 4)
plt.imshow(black_img)

# filled triangle uses fillPoly instead

vertices = np.array([[300, 300], [350, 450], [300, 450]], np.int32)
pts = vertices.reshape(-1, 1, 2)
cv2.fillPoly(black_img, [pts], color = (200, 0, 200))
plt.imshow(black_img)

# draw line

cv2.line(black_img, pt1 = (0, 500), pt2 = (500, 0), color = (200, 0, 100), thickness = 3)
plt.imshow(black_img)

# write text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putTest(black_img, text = 'Rhyme', org = (210, 500), fontFace = font, fontScale = 3, color = (255, 255, 0), thickness = 3, lineType = cv2.LINE_AA)
plt.imshow(black_img)