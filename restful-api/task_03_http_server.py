#!usr/bin/puthon3
"""
restful-api.task_03_http_server
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps


class BeautifulServer(BaseHTTPRequestHandler):
    """
    Class BeautifulServer
    """
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))

        elif self.path == '/data':
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_data = dumps(data)
            self.wfile.write(json_data.encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'apllication/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            self.wfile.write(dumps(info).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Endpoint not found".encode('utf-8'))


if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, BeautifulServer)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()
