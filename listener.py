from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess

MAC_ADRESS = "00:D8:61:C8:20:5E"

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/wakeup":
            self.send_response(200)
            self.end_headers()
            subprocess.call(["wakeonlan", MAC_ADRESS])
            self.wfile.write(b'Woken UP !')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')
        


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()