# drawing with mouse with OpenCV

# import libraries

import cv2
import numpy as np 

# function
# x, y, flags, param are fed from OpenCV automatically

def draw_circle(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		# image, center, radius, color, thickness
		cv2.circle(img, (x, y), 20, (35, 60, 78), -1)
	elif event == cv2.EVENT_RBUTTONDOWN:
		# image, center, radius, color, thickness
		cv2.circle(img, (x, y), 70, (35, 60, 78), -1)

# connect function with callback

cv2.namedWindow(winname = 'my_drawing')

# callback

cv2.setMouseCallback('my_drawing', draw_circle)

# using OpenCV to show the Image

imp = np.zeros((512, 512, 3), np.int8)

while True:
	cv2.imshow('my_drawing', img)
	if cv2.waitKey(5) & 0xFF == 27:
		# if press escape key (27) break
		break

cv2.destroyAllWindows()