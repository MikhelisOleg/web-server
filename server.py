from http.server import BaseHTTPRequestHandler, HTTPServer
import json

message = "Http-server"

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/message':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'message': message}
            self.wfile.write(json.dumps(response).encode())
        elif self.path == '/health':
            self.send_response(200)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()
server_address = ('', 8080)
httpd = HTTPServer(server_address, RequestHandler)
print('Launch http-server...')
httpd.serve_forever()