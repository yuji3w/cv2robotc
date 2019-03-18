import numpy as np
import cv2

cap = cv2.VideoCapture(0)


while(True):
	ret, frame = cap.read()
	originalImg = frame
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	duplicateGray = gray.copy()

	gray = cv2.GaussianBlur(gray, (99,99), 0) #image dims are 640, 480 so this is 1/5 of pic
	minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(gray)
	cv2.circle(originalImg, maxLoc, 5, (0, 255, 0), 2)
	cv2.circle(originalImg, minLoc, 5, (255, 0, 0), 2)

	#experimental countouring
	ret, thresh = cv2.threshold(duplicateGray,127,255,0)
	duplicateGray, contours, hier = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) #retr list ignores hierarchy
	#cv2.drawContours(originalImg, contours, -1, (0,255,0), 3)
	#cv2.imshow("image",originalImg)

	squareHull = []

	for cnt in contours:
		if cv2.contourArea(cnt)>5000:
			hull = cv2.convexHull(cnt)
			hull = cv2.approxPolyDP(hull,0.1*cv2.arcLength(hull,True),True) #.1 is a good value for max length variance
			if len(hull) == 4:
				squareHull = hull
				cv2.drawContours(originalImg,[hull],0,(0,255,0),2)
			"""if len(hull)==4:
				cv2.drawContours(originalImg,[hull],0,(0,255,0),2)"""
	#implement biggest contour wins, canny

	fHeight, fWidth, fChannels = originalImg.shape

	xAvg = yAvg = 0;
	if(len(squareHull) == 4):
		for coord in squareHull:
			xAvg += coord[0][0]
			yAvg += coord[0][1]
		xAvg /= 4
		yAvg /= 4

	if(xAvg > fWidth/2):
		print("RIGHT")
	else:
		print("LEFT")

	if(yAvg > fHeight/2):
		print("LOW")
	else:
		print("HIGH")

	#displays the image with circles for darkest/lightest
	cv2.imshow("image",originalImg)

	inputKey = cv2.waitKey(0)
	cv2.destroyAllWindows()
	if chr(inputKey & 255) == 'q':
		break

cap.release()
cv2.destroyAllWindows()