from http.server import HTTPServer
from server import ServerInstance

HOST_NAME = 'localhost'
PORT_NUMBER = 8000
HTTP_PREFIX = 'http://'

def run_server(ServerClass, HOST, PORT, ServerInstance, URL):
    WebServer =  ServerClass((HOST, PORT), ServerInstance)
    print('Server UP - %s%s:%s' % (URL, HOST, PORT))
    try:
        WebServer.serve_forever()
    except KeyboardInterrupt:
        WebServer.server_close()
    print("Server DOWN - %s:%s" % (HOST_NAME, PORT_NUMBER))

run_server(HTTPServer, HOST_NAME, PORT_NUMBER, ServerInstance, HTTP_PREFIX)