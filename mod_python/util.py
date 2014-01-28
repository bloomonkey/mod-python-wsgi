
from cgi import FieldStorage as CGIFieldStorage
from cgi import parse_qs as cgi_parse_qs, parse_qsl as cgi_parse_qsl


class Field(object):

    def __init__(self, name, value):
        raise NotImplementedError()


class StringField(str):

    def __init__(self, value):
        super(StringField, self).__init__(value)

    @property
    def value(self):
        return self


class FieldStorage(CGIFieldStorage):

    def __init__(self, req, keep_blank_values=False, strict_parsing=None):
        """Constructor.

        :arg req: The request object
        :type req: mod_python_wsgi.request.ModPythonRequest
        :arg keep_blank_values: blank values in URL encoded form data should
            be treated as blank strings
        :type keep_blank_values: bool

        """
        # Parse request parameters into a single data structure
        self._multidict = req.request.params

    def get(self, name, default=None):
        val = self._multidict.get(name, default)
        if hasattr(val, 'read'):
            return Field(name, val)
        elif val is not None:
            return StringField(val)

    def getlist(self, name):
        l = []
        for val in self._multidict.getall(name):
            if hasattr(val, 'read'):
                l.append(Field(name, val))
            else:
                l.append(StringField(val))
        return l

    def getfirst(self, name, default=None):
        return self.get(name, default)

    def getvalue(self, name, default=None):
        val = self.getlist(name)
        if not val:
            return default
        elif len(val) == 1:
            return val[0]
        else:
            return val

    def has_key(self, key):
        return key in self._multidict


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
