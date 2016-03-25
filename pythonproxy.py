import SocketServer
import SimpleHTTPServer
import urllib

PORT = 8000

class Foo(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.lower().find("wfs") != -1:
            self.path = self.path[5:]
            print self.path
            self.copyfile(urllib.urlopen(self.path), self.wfile)
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpd = SocketServer.TCPServer(('', PORT), Foo)
print "serving at port", PORT
httpd.serve_forever()
