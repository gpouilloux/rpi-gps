#!/usr/bin/python

import cgi, cgitb 
import serial
import sys
import time

cgitb.enable()  # for troubleshooting
print "Content-Type: text/html\n\n"
try:
	ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=3)
	#ser.write('sno, Stream1, COM1, +GSV+GLL, sec1'+'\r')
	ser.write('enoc, COM1, +GSV+GLL'+'\r')
	time.sleep(1)
	total = ''
	while ser.inWaiting() > 0:
		out = ser.readline()
		if "$GPGLL" in out:
			gll = out
		elif "$GPGSV" in out:
			gsv = out
		total += out
		
	if total != '':
		coord = gll.split(',')
		sat = gsv.split(',')
		print '<p>Latitude : '+coord[1]+','+coord[2]+'</p>'
		print '<p>Longitude : '+coord[3]+','+coord[4]+'</p>'
		print '<p>Number of satellites : '+sat[3]+'</p>'

	else:
		print '<p>Error</p>'
				
except serial.serialutil.SerialException, e:
	print '<p>Error : '+str(e)+' </p>'
