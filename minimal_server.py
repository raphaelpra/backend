from http.server import HTTPServer, SimpleHTTPRequestHandler

handler = SimpleHTTPRequestHandler

print("Open this in your browser:\nhttp://localhost:9000/index.html")

httpd = HTTPServer(('', 9000),  handler)
httpd.serve_forever()
