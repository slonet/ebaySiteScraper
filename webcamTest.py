from cv2 import *

cam = VideoCapture(0)
s, img = cam.read()

if s:
	imwrite('testImage.jpg',img)
else:
	print('Could not capture an image')