import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	originalImg = frame
	grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	grey = cv2.GaussianBlur(grey, (41,41), 0)#40,40 are really arbitrary
	minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(grey)
	cv2.circle(originalImg, maxLoc, 5, (0, 255, 0), 2)
	cv2.circle(originalImg, minLoc, 5, (255, 0, 0), 2)

	cv2.imshow("image",originalImg)

	inputKey = cv2.waitKey(0)
	cv2.destroyAllWindows()
	if chr(inputKey & 255) == 'q':
		break

cap.release()
cv2.destroyAllWindows()