# Construction of basic http server without framework

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class ServerInstance(BaseHTTPRequestHandler):
    # Defining the basic header of server handler
    def set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Instancing the get method in the server instance
    def do_GET(self):
        # Setting the configurated header
        self.set_headers()

        output_data = {'status': 'OK', 'result': 'Request Received!'}
        output_json = json.dumps(output_data)

        self.wfile.write(output_json.encode('utf-8'))
# ----------------------------------------------------------------

config = {
    'class': HTTPServer,
    'instance': ServerInstance,
    'port': 5500,
    'host': 'localhost',
    'link': 'http://'
}

def RunServer(config):
    with config['class']((config['host'], config['port']), config['instance']) as webServer:
        print(f"Server Running in {config['link']}{config['host']}:{config['port']}")
        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            webServer.server_close()
            print('Server stopped.')

RunServer(config)
