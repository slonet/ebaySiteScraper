### webCamTimelapse.py
#
# A python script that takes photos using a usb web cam with a specific period.
# 
### Author:
#
# Tyler Slone
# 11/17/2018
#

import argparse
import time
from subprocess import call

save_dir = ''
period = None

### Set up the timelapse capture
def init():
	global period
	global save_dir
	
	try:	
		period = float(input('Please enter a timelapse period in minutes: '))*60

	except:
		print('\nPlease enter a number')
		init()

	try:
		save_dir = input('Please enter the save directory with quotes: ')
		call(['mkdir', save_dir])

	except:
		print('\nPlease enter a valid directory')
		init()

	print('\nPeriod = %f, Save Directory = %s') % (period, save_dir)

init()