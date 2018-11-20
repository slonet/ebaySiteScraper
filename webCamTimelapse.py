### webCamTimelapse.py
#
# A python script that takes photos using a usb web cam with a specific period.
# 
### Author:
#
# Tyler Slone
# 11/17/2018
#

import cv2
import time
import datetime
from subprocess import call

#save_dir = ''
save_dir = '/media/pi/FLASH_DRIVE/pee-wee'
period = 15

### Set up the timelapse capture
def init():
	#global period
	#global save_dir
	
	#try:	
	#	period = float(input('Please enter a timelapse period in minutes: '))*60

	#except:
	#	print('\nPlease enter a number')
	#	init()

	try:
	#	save_dir = input('Please enter the save directory with quotes: ')
		call(['mkdir', save_dir])

	except:
		print('\nPlease enter a valid directory')
	#	init()

def captureImage(name_str):
	cam = cv2.VideoCapture(0)
	s, img = cam.read()
	
	current_time = datetime.datetime.now()
	stamp = current_time.strftime('%Y-%m-%d_%H-%m') + name_str
	img_dir = save_dir + '/' + stamp + '.jpg'
	print(img_dir)
	cv2.imwrite(img_dir,img)

	if s:
		cv2.imwrite('testImage.jpg',img)
	
	else:
		print('\nCould not capture image')


def runTimelapse():
	img_no = 0

	while(True):
		captureImage('_image_' + str(img_no))
		print('Successfully captured image. Next image in ' + str(period/60) + ' minutes')
		time.sleep(period)
		img_no = img_no + 1

init()
runTimelapse()