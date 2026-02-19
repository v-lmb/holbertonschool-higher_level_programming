#!usr/bin/puthon3
"""
restful-api.task_03_http_server
"""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
	Class SimpleAPIHandler
	"""
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'apllication/json')
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            error_msg = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_msg).encode('utf-8'))


if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Serving on port 8000")
    httpd.serve_forever
