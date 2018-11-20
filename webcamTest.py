from cv2 import *

cam = VideoCapture(0)
s, img = cam.read()

if s:
	namedWindow('Camera Test')
	imshow('Camera Test', img)
	waitKey(0)
	destroyWindow('Camera Test')
	#imwrite('testImage.jpg',img)
else:
	print('Could not capture an image')