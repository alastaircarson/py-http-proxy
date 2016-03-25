import SocketServer
import SimpleHTTPServer
import urllib

PORT = 8000

class Proxy(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = self.path[1:]
        print self.path
        print self.wfile
        if self.path.lower().find("wfs"):
            self.copyfile(urllib.urlopen(self.path), self.wfile)
        else:
            super(Proxy, self).do_GET()

httpd = SocketServer.TCPServer(('', PORT), Proxy)
print "serving at port", PORT
httpd.serve_forever()
