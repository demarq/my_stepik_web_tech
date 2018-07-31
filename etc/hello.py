def app(environ, start_response):
    data = environ['QUERY_STRING']
    start_response('200 OK', [('Content-type', 'text/plain')])
    data = '\n'.join(data.split('&')).encode('utf-8')
    return iter([data])
