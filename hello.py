def app(environ, start_response):
    data = environ['QUERY_STRING']
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    data = '\n'.join(data.split('&')).encode('utf-8')
    return iter([data])
