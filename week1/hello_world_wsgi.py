"""
Run this:
$ pip install gunicorn
$ gunicorn hello_world_wsgi:application
"""
def application(environ, start_response):
    data = b'Hello World\n'
    start_response('200 OK',
                  [('Content-Type', 'text/plain'),
                   ('Content-Length', str(len(data)))])

    return iter([data])
