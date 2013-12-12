"""WSGI Application to wrap a mod_python callable.

This is usually the `handler` function that would have been configured for
mod_python.
"""

from mod_python_wsgi.request import ModPythonRequest


class ModPythonWSGIApp(object):

    def __init__(self, callable_):
        self.callable = callable_

    def __call__(self, environ, start_response):
        request = ModPythonRequest(environ)
        retval = self.callable(request)
        if retval == 1:
            # Request declined !?
            request.response.status = "502 Bad Gateway"
        elif retval:
            request.response.status_code = retval
        else:
            # apache.OK
            request.response.status = "200 OK"

        return request.response(environ, start_response)
