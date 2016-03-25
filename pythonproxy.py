import SocketServer
import SimpleHTTPServer
import urllib

PORT = 8000

class Proxy(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.lower().find("wfs") != -1:
            self.path = self.path[5:]
            self.copyfile(urllib.urlopen(self.path), self.wfile)
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpd = SocketServer.TCPServer(('', PORT), Proxy)
print "serving at port", PORT
httpd.serve_forever()
