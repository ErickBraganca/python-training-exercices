from http.server import BaseHTTPRequestHandler
from routes.index import router

from json import dumps
from os import path

class ServerInstance(BaseHTTPRequestHandler):
  def set_HEAD(self, code, type):
    self.send_response(code)
    self.send_header('Content-type', type)
    self.send_header('Access-Control-Allow-Origin', 'All')
    self.end_headers()
    
  def do_GET(self):
    self.handler_Request('get')
    
  def do_POST(self):
    self.handler_Request('post')
    
  def handler_Request(self, method):
    path_request = self.path
    method_controller = router[method]
    router_data = method_controller(path_request)
    base_url = path.relpath('views')

    #Return of data package from router
    output_data = router_data['content']
    output_status = router_data['status']
    output_template = router_data['template']
    output_type = router_data['type']
    
    if output_template:
      view_url = path.join(base_url, output_data)
      output_view = open(view_url)
      output_content = output_view.read()
      response_content = bytes(str(output_content), 'utf-8')
      self.handler_Response(response_content, output_status, output_type)
    else:
      output_json = dumps(output_data)
      output_content = output_json.encode('utf-8')
      self.handler_Response(output_content, output_status, output_type)
  def handler_Response(self, content, code, type):
    self.set_HEAD(code, type)
    self.wfile.write(content)


