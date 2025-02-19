from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		client_addr = self.client_address
		request_path = self.path
		print(f"Server received req from {client_addr} for path {self.path}")
		if self.path == "/":
			print("coucou")
			self.path = "index.html"
		try:
			with open(f'monsite/{self.path}', 'r') as f:
				content = f.read()
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			self.wfile.write(bytes(content, 'utf8'))
		except:
			self.send_response(404)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			self.wfile.write(b'404: File not found')

handler = MyHandler

httpd = HTTPServer(('', 8000),  handler)
httpd.serve_forever()
