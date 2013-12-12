
from cgi import parse_qs as cgi_parse_qs, parse_qsl as cgi_parse_qsl


class FieldStorage(object):

    def __init__(self, req):
        """Constructor.

        :arg req: The request object
        :type req: mod_python_wsgi.request.ModPythonRequest
        """
        # Parse request parameters into a single data structure
        self._multidict = req.request.params

    def __getattr__(self, name):
        if name in ['get', 'getfirst', 'getvalue']:
            return self._multidict.get
        elif name == 'getlist':
            return self._multidict.getall
        else:
            return getattr(self._multidict, name)


def parse_qs(*args):
    return cgi_parse_qs(*args)


def parse_qsl(*args):
    return cgi_parse_qsl(*args)


def redirect(req, location, permanent=0, text=None):
    req.response.location = location
    if permanent:
        req.response.status = 301
    else:
        req.response.status = 307
    if text:
        req.response.body = text
