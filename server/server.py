from BaseHTTPServer import HTTPServer 
from CGIHTTPServer import CGIHTTPRequestHandler

handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin', '/htbin']  # this is the default

PORT = 8088
server = HTTPServer(('localhost', PORT), handler)
print 'serving at port : %d' % PORT
server.serve_forever()
