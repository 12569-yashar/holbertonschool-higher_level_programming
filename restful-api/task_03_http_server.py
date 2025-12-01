#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "localhost"
PORT = 8000

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type="text/plain"):
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self._set_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self._set_headers(content_type="application/json")
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/status":
            self._set_headers()
            self.wfile.write(b"OK")
        elif self.path == "/info":
            self._set_headers(content_type="application/json")
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode("utf-8"))
        else:
            self._set_headers(status_code=404)
            self.wfile.write(b"Endpoint not found")

def run_server():
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Starting server at http://{HOST}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
        httpd.server_close()

if __name__ == "__main__":
    run_server()

