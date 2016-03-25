import SocketServer
import SimpleHTTPServer
import urllib

PORT = 8000

class Foo(SimpleHTTPServer.SimpleHTTPRequestHandler):
#    def __init__(self,*args):
#        SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(args)

    def do_GET(self):
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpd = SocketServer.TCPServer(('', PORT), Foo)
print "serving at port", PORT
httpd.serve_forever()
