from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class SimpleServer(BaseHTTPRequestHandler):
    def _set_response(self, status_code=200, content_type='text/html'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/submit_email':
            self._set_response()
            self.wfile.write("Submit Email Page".encode('utf-8'))
        else:
            self._set_response(404)
            self.wfile.write("Not Found".encode('utf-8'))

    def do_POST(self):
        if self.path == '/submit_email':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            parsed_data = urllib.parse.parse_qs(post_data.decode('utf-8'))
            email = parsed_data.get('email', [''])[0]

            response_message = f"Email received: {email}"
            self._set_response()
            self.wfile.write(response_message.encode('utf-8'))
        else:
            self._set_response(404)
            self.wfile.write("Not Found".encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleServer, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

