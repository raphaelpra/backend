from http.server import HTTPServer, BaseHTTPRequestHandler
import json

data_saved = {}

class EchoHttpHandlerWithPOST(BaseHTTPRequestHandler):
    def do_GET(self):
        client_addr = self.client_address
        request_path = self.path

        self.send_response(200)
        self.send_header(b'Content-type', b'text/html')
        self.end_headers()
        self.wfile.write( f"Server receive GET request {request_path} from {client_addr}".encode())

    def do_POST(self):
        client_addr = self.client_address
        request_path = self.path
        if request_path == "api/register":
            data_size = int(self.headers["Content-Length"])
            self.log_message( f"data_size = {data_size}")
            data_raw = self.rfile.read(data_size).decode()
            data_json = json.loads(data_raw)
            print(data_json)
        else:
            self.send_response(404)


server = HTTPServer(("", 8000), EchoHttpHandlerWithPOST)
server.serve_forever()
