def getRequest(path):
  dummy = {
    '/':{
    'content': 'index.html',
    'template': True,
    'type': 'text/html',
    'status': 200},

    '/content':{
    'content': {'result': 'Request Received!'},
    'template': False,
    'type': 'application/json',
    'status': 200},

    #Instance of error object for the exception request
    '404':{
    'content': {'result': 'Route not Found!'},
    'type': 'application/json',
    'status': 404}
  }
  try:
    return dummy[path]
  except KeyError:
    return dummy['404']
#Enter point of router
router = {
  'get': getRequest
}

