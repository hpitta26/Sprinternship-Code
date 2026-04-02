from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello from Docker!</h1><p>Running on Python inside a container.</p>")
    def log_message(self, format, *args):
        pass  # suppress access logs

if __name__ == "__main__":
    print("Server running on http://localhost:8080")
    HTTPServer(("", 8080), Handler).serve_forever()
