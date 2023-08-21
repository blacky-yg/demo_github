from http.server import BaseHTTPRequestHandler, HTTPServer

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(body.decode('utf-8'))
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'ok')

def run_server(port=3000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, WebhookHandler)
    print(f'Server running at http://localhost:{port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
