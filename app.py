def application(env, start):
    body = b'Hello, World!\n'
    start(b"200 OK", [('Content-Length', str(len(body))), ('Content-Type', 'text/plain')])
    return [body]

try:
    import meinheld
    meinheld.server.set_access_logger(None)
    meinheld.server.set_error_logger(None)
    meinheld.server.set_keepalive(10)
except ImportError:
    pass
