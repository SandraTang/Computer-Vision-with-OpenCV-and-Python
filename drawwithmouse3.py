# more mouse functions

import cv2
import numpy as np 

# vars
# true when mouse button down
# false when mouse button up

drawing = False 
ex = -1
ey = -1

# functions
# x, y, flags, param fed from OpenCV automatically

def draw_rectangle(event, x, y, flags, params):
	global ex, ey, drawing
	if event == cv2.EVENT_LBUTTOMDOWN:
		drawing = True 
		ex, ey = x, y
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
	elif event == cv2.EVENT_LBUTTOMUP:
		drawing = False 
		cv2.rectangle(img, (ex, ey), (x, y), (255, 0, 255), -1)


# connect function with callback

img = np.zeros((512, 512, 3), np.int8)
cv2.namedWindow(winname = 'my_drawing')

# callback

cv2.setMouseCallback('my_drawing', draw_rectangle)

# using OpenCV to show the image

while True:
	cv2.imshow('my_drawing', img)
	if cv2.waitKey(5) & 0xFF == 27:
		# if press escape key (27) break
		break

cv2.destroyAllWindows()