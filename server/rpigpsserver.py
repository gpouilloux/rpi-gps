#!/usr/bin/python

import os
from BaseHTTPServer import HTTPServer 
from CGIHTTPServer import CGIHTTPRequestHandler

os.chdir('/home/pi/rpi/rpi-gps/server')

handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin', '/htbin']  # this is the default

PORT = 8088
server = HTTPServer(('192.168.2.1', PORT), handler)
print 'serving at port : %d' % PORT
server.serve_forever()
