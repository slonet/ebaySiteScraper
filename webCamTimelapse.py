### webCamTimelapse.py
#
# A python script that takes photos using a usb web cam with a specific period.
# 
### Author:
#
# Tyler Slone
# 11/17/2018
#

import time
from subprocess import call

save_dir = '/media/pi/FLASH_DRIVE'
period = None

### Set up the timelapse capture
def init():
	try:
		global period
		period = float(input('Please enter a timelapse period in minutes: '))*60

	except:
		print('\nPlease enter a positive number...')
		init()

	global save_dir
	special_chars = [['.'],[' '],['~'],['\\'],['/'],[','],[';'],[':'],['|'],['`']]
	name = input('Please name the timelapse set: ')

	try:
		for i in range(0,len(special_chars)):
			
			if name.find(special_chars[i]) != -1:
				raise Exception('Invalid name')

		save_dir = save_dir + '/' + name

	except:
		print('\nPlease do not use spaces or special characters')
		init()
	try:

	print('\nPeriod = %f, Save Directory = %s') % (period, save_dir)



init()