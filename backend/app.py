
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = os.getenv("APP_MESSAGE", "Backend is working!")

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

server = HTTPServer(("0.0.0.0", 5000), MyHandler)

print("Python backend running on port 5000")

server.serve_forever()
