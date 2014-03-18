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
	out = ''
	while ser.inWaiting() > 0:
		out += ser.readline()
		
	if out != '':
		print '<p>'+out+'</p>'
	else:
		print '<p>Error</p>'
				
except serial.serialutil.SerialException:
	print '<p>Error</p>'
